import os
import sys

from .config import Config
import boto3

home = os.environ["HOME"]

path_to_config = f"{home}/.config/cloudphoto/cloudphotorc"

config = Config()
try:
    cfg_file = open(path_to_config)
    config.read(cfg_file)
    print("Configs:")
    print(config)
except OSError as err:
    print(f"Error: config file not found : {err}​")
    sys.exit(os.EX_CONFIG)

session = boto3.session.Session()

required_configs = [
    "bucket",
    "aws_access_key_id",
    "aws_secret_access_key",
    "region",
    "endpoint_url",
]

# Check config values
for conf_item in required_configs:
    check_result = config.includes(conf_item)
    if isinstance(check_result, str):
        print(f"Error: config file is incomplete : {check_result} not found​")
        sys.exit(os.EX_CONFIG)

bucket = config.get("bucket")
access = config.get("aws_access_key_id")
secret = config.get("aws_secret_access_key")
region = config.get("region")
endpoint_url = config.get("endpoint_url")

S3_CLIENT = boto3.client(
    service_name="s3",
    aws_access_key_id=access,
    aws_secret_access_key=secret,
    region_name=region,
    endpoint_url=endpoint_url,
)

BUCKET_NAME = bucket

URL = f"https://{BUCKET_NAME}.website.yandexcloud.net"


    
