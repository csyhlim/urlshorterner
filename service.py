import string
import random
from storage import load_data, save_data

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

def shorten_url(url):
    if not is_valid_url(url):
        raise ValueError("Invalid URL")

    data = load_data()
    code = generate_code()

    while code in data:
        code = generate_code()

    data[code] = url
    save_data(data)

    return code

def get_url(code):
    data = load_data()
    return data.get(code)