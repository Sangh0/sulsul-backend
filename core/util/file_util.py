import urllib
import uuid

from botocore.exceptions import BotoCoreError, ClientError
from fastapi import UploadFile, HTTPException
from starlette import status

from core.client.aws_client import S3Client
from core.config.var_config import S3_BUCKET_NAME

directories = ["images"]

s3 = S3Client()


def upload_file_to_s3(file: UploadFile, directory: str) -> str:
    if directory not in directories:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="invalid directory"
        )

    filename = f"{str(uuid.uuid4())}.jpg"
    s3_key = f"{directory}/{filename}"

    try:
        s3.upload_fileobj(file.file, s3_key)
    except (BotoCoreError, ClientError) as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"S3 upload failed: {str(e)}",
        )

    url = "https://s3-ap-northeast-2.amazonaws.com/%s/%s" % (
        S3_BUCKET_NAME,
        urllib.parse.quote(s3_key, safe="~()*!.'"),
    )

    return url
