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
    dynamodb.delete(TableName=os.getenv('tableName'), Key=key)

    return {
      'status': True
    }
    
  return makeHandler(handlerFunc)(event, context)