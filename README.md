# 🖼️ Capstone-Resizing-Image

![Python](https://img.shields.io/badge/python-3.9-blue?logo=python&logoColor=white)
![AWS Lambda](https://img.shields.io/badge/AWS%20Lambda-yellow?logo=aws&logoColor=white)
![S3](https://img.shields.io/badge/AWS%20S3-orange?logo=amazons3&logoColor=white)

**Serverless image resizing pipeline** using AWS Lambda, Step Functions, and S3.

---

## 🚀 How It Works
1. Upload an image to `capstone-og-image`.  
2. Step Functions triggers `capstoneResizeImage` Lambda to:
   - Download the image
   - Resize with **Pillow**
   - Upload to `capstone-new-image`  
3. Step Functions monitors success or failure.

---

## ⚙️ Setup

### Lambda Function
- Runtime: Python 3.9  
- Layer: `Pillow-3-9-Layer`  
- Memory: 1024 MB  
- Timeout: 30–60s  

### IAM Policy
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": [
    "arn:aws:s3:::capstone-og-image/*",
    "arn:aws:s3:::capstone-new-image/*"
  ]
}
```

## ⚙️ Step Functions

Create a state machine: ImageResizeStateMachine

🔹 States

  Choice – Decide next action based on Lambda result

  Success – Triggered when image is resized successfully

  Fail – Triggered when resizing fails

🔹 Lambda Invocation Role

  Attach the IAM role with S3 access to allow Lambda to read/write images.

🔹 Workflow Diagram
<img width="957" height="572" alt="image" src="https://github.com/user-attachments/assets/1baf860e-0207-451b-af09-000f9a748c25" />


🔹 Notes

Ensure Lambda runtime matches Pillow layer version (Python 3.9)

Increase Lambda memory for large images to prevent OutOfMemory errors

## 🧪 Testing
🔹 Test the API Gateway using Postman

Open Postman and create a new POST request.

Set the request URL to your API Gateway endpoint, for example:

https://<api-id>.execute-api.<region>.amazonaws.com/upload

Go to the Body tab → select binary → choose your image file.

Click Send.

You should receive a 200 OK response if the upload succeeded.

Verify the original image appears in the capstone-image-upload bucket.

🔹Test the Step Functions

Start execution in the Step Functions console.

Wait for the execution to complete.

Verify the resized image appears in capstone-new-image.

Check CloudWatch Logs for Lambda execution details.

## 💡 Tips & Best Practices

Match Python runtime and Pillow layer version (both 3.9)

Increase Lambda memory for large images to prevent OutOfMemory

Use descriptive image filenames for easier tracking

## 📁 Project Structure

capstone-image-upload – S3 bucket for original images

capstone-new-image – S3 bucket for resized images

capstoneResizeImage – Lambda function for resizing

API Gateway – HTTP endpoint for image upload

Step Functions – Workflow automation

## 🌟 Features

Fully serverless & scalable

Automatic image resizing on upload

Easy monitoring via Step Functions & CloudWatch

Modular & reusable architecture

## 📌 References

AWS Lambda Documentation

AWS Step Functions Documentation

Boto3 S3 Integration
