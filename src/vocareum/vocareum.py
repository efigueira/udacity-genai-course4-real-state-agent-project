import os
from pathlib import Path


def load_vocareum_key():
    api_key_path = Path(__file__).parent.parent.parent / "vocareum_key"

    if api_key_path.is_file():
        with open(api_key_path, 'r') as f:
            api_key = f.read()
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_BASE"] = "https://openai.vocareum.com/v1"
        print(f'Loaded API key: {api_key_path}')
    else:
        print('API key not found')
        return ValueError('API key not found')
