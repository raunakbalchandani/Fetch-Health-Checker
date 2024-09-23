# Fetch-Health-Checker

This project implements a Python program to monitor the health of a set of HTTP endpoints defined in a YAML configuration file. It periodically checks the availability of these endpoints and logs the cumulative availability percentage of each domain after each test 

# Table of Contents

1. [Features](#Features)
2. [Pre-Requisites](#Pre-Requisites)
3. [Installation and Running the code](#Installation-and-Running-the-code)
4. [Usage Example](#Usage-Example)
5. [Sample YAML Configuration](#Sample-YAML-Configuration)
6. [Explaination of Availability Calculation](#Explanation-of-Availability-Calculation)
7. [Troubleshooting](#Troubleshooting)
8. [Future Scope](#Future-Scope)
9. [Contributing](#Contributing)
10. [License](#License)


# Features

1. Reads endpoints from a YAML configuration file.
2. Supports HTTP GET and POST methods with customizable headers and body.
3. Checks the availability of each endpoint every 15 seconds.
4. Considers an endpoint UP if:
5. The HTTP status code is between 200 and 299.
6. The response time is less than 500 ms.
7. Logs the cumulative availability percentage of each domain after each test cycle.
8. Continues running until manually stopped.

# Pre-Requisites

1. Python 3.7+: This project is written in Python and requires Python version 3.7 or later.
 - Download Python for your platform (Windows, macOS, Linux).
 - Make sure Python is added to your system’s PATH during installation.

2. pip: Python's package installer. It typically comes pre-installed with Python, but you can install or upgrade it by running:
   ```
   bash python -m ensurepip --upgrade
   
# Installation and Running the code

1. Clone the repository to your local machine, run the following commands one by one in the terminal:
   ```git clone <repository-url>```
   ```cd <repository-directory>```

  

2. Create a virtual environment (optional but recommended to avoid dependency conflicts):

      ```python -m venv venv```

3. To activate the virtual environment (depending on the OS):
   
   Windows: ```venv\Scripts\activate```
   
   MacOS:   ``` bash source venv/bin/activate```

4. Install Dependencies: The project relies on the requests and PyYAML Python libraries. All the required libraries are compiled in the requirements.txt file, available in the repository. Install them using pip:

   Command: ```pip install -r requirements.txt```

5. Once you have installed the dependencies, you can run the health checker program by providing the path to your YAML configuration file as an argument:

    Run the following command: ```python fetchtest.py /path/to/your/config.yaml```

    Replace "/path/to/your/config.yaml with the path where the yaml file is stored in your local machine

6. Once the command is executed, the program will start checking the health of each endpoint every 15 seconds, logging the availability percentage of each domain to the console

7. The program runs continuously and will perform health checks until manually interrupted. To stop it, simply press CTRL+C (for windows)  or (Control) ^+C (for mac) in the terminal.

# Usage Example

Here’s an example output of the website availability logs:

    google.com has 75% availability
    github.com has 100% availability
    fakewebsite123.com has 0% availability
    jsonplaceholder.typicode.com has 50% availability

# Sample YAML Configuration

The YAML configuration file defines the endpoints that the program will monitor. Here’s an example ```configexample.yaml``` file

```
- name: Google Home Page
  url: https://www.google.com/
  method: GET
  headers: 
    user-agent: health-monitor

- name: GitHub Home Page
  url: https://www.github.com/
  method: GET
  headers: 
    user-agent: health-monitor

- name: Example POST Request
  url: https://jsonplaceholder.typicode.com/posts
  method: POST
  headers: 
    content-type: application/json
    user-agent: health-monitor
  body: '{"title": "foo", "body": "bar", "userId": 1}'

- name: Non-existent Site
  url: https://www.fakewebsite123456.com/
  method: GET
  headers: 
    user-agent: health-monitor
```


The fields in the YAML file:

- name: A descriptive name for the endpoint.
- url: The HTTP or HTTPS URL of the endpoint.
- method: The HTTP method to use (GET or POST). Defaults to GET if omitted.
- headers: Optional HTTP headers.
- body: Optional request body for POST requests.

# Explanation of Availability Calculation

The program considers an endpoint UP if:

- The HTTP status code is between 200 and 299.
- The response time is less than 500 milliseconds.
- The availability percentage for each domain is calculated as:

Availability Percentage = 100 x (Total UP Requests/Total requests (UP + DOWN))

After each 15-second test cycle, the availability percentage is logged to the console. The percentage is calculated cumulatively, meaning it takes into account all requests made to the domain since the program started running

# Troubleshooting

- Missing Dependencies: If you get an error like ModuleNotFoundError: No module named 'requests' or No module named 'yaml', it means the required dependencies haven’t been installed. Run the following command:
```pip install -r requirements.txt```

- YAML Parsing Issues: Ensure your configuration file is correctly formatted as YAML. A small syntax error could prevent the program from parsing the file. Use a YAML linter if needed

# Future Scope

In the future, to enhance monitoring and alerting for this health checker, we can integrate with AWS CloudWatch for real-time observability and automated alerts.

1. CloudWatch Logs Integration
   - Use AWS CloudWatch Logs to send availability data for long-term monitoring.
   - Logs can be pushed to CloudWatch using the boto3 SDK.
   - This allows for centralized log storage and easy querying of availability data.

2. Setting Up CloudWatch Alarms
   - We can configure CloudWatch Alarms to trigger notifications when domain availability falls below a certain threshold (e.g., 90%)
   - Using AWS SNS (Simple Notification Service) to send alerts via email or SMS when availability drops
  
3. Real-time Dashboards
   - Build CloudWatch Dashboards to visualize domain health and availability trends in real-time.
   - This helps track uptime and provides insights into performance issues over time.

By leveraging AWS CloudWatch, we can set up a fully automated monitoring and alerting system, ensuring high reliability and proactive incident management.

# Contributing

Feel free to fork this repository and make pull requests. Contributions to improve the codebase and add new features are welcome. Please ensure that your contributions adhere to Python best practices.

# License

This project is licensed under the MIT License. See the LICENSE file for more details




  



