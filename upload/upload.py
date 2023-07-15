import boto3

def lambda_handler(event, context):
   
    s3 = boto3.client('s3')
       
    file_path = 'test.txt'
        
    bucket_name = 'umarzamy-chf-upload'
    key = 'ok.txt'
    s3.upload_file(file_path, bucket_name, key)
    
    return {
        'statusCode': 200,
        'body': 'ok'
    }
