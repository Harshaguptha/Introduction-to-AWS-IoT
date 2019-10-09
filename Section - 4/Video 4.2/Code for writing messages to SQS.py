import boto3

access_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
region ="xx-xxxx-x"
queue_url = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def post_message(client, message_body, url):
	response = client.send_message(QueueUrl = url, MessageBody= message_body)

def lambda_handler(event, context):
    client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
    x = event['temperature']
    if x > 25:
        post_message(client, 'on', queue_url)
        message = "on"
    elif x <= 25:
        post_message(client, 'off', queue_url)
        message = "off"
