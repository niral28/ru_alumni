# Developer's Guide

[Work in progress!]

Parth Parikh, Austus Chang, Niral Shah 


## Set up Local Repo

Clone remote GitHub repo:

    git clone https://github.com/niral28/ru_alumni.git
    cd ru_alumni

Set up your own remote development branch. For example:

    git checkout -b dev-<your-name>
    git push --set-upstream origin dev-<your-name> 

Some things to consider:
* Work on feature branches, not master
* Keep your commit messages concise
* Squash intermediate commits into logical chunks


## Set up your environment

From within `ru_alumni/`

    pip install pipenv
    pipenv install -r requirements.txt
    pipenv shell

Make sure awsebcli was installed:

    cat Pipfile | grep awsebcli

    # You should see:
    awsebcli = "*"

If not, run: `pip install awsebcli`


## Connect with AWS Elastic Beanstalk

One-time init wizard (make sure virtualenv is activated)

    eb init 

1. Select `us-east-2` for region.  
   * Session may prompt you for programmatic aws credentials. There are two ways to access AWS, through the web console and through API. 
   * If you don't know you're programmatic credentials
     * go to AWS web console and **Services -> IAM**
     * Click **Users** and select your username
     * Open the **Security Credentials** tab
     * Scroll down to and select **Create access key**
     * Save the csv file to your local machine.
   * Now that you have verified your credentials you can type them in and safely proceed!

2. Select `ru_alumni` for application to use.  
3. Choose `no` for CodeCommit 


## How to push changes to EB

* Commit your changes locally
* Build/test your changes
* Push to AWS EB: `eb deploy`
* Don't forget to push your changes to GitHub as well


## How to run tests using pytest

From the project root directory, run:

    pytest -vs

The `-v` argument enables verbose logs and `-s` outputs enables standard out (stdout) prints in terminal. 

Note: For tests in `test_dynamo.py` to run, you must have a local instance of DynamoDB running. To do this, be sure to start DynamoDB locally by running:

    java -Djava.library.path=./DynamoDBLocal_lib \
        -jar DynamoDBLocal.jar \
        -sharedDb

from the directory containing `DynamoDBLocal.jar` and `DynamoDBLocal_lib/`.

It is also necessary to have a `local_testing` profile in your aws cli
configuration. You can add this to `~/.aws/config` as:

        [profile local_testing]
        aws_access_key_id = any_string
        aws_secret_access_key = any_string
