from base64 import b64encode
from base64 import b64decode

class Encode:
    def __init__(self):
        hello = ""


    def encode(self, original_file):
        with open(original_file, "rb") as original_file:
            encoded_data = b64encode(original_file.read())
            return encoded_data


    def decode(self, encoded_file, file_ending):
        decoded_file = b64decode(encoded_file)
        filename = f'decoded_file.{file_ending}'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(decoded_file)