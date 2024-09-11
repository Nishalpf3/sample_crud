
🌟 Employee Register System 🌟
A web-based Employee Management System developed using Django, allowing users to perform CRUD (Create, Read, Update, Delete) operations for managing employee records.

🎯 Features:
✨ Add Employees: Create new employee records with their full name, employee code, mobile number, and position.
📝 Edit Employees: Update the details of existing employees.
❌ Delete Employees: Remove employee records from the system.
👀 View Employees: Display all employees in a list format with the option to edit or delete.
💻 Technologies Used:
Framework: Django 3.1.1
Frontend: Bootstrap 4, HTML, CSS
Database: SQLite (default)
Programming Language: Python 3.10
Template Tags: Django crispy forms
⚙️ Installation
Follow the steps below to set up the project locally:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/employee-register.git
cd employee-register
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy code
source venv/bin/activate
On Windows:

bash
Copy code
venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run database migrations:

bash
Copy code
python manage.py migrate
Run the development server:

bash
Copy code
python manage.py runserver
Access the application by navigating to:
http://127.0.0.1:8000/employee/ in your browser.

🗂️ Project Structure
bash
Copy code
employee_project/
├── employee_register/
│   ├── migrations/
│   ├── templates/
│   │   └── employee_register/
│   │       ├── base.html
│   │       ├── employee_form.html
│   │       └── employee_list.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── employee_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
🎮 Usage
➕ Add a new employee by clicking on "Add New" in the employee list.
🖊️ Update an employee by clicking on the edit icon next to an employee's name.
🗑️ Delete an employee by clicking on the trash icon next to an employee's name.
📋 View the full list of employees in the table on the main page.
🖼️ Screenshots
Description	Screenshot
Employee List	
Add/Edit Employee Form	
🤝 Contributing
Feel free to contribute to the project by opening a pull request. Here’s how you can contribute:

Fork the project.

Create a feature branch:

bash
Copy code
git checkout -b feature/AmazingFeature
Commit your changes:

bash
Copy code
git commit -m 'Add some AmazingFeature'
Push to the branch:

bash
Copy code
git push origin feature/AmazingFeature
Open a pull request.

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
If you have any questions or suggestions, feel free to reach out to me at nishalpf3@gmail.com.

