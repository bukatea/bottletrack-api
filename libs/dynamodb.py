import boto3

client = boto3.client('dynamodb')

def get(**kwargs):
  return client.get_item(**kwargs)

def put(**kwargs):
  return client.put_item(**kwargs)

def query(**kwargs):
  return client.query(**kwargs)

def update(**kwargs):
  return client.update_item(**kwargs)

def delete(**kwargs):
  return client.delete_item(**kwargs)