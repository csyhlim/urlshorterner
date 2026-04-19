import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from service import is_valid_url, generate_code

def test_valid_url():
    assert is_valid_url("http://google.com")

def test_invalid_url():
    assert not is_valid_url("google.com")

def test_generate_code_length():
    code = generate_code()
    assert len(code) == 6

def test_generate_code_unique():
    codes = set(generate_code() for _ in range(100))
    assert len(codes) == 100

def test_valid_https():
    assert is_valid_url("https://google.com")

def test_empty_url():
    assert not is_valid_url("")

def test_generate_code_not_none():
    assert generate_code() is not None

def test_generate_code_type():
    assert isinstance(generate_code(), str)

def test_generate_code_length_custom():
    assert len(generate_code(8)) == 8

def test_multiple_codes_unique():
    codes = [generate_code() for _ in range(50)]
    assert len(set(codes)) == 50
    
def test_get_url_none():
    from service import get_url
    assert get_url("randomcode123") is None