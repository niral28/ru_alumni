import boto3
import pytest
import unittest.mock as mock
from ru_alumni import application


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
    ddb = session.client(
        'dynamodb',
        endpoint_url='http://localhost:8000',
        region_name='local'
    )
    print('\nsetup')
    # return ddb
    yield ddb
    print('\nteardown')


class TestDynamo():

    def test_dynamo_connection(self, dynamodb):
        response = dynamodb.list_tables()
        assert 'ResponseMetadata' in response
        assert 'HTTPStatusCode' in response['ResponseMetadata']
        assert 200 == response['ResponseMetadata']['HTTPStatusCode']
