# Pandoc API on Azure Container

This repository contains the code for a Pandoc API service running on an Azure Container. The service allows users to convert documents from one markup format to another using Pandoc.

## Features

- **Document Conversion**: Convert documents between various formats supported by Pandoc.
- **Dockerized**: Runs in a Docker container for easy deployment.
- **Azure Integration**: Optimized for deployment on Azure Container Instances.

## Technologies Used

- **Python**: The primary programming language used for the API.
- **Docker**: Containerization of the application.
- **Pandoc**: The document conversion tool.
- **Azure**: Cloud platform for hosting the container.

## Getting Started

### Prerequisites

- Docker installed on your local machine.
- Azure account for deploying the container.
- Python (if you plan to run the service locally).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kressety/pandoc-api.git
    cd pandoc-api
    ```

2. Build the Docker image:
    ```sh
    docker build -t pandoc-api .
    ```

3. Run the Docker container:
    ```sh
    docker run -p 8000:8000 pandoc-api
    ```

### Usage

Once the Docker container is running, you can access the API at `http://localhost:8000`. Use the API endpoints to convert documents between different formats. Detailed documentation for the API endpoints can be found in the `docs` directory of this repository.

### Deployment on Azure

To deploy the service on Azure Container Instances, follow these steps:

1. Login to your Azure account:
    ```sh
    az login
    ```

2. Create a resource group:
    ```sh
    az group create --name pandoc-api-rg --location eastus
    ```

3. Create a container instance:
    ```sh
    az container create --resource-group pandoc-api-rg --name pandoc-api --image your-dockerhub-username/pandoc-api --dns-name-label pandoc-api --ports 8000
    ```

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
