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

                    echo ">> Running server-side deployment script..."
                    sudo -n -u occupify /usr/local/sbin/occupify-agentic-deploy
                '''
            }
        }

        stage('Trigger Contribution Sync') {
            when {
                expression {
                    env.BRANCH_NAME == 'main' ||
                    env.GIT_BRANCH == 'origin/main' ||
                    env.GIT_BRANCH == 'main'
                }
            }

            steps {
                echo '>> Triggering downstream Contribution Sync pipeline...'
                build job: 'occupify-contribution-sync',
                      parameters: [
                          string(name: 'SOURCE_BRANCH', value: env.BRANCH_NAME ?: 'main'),
                          string(name: 'TRIGGERED_BY_BUILD', value: "${env.BUILD_NUMBER}")
                      ],
                      wait: true
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
