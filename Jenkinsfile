pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from GitHub/GitLab
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Ensure the gpiozero library is available
                sh 'pip3 install gpiozero --break-system-packages'
            }
        }

        stage('Deploy & Run') {
            steps {
                echo 'Starting the LED Blink script...'
                // Running in the background so Jenkins doesn't hang
                sh 'nohup python3 blink.py &'
            }
        }
    }
}
