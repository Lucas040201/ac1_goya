import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

tableMensagens = dynamodb.Table('Mensagens')

def lambda_handler(event, context):
    remetente = str(event['from'])
    destinatario = str(event['to'])

    try:
        response = tableMensagens.query(
            KeyConditionExpression=Key('destinatario').eq(destinatario))

        for x in response['Items']:
            if x['remetente'] == remetente:
                return {
                    'statusCode': 200,
                    'body': json.dumps(x['body'])
                }

    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar recuperar mensagens')
        }