import boto3
client = boto3.client('ec2','us-east-1')
custom_filter=[{'Name':'tag:Team','Values':['myteam']}]
response = client.describe_instances(Filters=custom_filter)

def stop(event,context):
    instances = []
    for doc in response['Reservations']:
        instance = doc['Instances'][0]
        instances.append(instance['InstanceId'])

    for inst in instances:
        print('Stopping instance ',inst)
        client.stop_instances(InstanceIds=[inst])
