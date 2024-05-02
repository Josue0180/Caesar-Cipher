from app import create_app
from app.encode import encode

flask_app = create_app()

def test_encode_function():
    encoded_message = encode("ABCD", 2)
    assert encoded_message == "CDEF"