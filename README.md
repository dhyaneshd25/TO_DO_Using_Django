1. Prerequisites
Before you begin, ensure that you have the following software installed:

Python 3.12 or higher
pip (Python package manager)
Chrome browser
ChromeDriver compatible with your Chrome version
Python Dependencies:
You will need to install the required Python dependencies for this project. They are listed in the requirements.txt file.

To install dependencies, use the following command:

bash
Copy code
pip install -r requirements.txt
2. Setting Up the Environment
1. Clone the Repository:
bash
Copy code
git clone <repository-url>
cd <project-directory>
2. Set Up the Database:
Run the following Django commands to set up your database:

bash
Copy code
python manage.py migrate
This will create the necessary tables in your database.

3. Install ChromeDriver:
You will need to download and install ChromeDriver to enable Selenium-based testing. You can download it from here based on your Chrome version. Alternatively, you can use webdriver_manager to automatically handle ChromeDriver installation during testing.

3. Running the Application
1. Run the Development Server:
To start the Django development server, use the following command:

bash
Copy code
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

2. Access the Application:
Open your browser and navigate to http://127.0.0.1:8000/ to see your To-Do List application in action.

