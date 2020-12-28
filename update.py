import json
import os

from libs import dynamodb
from libs.handler import makeHandler

def prepareUpdateParams(data, keys):
  changed = []
  expressionAttributeValues = {}
  for key in keys:
    if data.get(key['name']):
      changed.append(key)
      expressionAttributeValues[':' + key['name']] = {
        key['type']: data[key['name']]
      }

  return (
    "{}{}".format("SET " if changed else "", ', '.join("{} = {}".format(item['name'], ':' + item['name']) for item in changed)),
    expressionAttributeValues
  )

def main(event, context):
  def handlerFunc(event, context):
    data = json.loads(event['body'])
    key = {
      'userId': {
        'S': event['requestContext']['identity']['cognitoIdentityId']
      },
      'bottleName': {
        'S': event['pathParameters']['name']
      }
    }
    expr, values = prepareUpdateParams(
      data,
      [
        {
          'name': 'BD_ADDR',
          'type': 'S'
        }
      ]
    )
    if expr != "":
      dynamodb.update(
        TableName=os.getenv('tableName'),
        Key=key,
        UpdateExpression=expr,
        ExpressionAttributeValues=values,
        ReturnValues="ALL_NEW"
      )

    return {
      'status': True
    }
    
  return makeHandler(handlerFunc)(event, context)