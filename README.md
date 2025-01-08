AWS Rekognition Label Detection

This project demonstrates how to use AWS Rekognition to detect labels in an image stored in an S3 bucket. The script uses the AWS SDK for Python (Boto3) to interact with AWS Rekognition.

Prerequisites

AWS Account:

Ensure you have an active AWS account.

AWS CLI Configuration:

Install and configure the AWS CLI with a default profile. Set up access and secret keys for a user with rekognition:DetectLabels permission.

aws configure

Python Environment:

Python 3.7 or higher is recommended.

Install the required libraries:

pip install boto3

S3 Bucket:

Upload an image to your S3 bucket that you want to analyze.

Ensure the S3 bucket policy grants Rekognition access.

How to Use

Clone or download the repository.

Update the following variables in the script:

bucket: Replace with your S3 bucket name.

key: Replace with the path to your image in the S3 bucket.

Run the script:

python detect_labels.py

File Structure

project-folder/
|-- detect_labels.py
|-- README.md

Script Details

detect_labels.py:
This script contains the following:

detect_labels(bucket, key): Connects to AWS Rekognition and detects labels for the given image.

main(): Calls the detect_labels function and prints the detected labels.

Sample Output

When you run the script successfully, it will display detected labels and their confidence scores:

Detected Labels:
Label: Tree, Confidence: 99.45%
Label: Plant, Confidence: 98.67%

Error Handling

The script includes error handling to manage issues like:

Invalid AWS credentials

Incorrect bucket or key names

Insufficient permissions

Notes

Ensure the rekognition:DetectLabels IAM permission is granted for your user or role.

S3 bucket policies should allow Rekognition to access the specified image.

License

This project is open-source and available under the MIT License.

