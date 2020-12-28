import json

def makeHandler(lambdaFunc):
  def handler(event, context):
    try:
      body = lambdaFunc(event, context)
      statusCode = 200
    except Exception as e:
      body = {
        'error': str(e)
      }
      statusCode = 500

    return {
      'statusCode': statusCode,
      'body': json.dumps(body),
      'headers': {
        'Access-Control-Allow-Origin': "*",
        'Access-Control-Allow-Credentials': True,
      } 
    }

  return handler