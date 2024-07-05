import smtplib
import requests
import json
import time
import yaml
import logging
import re

from utils import get_user_agent, get_carriers, get_carrier_gateway

 # Regex to validate email address
email_validate_pattern = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$" 

def fetch_class_info(class_num):
    """
    Fetch the class information for a given class number.

    Args:
        class_num (str): The class number to fetch information for.

    Returns:
        int: The number of available seats in the class.
    """
    url = f"https://eadvs-cscc-catalog-api.apps.asu.edu/catalog-microservices/api/v1/search/classes?&refine=Y&advanced=true&campusOrOnlineSelection=A&classNbr={class_num}&honors=F&promod=F&searchType=all&term=2247"

    headers = {
        "User-Agent": get_user_agent(),
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://catalog.apps.asu.edu/",
        "authorization": "Bearer null",
        "Origin": "https://catalog.apps.asu.edu",
        "DNT": "1",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "TE": "trailers"
    }

    response = requests.get(url, headers=headers)
    class_results = json.loads(response.text)
    seat_info = class_results['classes'][0]['seatInfo']
    return seat_info['ENRL_CAP'] - seat_info['ENRL_TOT']

def input_data():
    """
    Read and validate input data from the config.json file.

    Returns:
        list: A list containing class number, phone number, carrier, and email ID.

    Raises:
        ValueError: If the input data is not valid.
    """
    with open('config.json') as f:
        data = json.load(f)
        classnum = data['classnum']
        phone_number = data['phone_number']
        carrier = data['carrier']
        email_id = data['email_id']

        if len(classnum) != 5 or not classnum.isdigit():
            raise ValueError('Class number should be a 5-digit code')

        if len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError('Phone number should be a 10-digit code')

        if carrier not in get_carriers():
            raise ValueError('Carrier should be one of the following: {}'.format(get_carriers()))

       
        if not re.match(email_validate_pattern, email_id):
            raise ValueError('Invalid email address')

        return [classnum, phone_number, carrier, email_id]

def get_credentials(filepath):
    """
    Get email credentials from a YAML file.

    Args:
        filepath (str): The path to the credentials YAML file.

    Returns:
        tuple: A tuple containing the email address and password.

    Raises:
        Exception: If there is an error loading the credentials file.
    """
    try:
        with open(filepath, 'r') as file:
            credentials = yaml.safe_load(file)
            user = credentials['user']
            password = credentials['password']

            if not re.match(email_validate_pattern, user):
                raise ValueError('Invalid email address')

            return user, password
    except (yaml.YAMLError, FileNotFoundError) as e:
        logging.error("Failed to load credentials: {}".format(e))
        raise

def send_mail(email_id, class_num):
    """
    Send an email notification that a class is open.

    Args:
        email_id (str): The recipient's email address.
        class_num (str): The class number to include in the email.

    Raises:
        Exception: If there is an error sending the email.
    """
    try:
        user, password = get_credentials("credentials.yaml")
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(user, password)
            message = f"Subject: Class {class_num} is open\n\nClass {class_num} should be added to your schedule. Visit MyASU to verify."
            server.sendmail(user, email_id, message)
        print("Email sent successfully")
    except Exception as error:
        print(f"Error, email was not sent: {error}")

def main():
    """
    Main function to check class availability and send notifications.
    """
    data = input_data()

    while True:
        seats_left = fetch_class_info(data[0])
        if seats_left > 0:
            print(f'Seats remaining: {seats_left}')
            send_mail(data[3], data[0])
            send_mail(f"{data[1]}@{get_carrier_gateway(data[2])}", data[0])
            break
        time.sleep(5)

if __name__ == "__main__":
    main()
