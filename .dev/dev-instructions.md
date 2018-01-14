# Developer's Guide

[Work in progress!]

Parth Parikh, Austus Chang, Niral Shah 


## Set up Local Repo

Clone remote GitHub repo:
```
git clone https://github.com/niral28/ru_alumni.git
cd ru_alumni
```

Set up your own remote development branch. For example:
```
git checkout -b dev-<your-name>
git push --set-upstream origin dev-<your-name> 
```

Some things to consider:
* Work on feature branches, not master
* Keep your commit messages concise
* Squash intermediate commits into logical chunks


## Set up your environment

From within `ru_alumni/`
```
pip install pipenv
pipenv install -r requirements.txt
pipenv shell
```

Make sure awsebcli was installed:
```
cat Pipfile | grep awsebcli

# You should see:
awsebcli = "*"
```

If not, run: `pip install awsebcli`


## Connect with AWS Elastic Beanstalk

One-time init wizard
```
eb init 
```
Select `us-east-2` for region.  
Select `ru_alumni` for application to use.  
Choose `no` for CodeDeploy  
Enter your AWS access and secret keys when prompted


## How to push changes to EB

* Commit your changes locally
* Build/test your changes
* Push to AWS EB: `eb deploy`
* Don't forget to push your changes to GitHub as well
