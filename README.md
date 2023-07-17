# BugHive Bug Tracker

BugHive is a bug tracker web application built using Django, HTML, and CSS. It provides a user-friendly interface for managing and tracking bugs in software projects. The app includes features such as user registration, authentication, email verification, bug creation, bug listing, bug details, bug updating, and bug deletion. The project is designed to be mobile-friendly and utilizes the Bootstrap framework.

## Table of Contents
* Features
* Installation
* Usage
* Project Structure
  * Root Directory
  * Main App Directory
  * Static Files Directory
  * Templates Directory
* Configuration
* Usage
* Deployment
* License
* Acknowledgements

## Features
1. **User Registration and Authentication:** Users can create an account and login to access the bug tracking functionality.
2. **Mobile Responsive Design:** The app is built using Bootstrap to ensure optimal user experience across different devices.
3. **Main Home Page:** The landing page of the app that provides an overview and directs users to the login or signup page.
4. **Sign up page:** New users can create an account by providing their information and selecting a username and password.
5. **Email Verification:** After signing up, users receive an email with a verification link to activate their account.
6. **Sign in page:** Existing users can log in to access their bug reports and other features.
7. **User home page:** After signing in, users are greeted with a personalized message displaying their name.
8. **Bug list page:** Users can view all the bugs they have reported, including the bug's title, bug priority, and current status.
9. **Individual bug page:** Clicking on a bug in the bug list page takes users to a detailed view of the bug, including additional information and options for updating or deleting the bug.
10. **Update bug page:** Users can modify the details of a bug by filling out an update form. Each bug has a unique update page based on its ID.
11. **Delete bug functionality:** Users can remove a bug from their list by clicking the delete button, which redirects them back to the bug list page with the bug removed.
12. **Bug form page:** Users can fill out a form to report a new bug. The submitted bug will then be displayed in the bug list page.
13. **CRUD functionality:** The application provides Create, Read, Update, and Delete (CRUD) functionality, allowing users to manage their bug reports effectively.

## Installation
1. Clone the repository: `git clone https://github.com/ighitesh/bughive.git`
2. Create a virtual environment: `virtualenv venv`
3. Activate the virtual environment:
   * For Linux/macOS: `source venv/bin/activate`
   * For Windows: `venv\Scripts\activate`
4. Install the required dependencies: `pip install -r requirements.txt`
5. Set up the database: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`
7. Access the BugHive app in your web browser at http://localhost:8000/.

## Usage
1. Sign in for a registered account by clicking on the "Sign In" link on the home page.
2. If the user is not signed up, they have to create an account using hte "Sign Up" link on the "Sign In" page.
3. Check your email for a verification link and click on it to activate your account.
4. Log in with your credentials using the "Sign In" page.
5. Upon successful login, you will be redirected to the user home page, where you will see a personalized welcome message.
6. To report a new bug, click on the "Bug Form" link and fill out the bug details.
7. View all your reported bugs by clicking on the "Bug List" link. You can click on individual bugs to view more details.
8. On the "Bug List" page, you have the option to update or delete the bug.
   * To update a bug, click on the "Update Bug" button and fill out the update form with the desired changes.
   * To delete a bug, click on the "Delete Bug" button, and the bug will be removed from your list.
9. To log out, click on the "Sign Out" link at the top-right corner of the navigation bar.

## Project Structure
The BugHive bug tracker project follows a specific directory structure to organize its files and modules. Here is an overview of the project structure:

* `manage.py`: The command-line utility for managing various aspects of the Django project.
* `db.sqlite3`: The default SQLite database file used for local development and testing.

### Root Directory
* `__init__.py`: An empty file that designates the root directory as a Python package.
* `__pycache__`: A directory that contains compiled Python bytecode files.
* `asgi.py` :The ASGI (Asynchronous Server Gateway Interface) entry point for the project.
* `info.py`: A Python file that may contain project-specific information.
* `settings.py`: The project's main settings file, which includes configurations for the Django project.
* `urls.py`: The URL configuration file that maps URLs to views.
* `urls.py`: The WSGI (Web Server Gateway Interface) entry point for the project.

### Main App Directory
The `main_app` directory contains the core functionality and logic of the BugHive bug tracker.
* `__init__.py`: An empty file that designates the main_app directory as a Python package.
* `__pycache__`: A directory that contains compiled Python bytecode files.
* `admin.py`: The admin configuration file for registering models with the Django admin site.
* `apps.py`: The configuration file for the main app.
* `forms.py`: Contains Django forms for bug-related operations.
* `migrations/`: A directory that stores database migration files.
* `models.py`: Contains Django models representing the bug tracker's data structure.
* `tests.py`: Contains unit tests for the main app.
* `token.py`: Contains token-related functionality.
* `urls.py`: The URL configuration file specific to the main app.
* `views.py`: Contains the views (functions or classes) responsible for handling HTTP requests and returning responses.

### Static Files Directory
The `static/` directory contains static assets used in the BugHive bug tracker.
* `assets/`: A directory that holds all the static assets for the project.
    * `css/`: Contains CSS files used for styling the web pages.
    * `img/`: Contains image files used in the BugHive app.
    * `js/`: Contains JavaScript files for client-side functionality.
    * `vendor/`: A directory that includes third-party libraries and frameworks used in the BugHive app.

### Templates Directory
The `templates/` directory contains HTML templates for the BugHive bug tracker.

* `activation_failed.html` : HTML template for displaying activation failure messages.
* `email_confirmation.html` : HTML template for the email confirmation page.
* `main_app/` : A directory that holds templates specific to the main app.
    * `bug_form.html` : HTML template for the bug creation form.
    * `bug_form_template.html` : HTML template for displaying the bug creation form.
    * `bug_list.html` : HTML template for the bug list page.
    * `bug_list_template.html` : HTML template for displaying the bug list.
    * `bug_solution_template.html` : HTML template for displaying bug solutions.
    * `bug_viewer.html` : HTML template for the individual bug page.
    * `bug_viewer_template.html` : HTML template for displaying individual bug details.
    * `index.html` : HTML template for the main landing page.
    * `signin.html` : HTML template for the user sign-in page.
    * `signup.html` : HTML template for the user sign-up page.
    * `update_bug.html` : HTML template for updating a bug.
    * `update_bug_template.html` : HTML template for displaying the bug update form.
    * `userpage.html` : HTML template for the user home page.

## Configuration
To configure the BugHive bug tracker, follow these steps:
1. **Install Python:** Make sure you have Python installed on your system. You can download and install Python from the official Python website.
2. **Install Dependencies:** Open a terminal or command prompt and navigate to the project's root directory. Run the following command to install the required dependencies: `pip install -r requirements.txt`
3. **Database Configuration:** Open the `settings.py` file located in the root directory. Configure the database settings according to your requirements. By default, the project uses SQLite, which is suitable for local development.
4. **Email Configuration:** In the `info.py` file, configure the email settings to enable email verification and notifications. Specify the SMTP server details, such as the host, port, username, and password.
5. **Static Files:** The BugHive bug tracker uses static files for CSS, JavaScript, and images. By default, these files are served from the `static/` directory. Ensure that your web server is configured to serve static files from this directory.

## Usage
To use the BugHive bug tracker, follow these steps:
1. **Run Migrations:** Apply the database migrations by running the following command in the project's root directory: `python manage.py migrate`
2. **Create a Superuser:** Create a superuser account to access the Django admin site and manage user accounts. Run the following command and follow the prompts: `python manage.py createsuperuser`
3. **Start the Development Server:** Run the following command to start the development server: `python manage.py runserver`
4. **Access the BugHive App:** Open a web browser and navigate to http://localhost:8000 or the appropriate URL where the development server is running. You will see the BugHive app's main landing page. Open a web browser and navigate to http://localhost:8000 or the appropriate URL where the development server is running. You will see the BugHive app's main landing page.
5. **User Registration:** Click on the "Sign Up" link to create a new user account. Fill in the required details, including username, email address, and password. An email confirmation link will be sent to the provided email address.
6. **User Authentication:** Once registered, you can log in using your credentials on the "Sign In" page.
7. **Bug Tracking:** After logging in, you will be directed to your home page, which displays your username. From there, you can create new bugs, view the bug list, update existing bugs, and delete bugs as needed.

## Deployment
To deploy the BugHive bug tracker to a production environment, follow these steps:
1. **Set Up a Production Database:** Configure a production database, such as PostgreSQL or MySQL, in the `settings.py` file. Update the database settings accordingly.
2. **Static Files Configuration:** Configure your web server to serve the static files from the `static/` directory in the project. Ensure that the appropriate directory permissions are set.
3. **Security Considerations:** Implement security measures such as using HTTPS, enabling CSRF protection, and setting strong passwords for user accounts. Consult Django's security documentation for more details.
4. **Environment Variables:** Use environment variables to store sensitive information, such as secret keys, database credentials, and email server details. Update the `settings.py` and `info.py` file to read these values from environment variables.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).

## Acknowledgements
BugHive was developed by me as a personal project. I would like to acknowledge the following resources that helped in building this app:
* Django: https://www.djangoproject.com/
* Bootstrap: https://getbootstrap.com/

Thank you for using BugHive Bug Tracker! I hope it helps you efficiently track and manage bugs in your projects.
