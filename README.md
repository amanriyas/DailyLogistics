# DailyLogistics

DailyLogistics is a web application designed to help firms manage employee attendance, daily/monthly expenses, and other logistics. The application is built using Django and Django REST Framework, and it uses PostgreSQL as the database.

## Project Structure

The project has the following structure:

- **DailyLogistics/attendance/**: Contains the Django app for managing attendance, including models, views, serializers, and URLs.

- **DailyLogistics/paramount/**: Contains the main Django project settings and URLs.

- **docker-compose.yaml**: Docker Compose configuration file for setting up the application and its dependencies.

- **dockerfile**: Dockerfile for building the backend service.

- **requirements.txt**: List of Python dependencies for the project.

## How to Run the Application

### Prerequisites

- Docker and Docker Compose installed on your machine.
- A `.env` file in the `DailyLogistics` directory with the following environment variables:

DB_USER=your_db_user DB_PASSWORD=your_db_password DB_NAME=your_db_name SECRET_KEY=your_django_secret_key

### Running the Application

1. **Build and Start the Containers**:
 Navigate to the `DailyLogistics` directory and run the following command to build and start the containers:
 ```sh

 docker-compose up --build

Access the Application: Once the containers are up and running, you can access the Django application at http://localhost:8000.

Stopping the Containers: To stop the containers, run:

docker-compose down

### Viewing the PostgreSQL Database with pgAdmin

To visually manage and interact with the PostgreSQL database, we have included a pgAdmin container in the `docker-compose.yaml` file. pgAdmin is a popular open-source administration and development platform for PostgreSQL.

The `docker-compose.yaml` file includes the following configuration for the pgAdmin container:

### Accessing pgAdmin

1. **Start the Containers**:
     Ensure that the containers are running by navigating to the `DailyLogistics` directory and executing:
     ```sh
     docker-compose up --build
     ```

2. **Access pgAdmin**:
     Open your web browser and go to `http://localhost:5050`. Log in with the credentials mentioned in your .env file:
     - **Email**: `admin@example.com` 
     - **Password**: `admin_examplepassword`

3. **Add a New Server**:
     - Click on "Add New Server".
     - In the "General" tab, enter a name for the server.
     - In the "Connection" tab, enter the following details:
         - **Host name/address**: `db`  # use the name given for your database service in the docker-compose file.
         - **Port**: `5432`
         - **Username**: Your PostgreSQL username (from the `.env` file).
         - **Password**: Your PostgreSQL password (from the `.env` file).

You can now use pgAdmin to manage your PostgreSQL database visually.


GitHub Actions Workflow
The repository includes a GitHub Actions workflow defined in main.yaml. This workflow is triggered on pushes and pull requests to the main branch. It performs the following steps:

Checkout Code: Uses the actions/checkout@v2 action to checkout the repository code.
Set up Docker Compose: Installs Docker Compose on the runner.
Build and Start Containers: Builds and starts the Docker containers using docker-compose.
Cleanup: Stops and removes the Docker containers.
The workflow ensures that the application can be built and run successfully in a Docker environment.

Application Endpoints
The application provides the following endpoints:

Employee Management:

GET /attendance/all-employees/: List all employees.
POST /attendance/add-employee/: Add a new employee.
PUT /attendance/edit-employee/<int:pk>/: Edit an existing employee.
DELETE /attendance/delete-employee/<int:pk>/: Delete an employee.
Role Management:

GET /attendance/all-roles/: List all roles.
POST /attendance/add-role/: Add a new role.
PUT /attendance/edit-role/<int:pk>/: Edit an existing role.
DELETE /attendance/delete-role/<int:pk>/: Delete a role.
Site Management:

GET /attendance/all-sites/: List all sites.
POST /attendance/add-site/: Add a new site.
PUT /attendance/edit-site/<int:pk>/: Edit an existing site.
DELETE /attendance/delete-site/<int:pk>/: Delete a site.
Attendance Management:

GET /attendance/site-attendance/: List all site attendance records.
POST /attendance/add-attendance/: Add a new site attendance record.
PUT /attendance/edit-attendance/<int:pk>/: Edit an existing site attendance record.