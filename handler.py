import json
import logging
import boto3
import datetime
import dynamo
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)
dynamodb = boto3.client('dynamodb', endpoint_url="http://host.docker.internal:4566")
table_name = os.environ["ITEMS_TABLE"]


def create(event, context):
    logger.info(f'Incoming request is: {event}')

    # Set the default error response
    response = {
        "statusCode": 500,
        "body": "An error occurred while creating item."
    }

    # return response
    item_str = event['body']
    item = json.loads(item_str)
    current_timestamp = datetime.datetime.now().isoformat()
    item['createdAt'] = current_timestamp

    res = dynamodb.put_item(
        TableName=table_name, Item=dynamo.to_item(item))

    # If creation is successful
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = {
            "statusCode": 201,
            "body": "Successfully added item"
        }

    return response


def get(event, context):
    logger.info(f'Incoming request is: {event}')
    # Set the default error response
    response = {
        "statusCode": 500,
        "body": "An error occurred while getting item."
    }

    item_id = event['pathParameters']['itemId']

    item_query = dynamodb.get_item(
        TableName=table_name, Key={'id': {'N': item_id}})

    if 'Item' in item_query:
        item = item_query['Item']
        logger.info(f'Item is: {item}')
        response = {
            "statusCode": 200,
            "body": json.dumps(dynamo.to_dict(item))
        }

    return response


def all(event, context):
    # Set the default error response
    response = {
        "statusCode": 500,
        "body": "An error occurred while getting all items."
    }

    scan_result = dynamodb.scan(TableName=table_name)['Items']

    items = []

    for item in scan_result:
        items.append(dynamo.to_dict(item))

    response = {
        "statusCode": 200,
        "body": json.dumps(items)
    }

    return response


def update(event, context):
    logger.info(f'Incoming request is: {event}')

    item_id = event['pathParameters']['itemId']

    # Set the default error response
    response = {
        "statusCode": 500,
        "body": f"An error occurred while updating item {item_id}"
    }

    item_str = event['body']

    item = json.loads(item_str)

    # current_timestamp = datetime.datetime.now().isoformat()
    # item['updatedAt'] = current_timestamp

    res = dynamodb.update_item(
        TableName=table_name,
        Key={
            'id': {'N': item_id}
        },
        UpdateExpression="set file_name=:f, media_type=:m, updatedAt=:u",
        ExpressionAttributeValues={
            ':f': dynamo.to_item(item['file_name']),
            ':m': dynamo.to_item(item['media_type']),
            ':u': dynamo.to_item(datetime.datetime.now().isoformat())
        },
        ReturnValues="UPDATED_NEW"
    )

    # If update is successful for item
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = {
            "statusCode": 200,
        }

    return response


def delete(event, context):
    logger.info(f'Incoming request is: {event}')

    item_id = event['pathParameters']['itemId']

    # Set the default error response
    response = {
        "statusCode": 500,
        "body": f"An error occurred while deleting item {item_id}"
    }

    res = dynamodb.delete_item(TableName=table_name, Key={
                               'id': {'N': item_id}})

    # If deletion is successful for item
    if res['ResponseMetadata']['HTTPStatusCode'] == 200:
        response = {
            "statusCode": 204,
            "body": "Successfully deleted"
        }
    return response