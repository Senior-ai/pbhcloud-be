from fastapi import FastAPI
import boto3

app = FastAPI()

# Create an S3 client for IDrive e2
endpoint = "l4g4.ch11.idrivee2-2.com"
client = boto3.client("s3", endpoint_url='process.env.endpoint')

# Get list of objects in bucket 'my-bucket'
print(client.list_objects(Bucket="my-bucket"))

@app.get("/")
async def root():
    return {"message": "Hello World"}