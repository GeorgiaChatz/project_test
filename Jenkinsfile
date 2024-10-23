// Declare WORKSPACE_DIR as a global variable
def WORKSPACE_DIR = ''
// Declare branchName as a global variable
def branchName = ''

pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Determine Branch and Workspace') {
            steps {
                script {
                    // Get the branch name
                    branchName = env.BRANCH_NAME ?: 'main' // Default to 'main' if BRANCH_NAME is not set

                    // Set workspace directory based on branch name
                    if (branchName == 'main') {
                        WORKSPACE_DIR = '/workspace/streamlit-app'
                    } else {
                        WORKSPACE_DIR = '/workspace-dev/streamlit-app'
                    }

                    echo "Building branch: ${branchName}"
                    echo "Workspace Directory: ${WORKSPACE_DIR}"
                }
            }
        }
        stage('Setup Workspace') {
            steps {
                sh "mkdir -p ${WORKSPACE_DIR}"
            }
        }
        stage('Checkout Code') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    // Clean workspace (optional)
                    deleteDir()
                    // Checkout code
                    checkout scm
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    // Install required packages
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Build') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    // Build commands (if any)
                    sh 'echo Building the application...'
                }
            }
        }
        stage('Test') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    // Run tests
                    sh 'echo Running tests...'
                    // Example: sh 'python -m unittest discover tests'
                }
            }
        }
        stage('Deploy') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    script {
                        if (branchName == 'main') {
                            // Deploy to production
                            sh 'echo Deploying to Production...'
                            // Add your production deployment commands here
                            // For example:
                            // sh 'sudo systemctl restart streamlit-app'
                        } else {
                            // Deploy to development environment
                            sh 'echo Deploying to Development...'
                            // Add your development deployment commands here
                            // For example:
                            // sh 'sudo systemctl restart streamlit-app-dev'
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
