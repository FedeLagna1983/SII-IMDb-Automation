pipeline {
    agent any

    options {
        timestamps()
    }

    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['all', 'pytest', 'behave'],
            description: 'Select which suite to run.'
        )
        string(
            name: 'PYTEST_ARGS',
            defaultValue: '-v',
            description: 'Extra pytest args (example: -v -n auto).'
        )
        string(
            name: 'BEHAVE_TAGS',
            defaultValue: '',
            description: 'Optional behave tag expression (example: @nicolas_cage).'
        )
        string(
            name: 'BEHAVE_EXTRA_ARGS',
            defaultValue: '',
            description: 'Extra behave args.'
        )
        booleanParam(
            name: 'INSTALL_BROWSERS',
            defaultValue: true,
            description: 'Install Playwright browsers before running tests.'
        )
    }

    environment {
        VENV_DIR = '.venv'
        PYTHONUNBUFFERED = '1'
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Validate Agent') {
            steps {
                script {
                    if (!isUnix()) {
                        error('This Jenkinsfile is configured for Linux agents. Use a Linux node or adapt commands for Windows.')
                    }
                }
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                    set -e
                    python3 --version
                    python3 -m venv "${VENV_DIR}"
                    . "${VENV_DIR}/bin/activate"
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt

                    if [ "${INSTALL_BROWSERS}" = "true" ]; then
                      python -m playwright install chromium firefox
                    fi
                '''
            }
        }

        stage('Run Pytest') {
            when {
                expression { params.TEST_SUITE == 'all' || params.TEST_SUITE == 'pytest' }
            }
            steps {
                sh '''
                    set -e
                    . "${VENV_DIR}/bin/activate"
                    mkdir -p reports/pytest

                    if command -v xvfb-run >/dev/null 2>&1; then
                      xvfb-run -a pytest ${PYTEST_ARGS} --junitxml=reports/pytest/junit.xml
                    else
                      pytest ${PYTEST_ARGS} --junitxml=reports/pytest/junit.xml
                    fi
                '''
            }
        }

        stage('Run Behave') {
            when {
                expression { params.TEST_SUITE == 'all' || params.TEST_SUITE == 'behave' }
            }
            steps {
                sh '''
                    set -e
                    . "${VENV_DIR}/bin/activate"
                    mkdir -p reports/behave

                    TAG_ARGS=""
                    if [ -n "${BEHAVE_TAGS}" ]; then
                      TAG_ARGS="--tags ${BEHAVE_TAGS}"
                    fi

                    if command -v xvfb-run >/dev/null 2>&1; then
                      xvfb-run -a python -m behave ${TAG_ARGS} ${BEHAVE_EXTRA_ARGS} --junit --junit-directory reports/behave
                    else
                      python -m behave ${TAG_ARGS} ${BEHAVE_EXTRA_ARGS} --junit --junit-directory reports/behave
                    fi
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/**/*.xml'
            archiveArtifacts allowEmptyArchive: true, artifacts: 'reports/**, screenshots/**'
        }
    }
}
