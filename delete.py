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
    dynamodb.delete(TableName=os.getenv('tableName'), Key=key)

    return {
      'status': True
    }
    
  return makeHandler(handlerFunc)(event, context)