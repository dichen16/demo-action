import localstack_client.session

session = localstack_client.session.Session()
s3 = session.client('s3')

buckets_json = s3.list_buckets()
print(buckets_json)

