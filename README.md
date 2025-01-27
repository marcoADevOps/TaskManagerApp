Task Manager Application
A simple Python-based Task Manager application with a SQLite database. This application allows users to add, view, and delete tasks. It is containerized using Docker and can be deployed to AWS ECS with Terraform.

Features
Add Tasks: Add new tasks with a title and description.

View Tasks: View all tasks in the database.

Delete Tasks: Delete tasks by their ID.

Database Layer: Uses SQLite for local development and can be adapted for PostgreSQL or MySQL for production.

Containerized: Dockerized for easy deployment.

Infrastructure as Code: Terraform scripts to deploy the application on AWS ECS with RDS (PostgreSQL).

Project Structure
Copy
TaskManagerApp/
│
├── app.py                # Main application logic
├── database.py           # Database operations (SQLite)
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
├── main.tf               # Terraform configuration for AWS ECS and RDS
└── README.md             # Project documentation
Prerequisites
Python 3.9+

Docker

Terraform

AWS Account (for deployment)

Getting Started
1. Clone the Repository
bash
Copy
git clone https://github.com/marcoADevOps/TaskManagerApp.git
cd TaskManagerApp
2. Run Locally
Install Python dependencies (if any):

bash
Copy
pip install -r requirements.txt
Run the application:

bash
Copy
python app.py
3. Build and Run with Docker
Build the Docker image:

bash
Copy
docker build -t task-manager-app .
Run the Docker container:

bash
Copy
docker run -it --rm -p 4000:80 task-manager-app
4. Deploy to AWS ECS with Terraform
Initialize Terraform:

bash
Copy
terraform init
Apply the Terraform configuration:

bash
Copy
terraform apply
Push the Docker image to Amazon ECR:

bash
Copy
docker push <ecr-repository-url>:latest
Access the application via the ECS service endpoint.

Terraform Infrastructure
The Terraform configuration provisions the following AWS resources:

ECS Cluster: Hosts the Task Manager application.

RDS Instance: PostgreSQL database for task storage.

VPC, Subnets, and Security Groups: Networking configuration for ECS and RDS.

ECR Repository: Stores the Docker image for the application.

Environment Variables
For production, you can configure the following environment variables:

DATABASE_URL: Connection string for the database (e.g., PostgreSQL).

PORT: Port on which the application runs (default: 80).

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Author
Marco A. DevOps

GitHub: marcoADevOps

