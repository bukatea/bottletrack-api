import json
import os

from libs import dynamodb
from libs.handler import makeHandler

def main(event, context):
  def handlerFunc(event, context):
    response = dynamodb.query(
      TableName=os.getenv('tableName'),
      KeyConditionExpression="userId = :userId",
      ExpressionAttributeValues={
        ':userId': {
          'S': "123"
        }
      }
    )

    return response['Items']
    
  return makeHandler(handlerFunc)(event, context)