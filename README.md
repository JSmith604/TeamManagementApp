# TeamMemberManagementApp

A simple team-member management application that allows the user to view, edit, add, and delete team members. Built with Python and Django.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python 3.x.
- You have Git installed on your machine.

## Setting Up the Project

To set up the project on your local machine, follow these steps:

### Clone the Repository

git clone [Your Repository URL]
cd [Your Repository Name]

### Set Up the Virtual Environment

# Install virtualenv if it's not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

### Environment Variables

1. Create a `.env` file in the project root (same directory as `manage.py`).
2. Generate a Django secret key. Use the Python shell:

    from django.core.management.utils import get_random_secret_key
    print(get_random_secret_key())

3. Add the generated secret key to the `.env` file:

    DJANGO_SECRET_KEY=your_generated_secret_key

### Database Migrations

python manage.py migrate

### Running the Server

python manage.py runserver

Navigate to `http://localhost:8000` in your browser to view the application.

## Running Tests

python manage.py test

## Built With

- Django 5.0 - The web framework used.
- SQLite - The database system.
- Python 3.x - Programming language.
