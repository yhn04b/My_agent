import os
import getpass

def get_api_key():
    key = os.getenv('DEEPSEEK_API_KEY')

    if not key:
        key = getpass.getpass("DeepSeek API key: ")
        
    if not key:
        raise ValueError("API Key cannot be empty.")

    return key