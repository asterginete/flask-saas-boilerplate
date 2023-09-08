# flask-saas-boilerplate

This boilerplate provides a starting point for building a Software as a Service (SaaS) application using Flask, Flask-SQLAlchemy, Flask-Login, and SQLite. It includes user authentication, billing, and basic dashboard functionality.

## Features

- **User Authentication**: Register, login, and logout functionality using Flask-Login and Werkzeug.
- **Database**: SQLite integration using Flask-SQLAlchemy for storing user data and subscription details.
- **Billing**: A basic billing dashboard for users to view their subscription and payment details.
- **Templates**: Basic HTML templates using Bootstrap for styling.

## Directory Structure

```
/flask-saas-boilerplate
|-- app/
|   |-- auth/
|   |   |-- templates/
|   |   |   |-- login.html
|   |   |   |-- register.html
|   |   |-- __init__.py
|   |   |-- routes.py
|   |-- billing/
|   |   |-- templates/
|   |   |   |-- billing.html
|   |   |-- __init__.py
|   |   |-- routes.py
|   |-- main/
|   |   |-- templates/
|   |   |   |-- index.html
|   |   |-- __init__.py
|   |   |-- routes.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- models.py
|   |-- static/
|   |-- templates/
|   |-- __init__.py
|-- migrations/
|-- venv/
|-- config.py
|-- run.py
```

## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/asterginete/flask-saas-boilerplate.git
   cd flask-saas-boilerplate
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   - `DATABASE_URL`: Connection string for the database.
   - `SECRET_KEY`: Secret key for Flask.
   - `STRIPE_SECRET_KEY`: Secret key for Stripe integration (if you decide to integrate Stripe).

5. **Initialize the Database**:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application**:
   ```bash
   python run.py
   ```

## Usage

1. **Register**: Navigate to the registration page and create an account.
2. **Login**: Use your credentials to log in.
3. **Dashboard**: Once logged in, you'll be redirected to the dashboard.
4. **Billing**: View and manage your subscription and payment details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
