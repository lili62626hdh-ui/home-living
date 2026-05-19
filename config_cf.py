import os

# Cloudflare R2 Configuration
CF_R2_ACCESS_KEY_ID = os.getenv('CF_R2_ACCESS_KEY_ID', '')
CF_R2_SECRET_ACCESS_KEY = os.getenv('CF_R2_SECRET_ACCESS_KEY', '')
CF_R2_BUCKET_NAME = os.getenv('CF_R2_BUCKET_NAME', '')
CF_R2_ENDPOINT_URL = os.getenv('CF_R2_ENDPOINT_URL', '')
