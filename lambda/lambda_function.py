import json
import os
from headless_chrome import create_driver
from PIL import Image
import boto3
import io
import time
from datetime import datetime


def lambda_handler(_event, _context):
    """ Sample handle about how to use the imported the layer with custom parameters """
    url = "https://www.pornhub.com"
    bucket_name = "YOUR_AWS_S3_BUCKET"

    now = datetime.now()  # current date and time
    name_suffix = now.strftime("%Y-%m-%d--%H-%M-%S")
    print(f"Using name suffix: {name_suffix}")

    new_params = [
        "--window-size=3840x2160",
        "--user-agent=MyUserAgent"
    ]
    driver = create_driver(new_params)
    driver.get(url)

    print("Fetched site; waiting 15 seconds to give JS time to load dynamic stuff")
    time.sleep(15)

    print("Taking screenshot")
    screenshot = driver.get_screenshot_as_png()

    print("Saving screenshot")
    buffer = io.BytesIO(screenshot)
    buffer.seek(0)
    s3 = boto3.client("s3", aws_access_key_id="YOUR_AWS_KEY",
                      aws_secret_access_key="YOUR_AWS_SECRET",
                      region_name="eu-central-1", )
    s3.upload_fileobj(buffer, bucket_name, f"screenshot-{name_suffix}.png")
    print("Done")

    return driver.page_source
