pipeline {
    agent any
    stages {
	stage('Web') {
		steps{
		sh "dcoker run -d -p mahadevann/myenv:test1"
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
