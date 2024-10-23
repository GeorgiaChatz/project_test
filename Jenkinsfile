// pipeline {
//     agent any
//     stages {
//         stage('Clone Repository') {
//             steps {
//                 // Clone the repository in /workspace (WSL path)
//                 script {
//                     sh 'rm -rf /workspace/streamlit-app || true'
//                     sh 'git clone https://github.com/GeorgiaChatz/project_test.git /workspace/streamlit-app'
//                 }
//             }
//         }
//         stage('Install Dependencies') {
//             steps {
//                 dir('/workspace/streamlit-app') {
//                     sh 'pip3 install -r requirements.txt'
//                 }
//             }
//         }
//         stage('Run Streamlit App') {
//             steps {
//                 dir('/workspace/streamlit-app') {
//                     sh 'streamlit run app.py &'
//                 }
//             }
//         }
//     }
// }
pipeline {
    agent any
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage('Setup Workspace') {
            steps {
                // Ensure the workspace directory exists
                sh 'mkdir -p /workspace/streamlit-app'
            }
        }
        stage('Checkout Code') {
            steps {
                dir('/workspace/streamlit-app') {
                    // Clean workspace (optional)
                    deleteDir()
                    // Checkout code
                    checkout scm
                }
            }
        }
        stage('Build') {
            steps {
                dir('/workspace/streamlit-app') {
                    // Your build commands here
                    sh 'echo Building...'
                }
            }
        }
        stage('Test') {
            steps {
                dir('/workspace/streamlit-app') {
                    // Your test commands here
                    sh 'echo Testing...'
                }
            }
        }
        stage('Deploy') {
            steps {
                dir('/workspace/streamlit-app') {
                    // Your deploy commands here
                    sh 'echo Deploying...'
                }
            }
        }
    }
}
