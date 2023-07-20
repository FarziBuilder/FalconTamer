import boto3
import json

aws_access_key_id = 'AKIAUNFXI2AGTXA7PYGY'
aws_secret_access_key = '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'


runtime= boto3.client('runtime.sagemaker', 
                      region_name='us-east-1',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key)


payload = {"text": "Human: What are asteroids?", "text_length": 50}


response = runtime.invoke_endpoint(EndpointName='falcon7b-model-ds-2023-07-08-11-03-30-763-endpoint',
                                   ContentType='application/json',
                                   Body=json.dumps(payload))

print(json.loads(response['Body'].read().decode('utf-8'))[0]['generated_text'])


