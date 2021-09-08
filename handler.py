import requests
import boto3
import uuid


def hello(event, context):
    url = "https://api.giphy.com/v1/gifs/trending?api_key=Fu6tWQivEENqj0lceLWwUdypMvnl1Tfy&q"
    response = requests.get(
        "https://api.giphy.com/v1/gifs/trending?api_key=Fu6tWQivEENqj0lceLWwUdypMvnl1Tfy&q")
    print(response.json()["data"][0]["url"])
    response = requests.get(url, stream=True)

    session = boto3.Session()
    s3 = session.resource('s3')

    bucket_name = 'tonussibucket'
    key = str(uuid.uuid4())
    bucket = s3.Bucket(bucket_name)
    bucket.upload_fileobj(response.raw, key)
    return True
