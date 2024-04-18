# Affinipay Application QA Assignment

### Description
The following is the repo I created as part of the application to Affinipay as QA Automation engineer. It implements the test cases for testing the API that was provided in the instructions

It was implemented using python and Playwright


### How to Run

After cloning the repository run the following commands for initializing a Virtual environment and installing the dependencies

`virtualenv venv`

`source venv/bin/activate (for Unix systems)`

or

`. venv/Scripts/activate (for Windows Systems)`

`pip install -r requirements.txt`

Once all dependencies are installed you can simply run the command

`pytest`

This will run all tests

### Project structure:
- src - folder that contains all the code
  - tests - Contains the test implementation
  - endpoints - contains the Methods for the endpoints
  - utils - contains some utils methods for asserting
  - fixtures - Contains the data structures required for the tests