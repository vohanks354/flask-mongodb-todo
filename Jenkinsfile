pipeline {
    environment {
        PROJECT_DEV="kirom-hadiyanto-dev"
        APP_NAME_DEV = "todo-api"
        DB_NAME_DEV = "mongodb-dev"
        GIT_REPO="git@github.com:vohanks354/flask-mongodb-todo.git"
        GIT_BRANCH="master"
    }

    agent any

    stages{
        stage('Get Latest Code') {
            steps {
                script {
                    try {
                        // git branch: "${GIT_BRANCH}", url: "${GIT_REPO1}", credentialsId: "${GIT_CRED1}"
                        git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage("Authentication Credential") {
            steps {
                script{
                    sh "oc login --token=sha256~v-IYTez-PqyVtHXYuEBY8yNBeVficMzjX_V-SptNuHo --server=https://api.sandbox-m2.ll9k.p1.openshiftapps.com:6443"
                    sh "oc project ${PROJECT_DEV}"
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc delete all -l app=${APP_NAME_DEV}"
                            }, 
                            'MonggoDB': {
                                sh "oc delete all -l app=${DB_NAME_DEV}"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Config') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc create -f yaml/buildconfig.yaml"
                            }, 
                            'MonggoDB': {
                                sh "oc create -f yaml/buildconfigdb.yaml"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Imagestream') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc create -f yaml/imagestream.yaml"
                            }, 
                            'MonggoDB': {
                                sh "oc create -f yaml/imagestreamdb.yaml"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Application') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc start-build ${APP_NAME_DEV} --from-dir=./ --follow"
                            }, 
                            'MonggoDB': {
                                sh "oc start-build ${DB_NAME_DEV} --from-dir=./ --follow"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Deployment') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc create -f yaml/deployment.yaml"
                            }, 
                            'MonggoDB': {
                                sh "oc create -f yaml/deploymentdb.yaml"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Service') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc create -f yaml/service.yaml"
                            }, 
                            'MonggoDB': {
                                sh "oc create -f yaml/servicedb.yaml"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
        stage('Build Route') {
            steps {
                script {
                    try {
                        parallel(
                            'Application': {
                                sh "oc create -f yaml/route.yaml"
                            }, 
                            'MonggoDB': {
                                sh "oc create -f yaml/routedb.yaml"
                            }
                        )
                    } catch (Exception e) {
                        sh "echo ${e}"
                    }
                }
            }
        }
    }
    post { 
        success { 
            echo 'Mission complete'
        }
        failure { 
            echo 'Mission failure'
        }
    }
}