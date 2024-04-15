
# Project Title: Embedding-a-Machine-Learning-Model-into-a-Web-App- (A Sepsis Detection API)

### Overview:

The Sepsis Detection API project aims to develop a FastAPI application for predicting the likelihood of sepsis development in ICU patients based on critical clinical indicators. The project involves building a machine learning model using Python and scikit-learn, developing a FastAPI interface for making predictions, containerizing the application with Docker for easy deployment, and saving the container image on Docker Hub for distribution.

### Project Requirements:
##### 1. Machine Learning Model Development:
     - Build a predictive model using scikit-learn to detect sepsis based on clinical indicators.
     - Experiment with different machine learning algorithms such as Gradient Boosting, Logistic Regression, and Random Forest to determine the most effective model.

##### 2. FastAPI Development:
    - Develop a FastAPI application using Python to serve as the interface for making sepsis predictions.
     - Create endpoints for each machine learning model to handle prediction requests.
    - Implement data validation using Pydantic to ensure the integrity of input data.

##### 3. Containerization with Docker:
     - Containerize the FastAPI application using Docker to encapsulate the application and its dependencies.
    - Write a Dockerfile to define the steps for building the Docker image.
     - Ensure that the Docker container exposes the necessary ports for communication with the FastAPI application.

##### 4. Deployment and Distribution:
     - Save the Docker container image on Docker Hub to serve as a centralized repository for the application.
    - Version the container image to track changes and ensure consistency across deployments.
     - Document the deployment process and provide instructions for running the containerized application.

### Expected Deliverables:
 - Machine learning model scripts for training and evaluation.
 - FastAPI application code with endpoints for making predictions.
 - Dockerfile for containerizing the FastAPI application.
 - Docker container image pushed to Docker Hub for distribution.

### Project Outcome:
 The successful completion of this project will result in a robust and scalable Sepsis Detection API that can be easily deployed in healthcare environments. The API will provide healthcare professionals with a valuable tool for early detection and management of sepsis, ultimately improving patient outcomes and saving lives.

 ### Links to medium article and docker image

  | Docker Image               | [nyams254/sep-pred-api](https://hub.docker.com/repository/docker/nyams254/sep-pred-api) |
 |---------------------------|---------------------------------------------------------------------------------------|
 | Article                   | [Building a FastAPI for Sepsis Prediction](https://medium.com/@nyamburam12/title-building-a-fastapi-for-sepsis-prediction-3bc0f7f89b70) |

 ## Author 

 <b> Monica Nyambura.

