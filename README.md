# InstaSecret

InstaSecret is a simple Flask-based web application that allows users to create and share secrets securely. Each secret can only be accessed once, ensuring privacy and security.

## Features

- Create a secret and generate a unique link to access it.
- Access the secret using the unique link.
- Secrets are marked as "used" after being accessed once, preventing reuse.

## Prerequisites

- Python 3.8 or higher installed on your system.
- pip (Python package installer) to manage dependencies.
- A virtual environment tool like `venv` or `virtualenv` (optional but recommended).
- Basic knowledge of Flask and Python.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd insta-secret```

2. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

# Usage
1. Activate your virtual environment (if using one):
    ```bash
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate     # On Windows
    ```

2. Run the Flask application:
    ```bash
    flask run
    ```

3. Open your web browser and navigate to:
    ```
    http://127.0.0.1:5000
    ```

4. Follow the on-screen instructions to create and share secrets securely.

