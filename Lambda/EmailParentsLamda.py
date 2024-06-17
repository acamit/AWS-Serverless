import json
import urllib.parse
import boto3
from botocore.exceptions import ClientError


import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

print('Loading function')

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    print(f"Received context: {context}")
    application_name = os.environ["application_name"]
    environment_name = os.environ["environment_name"]
    api_key=get_api_key()
    print(api_key)
    # send_email(api_key)

def send_email(api_key):
    sg = sendgrid.SendGridAPIClient(api_key=api_key)
    from_email = Email("amit.chawla02@nagarro.com", "Amit Chawla")  # Change to your verified sender
    to_email = To("amit.chawla02@nagarro.com", "Amit Chawla")  # Change to your recipient
    reply_to = To("amit.chawla02@nagarro.com", "Amit Chawla")
    subject = "Upcoming onsite workshop"
    content = Content("text/plain", "Hi Everyone,\nAs discussed over the call, we will be conducting an onsite workshop with the clien from July 3, 2024 - July 5,2024. Workshop will be conducted in Gurgaon Plot 13 office. Further detailed agenda will be shared as finalized. All the colleagues will be required to be in office during the visit. Colleagues must be in office by 12 pm Noon on July 3, 2024. Neccessary arrangements for accommodation will be made for collegaes living more than 50Km from the office(as per the existing HR records).\n\nThanks and Regards,\nAmit Chawla")
    mail = Mail(from_email, to_email, subject, content, reply_to)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

def get_api_key(application_name, environment_name):
    secret_name = f"{application_name}-config/{environment_name}/global"
    try:
        secrets_manager = boto3.client('secretsmanager')
        global_secret = secrets_manager.get_secret_value(SecretId=secret_name)
        configuration= json.loads(global_secret["SecretString"])
        return configuration["SendGrid/SendGridApiKey"]
    except ClientError as e:
        print("Unable to load secrets")
        raise e
    
lambda_handler(None, None)