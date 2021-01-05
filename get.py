import json
import os
from urllib.parse import unquote

from libs import dynamodb
from libs.handler import makeHandler

def main(event, context):
  def handlerFunc(event, context):
    key = {
      'userId': {
        'S': event['requestContext']['identity']['cognitoIdentityId']
      },
      'bottleName': {
        'S': unquote(event['pathParameters']['name'])
      }
    }
    response = dynamodb.get(TableName=os.getenv('tableName'), Key=key)
    if 'Item' not in response:
      raise Exception("Item not found.")

    return response['Item']
    
  return makeHandler(handlerFunc)(event, context)