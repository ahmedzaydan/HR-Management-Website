# Human Resources Website

This is a Human Resources website project with the following functionalities:

## Functionalities

1. **Add Employee**: Users can add a new employee to the system. The employee data should include the following details: id, name, email, address, phone number, gender, marital status, number of available vacation days, number of actual approved vacation days, salary, and date of birth.

2. **Update Employee**: Users can update the data of an existing employee.

3. **Delete Employee**: Users can delete an existing employee's data. A confirmation dialogue will be displayed before the deletion occurs.

4. **Search Employee**: Users can search for an employee by name in the search screen. The search results will display employees with similar names in a table format.

5. **Submit Vacation Form**: After searching for an employee, users can select a specific employee and submit a vacation form. The vacation form should include the following details: from date, to date, reason, and status (which will be initially set as "submitted"). The chosen employee's ID will also be associated with the vacation form.

6. **Review Submitted Vacations**: Users can review all "submitted" vacations of different employees. They will have the ability to approve or reject the submitted vacation requests. Each vacation request will be listed with buttons for approval and rejection.

7. **Approve or Reject Vacations**: If the user clicks on the "Approve" button, the vacation will be marked as approved. The employee's actual number of vacation days will be incremented, the available number of vacation days will be decremented, and the vacation will be removed from the submitted vacations page. If the user clicks on the "Reject" button, the vacation will be marked as rejected and removed from the submitted vacations page.

8. **Navigation Bar and Home Page**: The website will have a well-designed navigation bar to easily navigate through all the pages. It will also include a home page.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/ahmedzaydan/HR-Management-Website.git`

2. Install Python: Make sure you have Python installed on your machine. You can download Python from the official website and follow the installation instructions for your operating system.

3. Install Django framework: Open your command prompt or terminal and navigate to the project directory. Run the following command to install Django: `pip install django`

4. Install npm: If you don't have npm installed, you can download and install it from the official website.

5. Activate the virtual environment: In your command prompt or terminal, navigate to the "Framework" directory inside the project. Activate the virtual environment by running the appropriate command for your operating system. For example, on Windows, run `scripts\activate`.

6. Change directory: Navigate to the "Website" directory inside the project by running `cd Website`.

7. Run the server: Start the Django development server by running the following command: `python manage.py runserver`

   This will start the server and display the URL where you can access the HR Management Website in your browser.

   ```
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CTRL-BREAK.
   ```

8. Access the website: Open your web browser and visit the URL provided by the Django development server (e.g., http://127.0.0.1:8000/).

   You should now be able to interact with the HR Management Website locally on your machine.

## Technologies Used

- Front-end: HTML, CSS, JavaScript, AJAX
- Back-end: Django
- Database: SQLite

## Contact
If you have any questions or suggestions, please feel free to contact us at:
[ahmedzidanesyrian@gmail.com](mailto:ahmedzidanesyrian@gmail.com),
[davidnael824@gmail.com](mailto:davidnael824@gmail.com)
