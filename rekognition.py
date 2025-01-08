import boto3

def detect_labels(bucket, key):
    session = boto3.Session(profile_name="default")
    client = session.client("rekognition")
    
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

def main():
    bucket = "myfirsts3bucketproject"
    key = "images.jpg"
    response = detect_labels(bucket, key)
    if response:
        print("Detected Labels:")
        for label in response.get('Labels', []):
            print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%")

if __name__ == "__main__":
    main()
