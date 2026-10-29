# CI/CD Pipeline Automation

Interview-ready DevOps project demonstrating:

**GitHub → Jenkins → Tests → Docker → AWS ECR → Kubernetes rolling deployment**

## Tech Stack
Python, Flask, Pytest, Docker, Jenkins, AWS ECR, Kubernetes, GitHub.

## Architecture
```text
GitHub -> Jenkins -> pytest -> Docker build -> AWS ECR -> Kubernetes
                                                        -> Pods x2
                                                        -> LoadBalancer
```

## Run locally
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python app/app.py
```

Or:
```bash
docker build -t ci-cd-demo:local .
docker run --rm -p 5000:5000 ci-cd-demo:local
```

## AWS ECR
Create the repository:
```bash
aws ecr create-repository --repository-name ci-cd-demo --region ap-south-1
```

The Jenkins agent needs Git, Python 3, Docker, AWS CLI and kubectl, plus permission to push to ECR and deploy to Kubernetes.

Create a Jenkins credential named `aws-account-id` containing your AWS account ID. In a real environment, use Jenkins credential binding or an IAM role for AWS authentication.

## Pipeline flow
1. Checkout source.
2. Create a Python virtual environment and run pytest.
3. Build a versioned Docker image.
4. Authenticate to ECR.
5. Push the image to ECR.
6. Replace `IMAGE_PLACEHOLDER` with the ECR image URI.
7. Apply the Kubernetes Deployment and Service.
8. Wait for the rolling deployment to complete.

## Interview points
**Why ECR?** Managed AWS container registry with IAM integration.

**Why RollingUpdate?** Gradually replaces old Pods, reducing downtime.

**What would you improve?** Add GitHub webhooks, static analysis, Trivy image scanning, EKS/Terraform, Helm, Prometheus/Grafana, and canary or blue/green deployments.

## Security
Never commit AWS keys, kubeconfig files, passwords, or Jenkins secrets. Use secret management/IAM instead.
