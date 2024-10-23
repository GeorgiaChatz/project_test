pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    environment {
        WORKSPACE_DIR = ''
    }
    stages {
        stage('Determine Branch and Workspace') {
            steps {
                script {
                    // Get the branch name
                    def branchName = env.BRANCH_NAME

                    // Set workspace directory based on branch name
                    if (branchName == 'main') {
                        env.WORKSPACE_DIR = '/workspace/streamlit-app'
                    } else {
                        env.WORKSPACE_DIR = '/workspace-dev/streamlit-app'
                    }

                    echo "Building branch: ${branchName}"
                    echo "Workspace Directory: ${env.WORKSPACE_DIR}"
                }
            }
        }
        stage('Setup Workspace') {
            steps {
                sh 'mkdir -p ${WORKSPACE_DIR}'
            }
        }
        stage('Checkout Code') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    // Clean workspace (optional)
                    deleteDir()
                    // Checkout code
                    checkout scm
                }
            }
        }
        stage('Build') {
            steps {
                dir("${env.WORKSPACE_DIR}") {
                    // Your build commands here
                    sh 'echo Building...'
                }
            }
        }
        // Add additional stages as needed
    }
}
