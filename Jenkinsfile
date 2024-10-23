//
// def WORKSPACE_DIR = ''
// def branchName = ''
//
// pipeline {
//     agent any
//     options {
//         skipDefaultCheckout(true)
//     }
//     stages {
//         stage('Determine Branch and Workspace') {
//             steps {
//                 script {
//                     branchName = env.BRANCH_NAME ?: 'main' // Default to 'main' if BRANCH_NAME is not set
//
//                     if (branchName == 'main') {
//                         WORKSPACE_DIR = '/workspace/streamlit-app'
//                     } else {
//                         WORKSPACE_DIR = '/workspace-dev/streamlit-app'
//                     }
//
//                     echo "Building branch: ${branchName}"
//                     echo "Workspace Directory: ${WORKSPACE_DIR}"
//                 }
//             }
//         }
//         stage('Setup Workspace') {
//             steps {
//                 sh "mkdir -p ${WORKSPACE_DIR}"
//             }
//         }
//         stage('Checkout Code') {
//             steps {
//                 dir("${WORKSPACE_DIR}") {
//                     deleteDir()
//                     checkout scm
//                 }
//             }
//         }
//         stage('Install Dependencies') {
//             steps {
//                 dir("${WORKSPACE_DIR}") {
//                     sh 'pip install -r requirements.txt'
//                 }
//             }
//         }
//         stage('Build') {
//             steps {
//                 dir("${WORKSPACE_DIR}") {
//                     sh 'echo Building the application...'
//                 }
//             }
//         }
//         stage('Test') {
//             steps {
//                 dir("${WORKSPACE_DIR}") {
//                     sh 'echo Running tests...'
//                     // Example: sh 'python -m unittest discover tests'
//                 }
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 dir("${WORKSPACE_DIR}") {
//                     script {
//                         if (branchName == 'main') {
//                             // Deploy to production
//                             sh 'echo Deploying to Production...'
//                             // Add your production deployment commands here
//                             // For example:
//                             // sh 'sudo systemctl restart streamlit-app'
//                         } else {
//                             // Deploy to development environment
//                             sh 'echo Deploying to Development...'
//                             // Add your development deployment commands here
//                             // For example:
//                             // sh 'sudo systemctl restart streamlit-app-dev'
//                         }
//                     }
//                 }
//             }
//         }
//     }
//     post {
//         always {
//             echo 'Pipeline execution completed.'
//         }
//         success {
//             echo 'Build succeeded!'
//         }
//         failure {
//             echo 'Build failed.'
//         }
//     }
// }
// Declare WORKSPACE_DIR and branchName as global variables
def WORKSPACE_DIR = ''
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
                    branchName = env.BRANCH_NAME ?: 'main'
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
                    deleteDir()
                    checkout scm
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Build') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh 'echo Building the application...'
                    // Add build steps if necessary
                }
            }
        }
        stage('Test') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    sh 'echo Running tests...'
                    // Add test commands
                }
            }
        }
        stage('Deploy') {
            steps {
                dir("${WORKSPACE_DIR}") {
                    script {
                        if (branchName == 'main') {
                            sh 'echo Deploying to Production...'
                            sh '''
                                if screen -list | grep -q "streamlit_app_prod"; then
                                    screen -S streamlit_app_prod -X quit
                                fi
                            '''
                            // Start Streamlit app in screen session
                            sh '''
                                screen -dmS streamlit_app_prod bash -c "cd /workspace/streamlit-app && streamlit run app.py > /workspace/streamlit_prod.log 2>&1"
                            '''
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
