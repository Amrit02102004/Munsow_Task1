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

  ![1](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/5123a3b9-c03d-4003-b2d1-1897e2a14d40)
  ![2](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/a93894ff-b298-4344-948e-800e5241976f)
  ![3](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/1cd6c8fd-1427-401e-af83-3303574a2812)
  ![4](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/6a168971-c245-40f6-9a93-ffcb6c84f6fb)
  ![5](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/df021b27-6bbd-4038-b9a4-1dcee9b6e066)
  ![6](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/874ee57d-9ec6-4014-b747-22fa20085b47)
  ![7](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/06048117-16a5-416a-8fef-7c5323135265)
  ![8](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/029f747a-22b0-40fb-9b2e-e949507f7aad)
  ![9](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/66785af3-ec72-4559-952f-8f60d8342d64)
  ![10](https://github.com/Amrit02102004/Munsow_Task1/assets/114827768/5085e5eb-eed4-4d97-8feb-39eab68ac1a5)


