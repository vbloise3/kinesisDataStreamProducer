import boto3, json

client = boto3.client('kinesis')

# read in recordData, used to install httpd and start the httpd service on web EC2 instances
with open("./data/records.json", "rb") as f:
    records = f.read()
    
for record in records:
    response = client.put_record(
        StreamName='FirstDataStream',
        Data=json.dumps(record).encode('utf-8'),
        PartitionKey='FirstDataStream_key1'
        #ExplicitHashKey='string',
        #SequenceNumberForOrdering='string'
    )
