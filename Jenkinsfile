pipeline {
    agent any

    environment {
        APP_ENV = 'test'
        REGISTRY = 'ghcr.io'
        IMAGE_NAME = 'occupify/occupify-agentic'
    }

    options {
        timeout(time: 60, unit: 'MINUTES')
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
                    command -v docker
                    docker --version
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
                        docker build \
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

                        printf '%s' "$GHCR_TOKEN" | \
                            docker login "$REGISTRY" \
                                --username "$GHCR_USERNAME" \
                                --password-stdin

                        docker push "${FULL_IMAGE}:${BUILD_NUMBER}"
                        docker push "${FULL_IMAGE}:latest"

                        docker logout "$REGISTRY"
                    '''
                }
            }
        }

        stage('Deploy (Local GitOps)') {
            when {
                expression {
                    env.BRANCH_NAME == 'main' ||
                    env.GIT_BRANCH == 'origin/main' ||
                    env.GIT_BRANCH == 'main'
                }
            }

            steps {
                sh '''
                    set -eu

                    echo ">> Deploying occupify-agentic with Podman..."

                    OCCUPIFY_UID=$(id -u occupify)
                    GITOPS_DIR="/home/occupify/.config/systemd/user/git-ops"

                    if [ ! -d "$GITOPS_DIR" ]; then
                        echo "ERROR: GitOps directory not found: $GITOPS_DIR"
                        exit 1
                    fi

                    echo ">> Running deployment as occupify..."

                    sudo -u occupify env \
                        HOME=/home/occupify \
                        XDG_RUNTIME_DIR="/run/user/$OCCUPIFY_UID" \
                        DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$OCCUPIFY_UID/bus" \
                        FULL_IMAGE="${FULL_IMAGE}" \
                        bash -c '
                            set -eu

                            cd /home/occupify/.config/systemd/user/git-ops

                            echo ">> Pulling latest image from GHCR..."
                            podman pull "${FULL_IMAGE}:latest"

                            echo ">> Reloading user systemd..."
                            systemctl --user daemon-reload

                            echo ">> Restarting Occupify Agentic..."
                            systemctl --user restart occupify-be-agentic.service

                            echo ">> Waiting for service..."
                            sleep 5

                            echo ">> Service status:"
                            systemctl --user --no-pager --full status occupify-be-agentic.service

                            echo ">> Container status:"
                            podman ps -a --filter name=occupify-agentic
                        '

                    echo ">> Deployment completed."
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
