# 9ai Application

Welcome to the 9ai application repository! This application is designed to XYZ. Follow the steps below to set up and run the application on your local machine.

Steps
1. Creating a Virtual Environment and Activating It:
Create a Virtual Environment:
Open your terminal.

Navigate to your project directory (9ai) using the cd command.

Run the following command to create a virtual environment named venv:

python3 -m venv venv

Activate the Virtual Environment:

On macOS/Linux:

* source venv/bin/activate 
On Windows:

* venv\Scripts\activate

2. Installing Required Packages:
With the virtual environment activated, install the required packages using pip:

* pip install uvicorn pymongo fastapi

3. Setting Up Connection:
Navigate to 9ai-config-config.py.
Modify line no.4.
Enter the username and password for your MongoDB database user.

* uri = "mongodb+srv://<user>:<pass>app.7kssw1z.mongodb.net/?retryWrites=true&w=majority&appName=9aiapp"

4. Running the Application:
With the virtual environment activated and MongoDB cluster set up, run the following command to start your application:

* uvicorn main:app --reload
Navigate to http://127.0.0.1:8000/docs to view API documentation.

