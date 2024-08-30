from dotenv import load_dotenv
from pathlib import Path
import os

# 或者指定 .env 文件位置
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

# Test
keys = ["OSS_ACCESS_KEY_ID", "OSS_ACCESS_KEY_SECRET", "OSS_BUCKET_NAME", "OSS_ENDPOINT"]
for key in keys:
    print(key)
    print(os.getenv(key, default=None))


# Test Download
from oss2 import Auth, Bucket

auth = Auth(os.getenv("OSS_ACCESS_KEY_ID"), os.getenv("OSS_ACCESS_KEY_SECRET"))
bucket = Bucket(auth, os.getenv("OSS_ENDPOINT"), os.getenv("OSS_BUCKET_NAME"))

test_file = "研发/字体特效-模型/点字 299.csv"

bucket.get_object_to_file(test_file, "./test.csv")