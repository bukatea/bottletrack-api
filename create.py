import json
import os
import time

from libs import dynamodb
from libs.handler import makeHandler

def main(event, context):
  def handlerFunc(event, context):
    data = json.loads(event['body'])
    item = {
      'userId': {
        'S': "123"
      },
      'bottleName': {
        'S': data['bottleName']
      },
      'BD_ADDR': {
        'S': data['BD_ADDR']
      },
      'createdAt': {
        'N': str(time.time())
      }
    }
    dynamodb.put(TableName=os.getenv('tableName'), Item=item)

    return item
    
  return makeHandler(handlerFunc)(event, context)