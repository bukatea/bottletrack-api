import json
import os

from libs import dynamodb
from libs.handler import makeHandler

def main(event, context):
  def handlerFunc(event, context):
    key = {
      'userId': {
        'S': "123"
      },
      'bottleName': {
        'S': event['pathParameters']['name']
      }
    }
    response = dynamodb.get(TableName=os.getenv('tableName'), Key=key)
    if 'Item' not in response:
      raise Exception("Item not found.")

    return response['Item']
    
  return makeHandler(handlerFunc)(event, context)