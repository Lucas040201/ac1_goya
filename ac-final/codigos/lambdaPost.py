import json
from datetime import datetime
import urllib.parse
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

tableMensagens = dynamodb.Table('Mensagens')

s = boto3.client('s3')


def lambda_handler(event, context):
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    remetente = str(event['from'])
    destinatario = str(event['to'])
    mensagem = str(event['msg'])

    try:
        response = tableMensagens.query(
            KeyConditionExpression=Key('destinatario').eq(destinatario))

        body = [
            {
                'data_hora': (datetime.now()).strftime("%Y-%m-%d %H:%M:%S"),
                'msg': mensagem
            }
        ]

        for x in response['Items']:
            if x['remetente'] == remetente:
                body.extend(x['body'])
                break

        tableMensagens.put_item(
            Item={
                'destinatario': destinatario,
                'remetente': remetente,
                'body': body
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Mensagem de '
                               + remetente
                               + ' para '
                               + destinatario
                               + ' inserida no Banco de Dados')
        }

    except:
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
