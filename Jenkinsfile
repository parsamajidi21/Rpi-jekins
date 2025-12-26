pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install gpiozero --break-system-packages'
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Testing code logic with Mock Pins...'
                // This will fail the build if the test_blink.py script fails
                sh 'python3 test_blink.py'
            }
        }

        stage('Deploy & Run') {
            // This only runs if 'Run Unit Tests' passes!
            steps {
                sh 'pkill -f blink.py || true'
                sh 'nohup python3 blink.py > /dev/null 2>&1 &'
            }
        }
    }
}
