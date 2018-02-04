import boto3
import pytest
import unittest.mock as mock

from ru_alumni import application


application.config.from_object('ru_alumni.config.TestingConfig')

TEST_TABLE_NAME = 'TestUsers'
TEST_ACCOUNT_ID = 101
TEST_EMAIL_ADDRESS = 'alum@rutgers.edu'
TEST_TABLE_ATTRIBUTE_ARGS = {
    'TableName': TEST_TABLE_NAME,
    'KeySchema': [
        {
            'AttributeName': 'account_id',
            'KeyType': 'HASH'
        }
    ],
    'AttributeDefinitions': [
        {
            'AttributeName': 'account_id',
            'AttributeType': 'N'
        }
    ],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
}
TEST_ITEM = {
    'account_id': TEST_ACCOUNT_ID,
    'email_address': TEST_EMAIL_ADDRESS,
    'is_verified': False,
    'is_active': True,
}


def create_test_table(ddb):
    ddb.create_table(**TEST_TABLE_ATTRIBUTE_ARGS)


def populate_test_table(ddb):
    table = ddb.Table(TEST_TABLE_NAME)
    table.put_item(Item=TEST_ITEM)


def delete_test_table(ddb):
    table = ddb.Table(TEST_TABLE_NAME)
    table.delete()


@pytest.fixture
def dynamodb():
    """
    Gets local instance of DynamoDB pointed at http://localhost:8000

    Be sure to start DynamoDB locally by running:

        java -Djava.library.path=./DynamoDBLocal_lib \
             -jar DynamoDBLocal.jar \
             -sharedDb

    from the directory containing 'DynamoDBLocal.jar' and 'DynamoDBLocal_lib/'

    It is also necessary to have a 'local_testing' profile in your aws cli
    configuration. You can add this to '~/.aws/config` as:

        [profile local_testing]
        aws_access_key_id = any_string
        aws_secret_access_key = any_string
    """
    session = boto3.Session(profile_name='local_testing')
    ddb = session.resource(
        'dynamodb',
        endpoint_url='http://localhost:8000',
        region_name='local'
    )

    create_test_table(ddb)
    populate_test_table(ddb)
    yield ddb
    delete_test_table(ddb)


class TestDynamo():

    def test_dynamo_connection(self, dynamodb):
        table = dynamodb.Table(TEST_TABLE_NAME)
        assert 0 < table.item_count

    def test_email_confirmation(self, dynamodb):
        from ru_alumni import token_utils, email_utils

        # really, this is done before adding user to
        email_utils.validate_email_address(TEST_EMAIL_ADDRESS)

        # generate token
        token = token_utils.generate_token(TEST_ITEM)

        # send email...
        # hit /confirmation endpoint...

        # confirm token
        result_obj = token_utils.confirm_token(token)
        assert TEST_ITEM == result_obj

        # confirm user exists in database
        users_table = dynamodb.Table(TEST_TABLE_NAME)
        item = users_table.get_item(
            Key={
                'account_id': result_obj['account_id']
            }
        )
        assert TEST_EMAIL_ADDRESS == item['Item']['email_address']
        assert item['Item']['is_verified'] is False

        # flip is_verified flag to True
        # item['is_verified'] = True
        users_table.update_item(
            Key={
                'account_id': TEST_ACCOUNT_ID
            },
            UpdateExpression='SET is_verified = :val1',
            ExpressionAttributeValues={
                ':val1': True
            }
        )
