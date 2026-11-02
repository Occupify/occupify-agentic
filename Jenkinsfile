pipeline {
    agent any

    environment {
        APP_ENV = 'test'
        REGISTRY = 'ghcr.io'
        IMAGE_NAME = 'occupify/occupify-agentic'
    }

    options {
        timeout(time: 25, unit: 'MINUTES')
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    if (fileExists('occupify-agentic/pyproject.toml')) {
                        env.SERVICE_DIR = 'occupify-agentic'
                    } else {
                        env.SERVICE_DIR = '.'
                    }

                    env.FULL_IMAGE = "${env.REGISTRY}/${env.IMAGE_NAME}".toLowerCase()
                }

                sh '''
                    set -eu
                    command -v podman
                    podman --version
                    command -v uv
                    uv --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${env.SERVICE_DIR}") {
                    sh 'uv sync --locked'
                }
            }
        }

        stage('Lint & Format') {
            steps {
                dir("${env.SERVICE_DIR}") {
                    sh 'uv run ruff format --check .'
                    sh 'uv run ruff check .'
                }
            }
        }

        stage('Unit Tests') {
            steps {
                dir("${env.SERVICE_DIR}") {
                    sh '''
                        mkdir -p reports
                        uv run pytest \
                            --junitxml=reports/junit.xml \
                            --cov=app \
                            tests/unit/
                    '''
                }
            }

            post {
                always {
                    dir("${env.SERVICE_DIR}") {
                        junit testResults: 'reports/junit.xml',
                              allowEmptyResults: true
                    }
                }
            }
        }

        stage('Build Image') {
            steps {
                dir("${env.SERVICE_DIR}") {
                    sh '''
                        set -eu
                        podman build \
                            -t "${FULL_IMAGE}:${BUILD_NUMBER}" \
                            -t "${FULL_IMAGE}:latest" \
                            .
                    '''
                }
            }
        }

        stage('Push Image') {
            when {
                expression {
                    env.BRANCH_NAME == 'main' ||
                    env.GIT_BRANCH == 'origin/main' ||
                    env.GIT_BRANCH == 'main'
                }
            }

            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ghcr-credentials',
                        usernameVariable: 'GHCR_USERNAME',
                        passwordVariable: 'GHCR_TOKEN'
                    )
                ]) {
                    sh '''
                        set -eu

                        printf '%s' "$GHCR_TOKEN" |
                            podman login "$REGISTRY" \
                                --username "$GHCR_USERNAME" \
                                --password-stdin

                        podman push "${FULL_IMAGE}:${BUILD_NUMBER}"
                        podman push "${FULL_IMAGE}:latest"

                        podman logout "$REGISTRY"
                    '''
                }
            }
        }

        stage('Deploy (Local GitOps)') {
            when {
                branch 'main'
            }

            steps {
                sh '''
                    set -eu

                    echo ">> Deploying occupify-agentic..."

                    GITOPS_DIR=""
                    if [ -d "/home/occupify/occupify-gitops" ]; then
                        GITOPS_DIR="/home/occupify/occupify-gitops"
                    elif [ -d "$HOME/occupify-gitops" ]; then
                        GITOPS_DIR="$HOME/occupify-gitops"
                    fi

                    if [ -n "$GITOPS_DIR" ]; then
                        echo ">> Running GitOps deployment..."
                        cd "$GITOPS_DIR"
                        make be-agentic
                    else
                        echo ">> Deploying with Podman and systemd..."

                        podman pull "${FULL_IMAGE}:latest"

                        export XDG_RUNTIME_DIR="/run/user/$(id -u)"
                        export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"

                        systemctl --user daemon-reload
                        systemctl --user restart occupify-be-agentic
                    fi

                    echo ">> Container status:"
                    podman ps --filter name=occupify-agentic
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed: build ${BUILD_NUMBER}"
        }

        failure {
            echo "CI/CD pipeline failed on build ${BUILD_NUMBER}"
        }

        success {
            echo "CI/CD pipeline succeeded: occupify-agentic"
        }
    }
}
