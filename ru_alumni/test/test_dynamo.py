import boto3
import pytest
import unittest.mock as mock

from ru_alumni import application


application.config.from_object('ru_alumni.config.TestingConfig')

TEST_TABLE_NAME = 'TestUsers'
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
    'account_id': 720,
    'email_address': 'parthr.parikh@rutgers.edu'
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

    print('\nsetup [ ]')
    create_test_table(ddb)
    populate_test_table(ddb)
    print('setup [x]')

    yield ddb

    print('\nteardown [ ]')
    delete_test_table(ddb)
    print('teardown [x]')


class TestDynamo():

    def test_dynamo_connection(self, dynamodb):
        table = dynamodb.Table(TEST_TABLE_NAME)
        assert 0 < table.item_count
