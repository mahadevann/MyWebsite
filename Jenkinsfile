pipeline {
    agent any
    stages {
	stage('Web') {
		steps{
		sh "docker run --name dapp -p 8000:8000 -d mahadevann/myenv:test1"
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
