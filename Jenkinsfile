pipeline {
    agent {
        // Use a WSL Ubuntu path as the workspace
        label ''
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository in /workspace (WSL path)
                script {
                    sh 'rm -rf /workspace/streamlit-app || true'
                    sh 'git clone https://github.com/GeorgiaChatz/project_test.git /workspace/streamlit-app'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                dir('/workspace/streamlit-app') {
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Run Streamlit App') {
            steps {
                dir('/workspace/streamlit-app') {
                    sh 'streamlit run app.py &'
                }
            }
        }
    }
}
