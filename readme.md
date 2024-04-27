## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
  - [Register User](#register-user)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Amrit02102004/Munsow_Task1.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables (if any).

## Usage

1. Run the Flask application:

   ```bash
   flask run
   ```

2. Access the API endpoints through `http://localhost:5000` (or the appropriate address).

## Routes

### Register User

Registers a new user.

- **URL**

  `/api/register`

- **Method**

  `POST`

- **Data Params**

  - `username`: String (required)
  - `email`: String (required)
  - `password`: String (required)

- **Success Response**

  - **Code:** 201 CREATED
  - **Content:**
    ```json
    {
        "message": "User registered successfully",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

- **Error Responses**

  - **Code:** 400 BAD REQUEST
  - **Content:**
    ```json
    {
        "error": "Missing required fields. Try again with correct fields!"
    }
    ```
    OR
    ```json
    {
        "error": "Password must be at least 8 characters long"
    }
    ```

- **Images**
Sample request body images:
  ![1.png](PostMan Result/1.png)
  ![2.png](PostMan Result/2.png)
  ![3.png](PostMan Result/3.png)
  ![4.png](PostMan Result/4.png)
  ![5.png](PostMan Result/5.png)
  ![6.png](PostMan Result/6.png)
  ![7.png](PostMan Result/7.png)
  ![8.png](PostMan Result/8.png)
  ![9.png](PostMan Result/9.png)
  ![10.png](PostMan Result/10.png)
