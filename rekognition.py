import boto3

def detect_labels(bucket, key):
    client = boto3.Session("rekognition")
    try:
        response = client.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key
                }
            },

        )
        return response
    except Exception as e:
        print(f"Error detecting labels: {e}")
        return None

def lambda_handler(event,context):
    bucket = event["bucket"]
    key = event["key"]
    response = detect_labels(bucket, key)
    if response:
        print("Detected Labels:")
        for label in response.get('Labels', []):
            print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")
