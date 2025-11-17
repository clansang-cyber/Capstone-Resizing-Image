import boto3
from PIL import Image
import io
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Read event inputs
    source_bucket = event['source_bucket']
    destination_bucket = event['destination_bucket']
    key = event['key']
    width = event.get('width', 800)   # default width
    height = event.get('height', 800) # default height

    # Download the image from S3
    image_object = s3.get_object(Bucket=source_bucket, Key=key)
    image_content = image_object['Body'].read()

    # Open and resize the image using Pillow
    img = Image.open(io.BytesIO(image_content))
    img = img.resize((width, height))

    # Save resized image into memory
    buffer = io.BytesIO()
    img_format = img.format if img.format else "JPEG"
    img.save(buffer, format=img_format)
    buffer.seek(0)

    # Upload back to resized bucket
    new_key = f"resized_{key}"
    s3.put_object(
        Bucket=destination_bucket,
        Key=new_key,
        Body=buffer,
        ContentType=image_object['ContentType']
    )

    return {
        "status": "success",
        "original_key": key,
        "resized_key": new_key,
        "width": width,
        "height": height
    }
