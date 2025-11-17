# Capstone-Resizing-Image
Capstone Project: Serverless Image Processing Pipeline

A serverless workflow to automatically resize images using AWS Lambda, Step Functions, and S3.

How It Works

Upload an image to the source S3 bucket (capstone-og-image).

Step Functions invokes a Lambda function (capstoneResizeImage) that:

Downloads the image

Resizes it using Pillow

Uploads the resized image to the destination S3 bucket (capstone-new-image)

Step Functions monitors success/failure.

Setup Steps

Upload image to S3

Use the source bucket capstone-og-image.

Lambda Function

Runtime: Python 3.9

Attach Pillow layer (Pillow-3-9-Layer)

Memory: 1024 MB, Timeout: 30–60 sec

IAM Role

Attach policy for S3 access:

{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": [
    "arn:aws:s3:::capstone-og-image/*",
    "arn:aws:s3:::capstone-new-image/*"
  ]
}


Step Functions

Create state machine ImageResizeStateMachine

Attach Lambda invocation role

Include choice, success, and fail states

Test

Start execution in Step Functions console

Check resized image in capstone-new-image

View CloudWatch logs for Lambda execution

Tips

Match Python runtime and layer version (both 3.9).

Increase memory for large images to prevent OutOfMemory errors.
