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
                    // Guarantee image name is always strictly lowercase for GHCR/Docker
                    env.FULL_IMAGE = "${env.REGISTRY}/${env.IMAGE_NAME}".toLowerCase()
                }
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
                    sh 'mkdir -p reports'
                    sh 'uv run pytest --junitxml=reports/junit.xml --cov=app tests/unit/'
                }
            }
            post {
                always {
                    dir("${env.SERVICE_DIR}") {
                        junit testResults: 'reports/junit.xml', allowEmptyResults: true
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                dir("${env.SERVICE_DIR}") {
                    sh "docker build -t ${env.FULL_IMAGE}:${BUILD_NUMBER} -t ${env.FULL_IMAGE}:latest ."
                }
            }
        }

        stage('Push Image') {
            when {
                branch 'main'
            }
            steps {
                sh """
                    docker push ${env.FULL_IMAGE}:${BUILD_NUMBER}
                    docker push ${env.FULL_IMAGE}:latest
                """
            }
        }

        stage('Deploy (Local GitOps)') {
            when {
                branch 'main'
            }
            steps {
                sh '''
                    echo ">> Deploying occupify-agentic on local server..."
                    
                    GITOPS_DIR=""
                    if [ -d "/home/occupify/occupify-gitops" ]; then
                        GITOPS_DIR="/home/occupify/occupify-gitops"
                    elif [ -d "$HOME/occupify-gitops" ]; then
                        GITOPS_DIR="$HOME/occupify-gitops"
                    fi

                    if [ -n "$GITOPS_DIR" ]; then
                        echo ">> Running make be-agentic in $GITOPS_DIR..."
                        cd "$GITOPS_DIR" && make be-agentic
                    else
                        echo ">> Restarting occupify-be-agentic via systemd..."
                        export XDG_RUNTIME_DIR="/run/user/$(id -u)"
                        export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(id -u)/bus"
                        podman pull "${FULL_IMAGE}:latest"
                        systemctl --user daemon-reload
                        systemctl --user restart occupify-be-agentic
                    fi

                    echo ">> Checking container status:"
                    podman ps --filter name=occupify-agentic || true
                '''
            }
        }
    }

    post {
        failure {
            echo "CI/CD Pipeline failed on build ${BUILD_NUMBER}"
        }
        success {
            echo "CI/CD Pipeline succeeded: occupify-agentic deployed via local GitOps."
        }
    }
}
