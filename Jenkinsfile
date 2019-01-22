def git_repository = 'https://github.com/ONSdigital/onse-banking-app-infrastructure'
def namespace = 'aklearning'

def kubectl_image = 'aklearning/onse-eks-kubectl-deployer:0.0.1'

def git_commit = ''

def label = "build-${UUID.randomUUID().toString()}"
def build_pod_template = """
kind: Pod
metadata:
  name: build-pod
spec:
  containers:
  - name: kubectl
    image: ${kubectl_image}
    imagePullPolicy: Always
    tty: true
"""

podTemplate(name: 'app-infrastructure-build', label: label, yaml: build_pod_template) {
  node(label) {
    git git_repository

    stage('Deploy to Kubernetes') {
      withCredentials([
        string(credentialsId: 'AWS_ACCESS_KEY_ID', variable: 'AWS_ACCESS_KEY_ID'),
        string(credentialsId: 'AWS_SECRET_ACCESS_KEY', variable: 'AWS_SECRET_ACCESS_KEY'),
        string(credentialsId: 'KUBERNETES_SERVER', variable: 'KUBERNETES_SERVER'),
        file(credentialsId: 'KUBERNETES_CA', variable: 'KUBERNETES_CA')
      ]) {
        container(name: 'kubectl', shell: '/bin/sh') {
          sh '''kubectl config \
              set-cluster kubernetes \
              --server=$KUBERNETES_SERVER \
              --certificate-authority=$KUBERNETES_CA
          '''
          sh "kubectl create namespace ${namespace} || true"
          sh "kubectl apply -n ${namespace} -f kubernetes/"
        }
      }
    }
  }
}
