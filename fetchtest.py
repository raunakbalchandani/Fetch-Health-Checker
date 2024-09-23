import yaml
import argparse

#Loading the endpoints yaml file

def load_endpoints(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to parse input argument (YAML file path)
def parse_args():
    parser = argparse.ArgumentParser(description='HTTP Endpoints Health Checker')
    parser.add_argument('config', type=str, help='Path to YAML configuration file')
    return parser.parse_args()

# Fuction to send HTTP requests

import requests
import time

def check_health(endpoint):
    try:
        response = requests.request(
            method=endpoint.get('method', 'GET'),
            url=endpoint['url'],
            headers=endpoint.get('headers', {}),
            data=endpoint.get('body', None)
        )
        response_time = response.elapsed.total_seconds() * 1000  # Convert to milliseconds
        if 200 <= response.status_code < 300 and response_time < 500:
            return 'UP'
        else:
            return 'DOWN'
    except requests.exceptions.RequestException:
        return 'DOWN'


#Tracking Availability

domain_stats = {}

def update_stats(domain, status):
    if domain not in domain_stats:
        domain_stats[domain] = {'up': 0, 'total': 0}
    domain_stats[domain]['total'] += 1
    if status == 'UP':
        domain_stats[domain]['up'] += 1

def get_availability(domain):
    stats = domain_stats[domain]
    return round(100 * stats['up'] / stats['total'])  # Round to the nearest whole percentage

#Main Logic

import time

def extract_domain(url):
    return url.split('/')[2]  # Extracts the domain name from the URL

def run_health_checks(endpoints):
    while True:
        # Perform health check for each endpoint
        for endpoint in endpoints:
            domain = extract_domain(endpoint['url'])
            status = check_health(endpoint)
            update_stats(domain, status)
        
        # Log availability percentage for each domain
        for domain in domain_stats:
            print(f"{domain} has {get_availability(domain)}% availability")
        
        # Wait for 15 seconds before the next round
        time.sleep(15)

if __name__ == '__main__':
    args = parse_args()  # Parse the file path argument
    endpoints = load_endpoints(args.config)  # Load the YAML configuration
    run_health_checks(endpoints)  # Start the health check loop



