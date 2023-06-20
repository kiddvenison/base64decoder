import base64
import re

def isBase64(sb):
    try:
        if isinstance(sb, str):
            sb_bytes = bytes(sb, 'ascii')
        elif isinstance(sb, bytes):
            sb_bytes = sb
        else:
            raise ValueError("Argument must be string or bytes")
        return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
    except Exception:
        return False

def decode_base64(encoded_string):
    try:
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except UnicodeDecodeError:
        return None

def process_string(input_string):
    words = input_string.split()
    result = {}

    for word in words:
        if isBase64(word):
            decoded_word = decode_base64(word)
            if decoded_word is not None:
                result[word] = decoded_word
        else:
            result[word] = "Not a base64 string"

    return result

try:
    input_string = """

    # paste your string here, line breaks can be included 

    """
    result = process_string(input_string)

    if len(result) == 0:
        print("No base64 encoding found in the provided string.")
    else:
        for encoded_text, decoded_text in result.items():
            print(f"{encoded_text} | {decoded_text}")
except Exception as e:
    print(f"An issue occurred while running the script: {str(e)}")

# end of script
