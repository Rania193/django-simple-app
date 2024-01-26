# Django Blog App

## Overview

This Django Blog App is a web application that allows users to create, view, and manage blog posts. It comes with features like user registration, login/logout functionality, and a user profile page.

## Features

- **User Authentication:**
  - Users can register for an account and log in to create, edit, and delete their blog posts.

- **Blog Post Management:**
  - Create, edit, and delete blog posts.
  - View a list of all blog posts on the home page.

- **User Profile:**
  - Each user has a profile page displaying their username.
  - Users can access their profile page and update their information.

- **Login/Logout System:**
  - Secure user authentication with login and logout functionality.
  - Restricted access to certain routes based on user authentication status.

## Setup Instructions

To run this Django Blog App locally, follow these steps:

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/django-blog-app.git
   cd django-blog-app
   ```
2. **Create Virtual Environment:**

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies:**

```
pip install -r requirements.txt
```
4. **Apply Migrations:**

```
python manage.py migrate
```
5. **Create Superuser (Admin):**

```
python manage.py createsuperuser
```
6. **Run Development Server:**
```
python manage.py runserver
```
7. **Access the Application:**

Open your browser and go to http://127.0.0.1:8000/

8. **Access Admin Panel:**

Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.
