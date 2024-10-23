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
    environment {
        PROJECT_NAME = "streamlit-app"
    }
    stages {
        stage('Setup Workspace') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        env.WORKSPACE_PATH = "/workspace/${PROJECT_NAME}"
                    } else {
                        env.WORKSPACE_PATH = "/workspace-dev/${PROJECT_NAME}"
                    }
                    echo "Using workspace path: ${env.WORKSPACE_PATH}"
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    echo "Building ${PROJECT_NAME} in ${env.WORKSPACE_PATH}"
                    // Assuming your build command here. Adjust it based on your actual build process.
                    sh """
                        mkdir -p ${env.WORKSPACE_PATH}
                        cd ${env.WORKSPACE_PATH}
                        # Example build commands - adjust to your application needs
                        # e.g., git clone your repo or run any build scripts/commands
                        # git clone https://github.com/your-repo.git .
                        # Run build commands for your project here
                        echo "Build process executed for ${PROJECT_NAME} in ${env.WORKSPACE_PATH}"
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'main') {
                        echo "Deploying ${PROJECT_NAME} to the production environment"
                        // Production deployment commands here
                        sh """
                            # Deploy commands for production environment
                            # For example, copy files, run deployment scripts, etc.
                            echo "Production deployment complete for ${PROJECT_NAME}"
                        """
                    } else {
                        echo "Deploying ${PROJECT_NAME} to the development environment"
                        // Development deployment commands here
                        sh """
                            # Deploy commands for development environment
                            # For example, copy files, run deployment scripts, etc.
                            echo "Development deployment complete for ${PROJECT_NAME}"
                        """
                    }
                }
            }
        }
    }
}

