
@Library ("shared-library") _
pipeline {
    agent any
    environment {
      JIRA_URL = "https://hamza2022.atlassian.net/"
      JIRA_CREDENTIALS = credentials("jira-jenkins1")
    }

    stages {
        stage('pulling from github') {
            steps {
               git branch: 'main',
               credentialsId: 'ae737c21-98c1-48c1-a3a6-32eb8f9a3195',
               url: 'https://github.com/Hamzam2022/django_ecommerce_testing.git'
            }
        }
        stage ("Build python"){
            steps{
                bat '''python -m venv venv
                . venv/Scripts/activate
                pip install -r requirements.txt'''
            }
        }

         stage('Running tests') {
            steps {
                bat '''python -m pytest
                python -m pytest --alluredir=allure-results
                python -m pytest --html="report.html "
                   '''

            }
         }
          stage('Running Docker') {
            steps {
                bat '''
                // docker stop django-project
                docker image build -t django-project .
                docker run -p 5000:5000 -d django-project
                   '''
            }

        }



    }
     post {
        failure {
        // Create Jira issue and attach html and allure reports.
        echo 'Build has failed opening jira issue!'

      bat '''curl -D- -u mograbi.ha@gmail.com:uDXhOxsy6bYgu9WwVmDUE46C -X POST --data "@"C:\\Users\\Hamza\\OneDrive\\Desktop\\add.txt"" -H "Content-Type:application/json" https://hamza2022.atlassian.net/rest/api/2/issue/'''
      }
        always {

            publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: false,
            keepAll: false,
            reportDir: '',
            reportFiles: 'report.html',
            reportName: 'HTML Report',
            reportTitles: 'Pytest Report'])

            allure includeProperties: false, jdk: '', properties: [[key: '', value: '']], results: [[path: 'allure-results']]


            // emailext body: 'A Test EMail', recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']], subject: 'Test'
        }


    }
}