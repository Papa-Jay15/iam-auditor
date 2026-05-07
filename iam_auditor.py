import boto3
from datetime import datetime, timezone

print("=" * 50)
print("   IAM AUDITOR by papa_jay")
print("=" * 50)

iam = boto3.client('iam')
users = iam.list_users()

for user in users['Users']:
    username = user['UserName']
    print(f"USER: {username}")
    keys = iam.list_access_keys(UserName=username)
    for key in keys['AccessKeyMetadata']:
        status = key['Status']
        created = key['CreateDate']
        age = (datetime.now(timezone.utc) - created).days
        print(f"  KEY: {status} | AGE: {age} days")
        if age > 90:
            print(f"  WARNING: Key too old!")
    print("")

print("SCAN COMPLETE!")
