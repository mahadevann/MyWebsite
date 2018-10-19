pipeline {
    agent any
    stages {
	stage('Web') {
		steps{
			sh 'docker-compose up'
		}
	}
        stage('build') {
            steps {
                sh '''
		python --version
		'''
            }
        }
    }
}
