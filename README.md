# Coding-Challenge-CRM

# Project Overview
This project is a CRM (Customer Relationship Management) system written in Django Python. The purpose of the project is to track employees.

# Technologies Used
- Django
- Python
- Docker
- SQLite
# How to Run the Project
There are two ways to run the project: with Docker and without Docker.

#### Running the Project with Docker
To run the project with Docker, follow these steps:

- Clone the project repository [https://github.com/10are/Coding-Challenge-CRM.git] to your local machine."

Open a terminal and navigate to the project directory.

Run the following command to build the Docker image:

- `docker compose build`
- `docker compose up`

Access the application by navigating to http://localhost:8000 in your web browser.
#### Running the Project without Docker
To run the project without Docker, follow these steps:

- Clone the project repository [https://github.com/10are/Coding-Challenge-CRM.git] to your local machine."

Open a terminal and navigate to the project directory.

Run the following command to install the project dependencies:

- `pip install Django`
- `pip install -r requirements.txt`
- `python manage.py createsuperuser`  [for the create super user]

Run the following command to perform database migrations:

- `python manage.py makemigrations`
- `python manage.py migrate`

Run the following command to start the application:

- `python manage.py runserver`
Access the application by navigating to http://localhost:8000 in your web browser.


