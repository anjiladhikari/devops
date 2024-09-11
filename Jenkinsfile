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
                    sh 'python3 run_selenium_tests.py'
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

        // Monitoring and Alerting stage
        stage('Monitoring and Alerting') {
            steps {
                echo 'Setting up Monitoring and Alerting...'
                script {
                    // Example using Datadog or New Relic APIs to ensure the monitoring is active
                    // For Datadog:
                    sh '''
                    curl -X POST \
                    -H "DD-API-KEY: your-datadog-api-key" \
                    -H "Content-Type: application/json" \
                    -d '{
                        "monitor_name": "Website Uptime Monitor",
                        "query": "avg(last_5m):avg:http.response_time{*} > 500",
                        "type": "metric alert",
                        "message": "Alert: High response time detected!",
                        "tags": ["env:production"]
                    }' \
                    "https://api.datadoghq.com/api/v1/monitor"
                    '''
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
