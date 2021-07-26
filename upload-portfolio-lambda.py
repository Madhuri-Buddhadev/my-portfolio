import json
import boto3
from botocore.client import Config
import zipfile
from io import BytesIO
import mimetypes

    def lambda_handler(event, context):
 try:
    s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))
    sns = boto3.resource('sns')

    portfolio_bucket = s3.Bucket('portfoliobuild.madhuribuddhadev.com')

    build_bucket = s3.Bucket('portfoliobuild.madhuribuddhadev.com')

    build_bucket.download_file('portfoliobuild.zip','/tmp/portfoliobuild.zip')
    topic.publish(Subject="Update",Message="Portfolio Deployed Succesfully.")
    buffer = BytesIO()
    portfolio_zip = BytesIO()
    build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)

    with zipfile.ZipFile(portfolio_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
            portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    topic = sns.Topic('arn:aws:sns:us-east-1:556253038249:deployPortfolioTopic')
    s3 = boto3.resource('s3',config=Config(signature_version='s3v4'))
   sns = boto3.resource('sns')
   build_bucket = s3.Bucket('portfoliobuild.madhuribuddhadev.com')
   portfolio_bucket = s3.Bucket('portfoliobuild.madhuribuddhadev.com')

   build_bucket = s3.Bucket('portfoliobuild.madhuribuddhadev.com')
   build_bucket.download_file('portfoliobuild.zip','/tmp/portfoliobuild.zip')
   topic.publish(Subject="Update",Message="Portfolio Deployed Succesfully.")
   buffer = BytesIO()
   portfolio_zip = BytesIO()
   build_bucket.download_fileobj('portfoliobuild.zip',portfolio_zip)
         with zipfile.ZipFile(portfolio_zip) as myzip:
         for nm in myzip.namelist():
          obj = myzip.open(nm)
           portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
           portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    with zipfile.ZipFile(portfolio_zip) as myzip:
     for nm in myzip.namelist():
     obj = myzip.open(nm)
      portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
      portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
    with zipfile.ZipFile(portfolio_zip) as myzip:
     for nm in myzip.namelist():
     obj = myzip.open(nm)
      portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]}) portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
with zipfile.ZipFile(portfolio_zip) as myzip:
    for nm in myzip.namelist():
        obj = myzip.open(nm)
        portfolio_bucket.upload_fileobj(obj,nm,ExtraArgs={'ContentType':mimetypes.guess_type(nm)[0]})
        portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
        topic = sns.Topic('arn:aws:sns:us-east-1:556253038249:deployPortfolioTopic')

   except:
    topic.publish(Subject="Deployment failed",Message="Portfolio Deployment Failed.")
   raise
 return "Hi here"
