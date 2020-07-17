import boto3

s3 = boto3.client('s3', endpoint_url='http://localhost:4572', verify=False)

buckets_json = s3.list_buckets()

print(buckets_json)

