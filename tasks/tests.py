from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class ToDoListE2ETests(LiveServerTestCase):

    def setUp(self):
        # Use WebDriverManager to automatically download and set up chromedriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())  # Automatically handles the chromedriver path
        self.driver = webdriver.Chrome(service=service)  # Pass the service to the webdriver

    def tearDown(self):
        if self.driver:
            self.driver.quit()  # Quit the browser after the test is finished

    def test_add_task(self):
        # Open the add task page
        self.driver.get(self.live_server_url + '/add/')
        
        # Find the input elements and send values
        self.driver.find_element(By.NAME, 'title').send_keys('Test Task')
        self.driver.find_element(By.NAME, 'description').send_keys('This is a test task description.')
        self.driver.find_element(By.NAME, 'due_date').send_keys('2024-12-31')  # Set a valid date
        self.driver.find_element(By.TAG_NAME, 'button').click()  # Click the "Add Task" button

        # Wait for the page to reload and check if the task is present in the list
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ul'))
        )

        # Check if the task appears in the task list
        tasks = self.driver.find_elements(By.TAG_NAME, 'li')
        task_titles = [task.text for task in tasks]
        self.assertTrue('Test Task' in task_titles)

    def test_update_task(self):
        # First, add a task
        self.test_add_task()

        # Click the "Edit" link for the task
        edit_button = self.driver.find_element(By.LINK_TEXT, 'Edit')
        edit_button.click()

        # Update the task's title and description
        self.driver.find_element(By.NAME, 'title').clear()  # Clear the old value
        self.driver.find_element(By.NAME, 'title').send_keys('Updated Test Task')
        self.driver.find_element(By.NAME, 'description').clear()
        self.driver.find_element(By.NAME, 'description').send_keys('Updated task description.')
        self.driver.find_element(By.TAG_NAME, 'button').click()  # Submit the updated task

        # Wait for the page to reload and check if the updated task appears
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ul'))
        )

        # Check if the updated task is in the task list
        tasks = self.driver.find_elements(By.TAG_NAME, 'li')
        task_titles = [task.text for task in tasks]
        self.assertTrue('Updated Test Task' in task_titles)

    def test_delete_task(self):
        # First, add a task
        self.test_add_task()

        # Find and click the delete link for the first task
        delete_button = self.driver.find_element(By.LINK_TEXT, 'Delete')
        delete_button.click()

        # Confirm deletion (submit the form)
        self.driver.find_element(By.TAG_NAME, 'button').click()

        # Wait for the page to reload and check if the task is deleted
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ul'))
        )

        # Check if the task is no longer in the list
        tasks = self.driver.find_elements(By.TAG_NAME, 'li')
        task_titles = [task.text for task in tasks]
        self.assertNotIn('Test Task', task_titles)  # Assert that the task is not in the list

    def test_task_list_empty(self):
        # Ensure no tasks exist in the database
        from tasks.models import Task
        Task.objects.all().delete()

        # Visit the task list page
        self.driver.get(self.live_server_url)

        # Wait for the page to load and check for the "No tasks found" message
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'ul'))
        )

        # Check if "No tasks found" is in the page content
        page_source = self.driver.page_source
        self.assertIn("No tasks found.", page_source)

