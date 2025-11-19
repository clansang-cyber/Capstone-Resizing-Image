import boto3
from PIL import Image
import io
import json

s3 = boto3.client('s3')

DEST_BUCKET = 'capstone-new-image'

def lambda_handler(event, context):
    try:
        # If triggered by API Gateway → event["body"] is a string
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event

        # Required fields
        source_bucket = body["source_bucket"]
        key = body["key"]

        # Download the original image
        response = s3.get_object(Bucket=source_bucket, Key=key)
        image_bytes = response["Body"].read()

        # Load image via Pillow
        with Image.open(io.BytesIO(image_bytes)) as img:
            img.thumbnail((128, 128))

            # Ensure format always exists (default to JPEG)
            image_format = img.format if img.format else "JPEG"

            # Save resized image into memory
            buffer = io.BytesIO()
            img.save(buffer, format=image_format)
            buffer.seek(0)

        # Save resized image
        resized_key = f"resized-{key}"
        s3.put_object(
            Bucket=DEST_BUCKET,
            Key=resized_key,
            Body=buffer
        )

        # Step Functions-friendly output
        return {
            "status": "SUCCESS",
            "resized_key": resized_key,
            "message": f"Image resized successfully and saved as {resized_key}"
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
