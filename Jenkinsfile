pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Docker image...'
                script {
                    sh 'docker build -t my-website:latest .'
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Running Selenium tests...'
                script {
                    sh 'python3 run_selenium_tests.py'  // Add the test script later
                }
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running SonarQube analysis...'
                script {
                    sh 'sonar-scanner -Dsonar.projectKey=my-website -Dsonar.sources=. -Dsonar.host.url=http://localhost:9000 -Dsonar.login=mySonarToken'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to test environment...'
                script {
                    sh 'docker run -d -p 8080:80 my-website:latest'
                }
            }
        }

        stage('Release') {
            steps {
                echo 'Promoting to production environment...'
                script {
                    sh 'scp index.html user@production-server:/var/www/html/'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
