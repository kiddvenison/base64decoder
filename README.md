# Base64 Decoder

This Python script provides a simple way to decode Base64-encoded text found within a given input string. It identifies any Base64-encoded text, decodes it, and prints the original encoded text along with the decoded text.

## Requirements

- Python 3.x

## Usage

1. Paste your input string containing Base64-encoded text(s) inside the triple quotes (`"""`) of the `input_string` variable:

   ````python
   input_string = """"

   # paste your string here, line breaks can be included

   """
   ```

2. Run the script:

   ````
   python base64_decoder.py
   ```

3. The script will print the Base64-encoded text(s) found in the input string, along with their decoded counterparts:

   ````
   <encoded_text> | <decoded_text>
   ```

## Functions

- `isBase64(sb)`: Checks if the given string or bytes `sb` is a valid Base64-encoded value.
- `decode_base64(encoded_string)`: Decodes a valid Base64-encoded string `encoded_string` and returns the decoded string.
- `process_string(input_string)`: Processes the input string `input_string`, identifies Base64-encoded text(s), and returns a dictionary with encoded and decoded text pairs.

## Example

```python
input_string = """SGVsbG8sIFdvcmxkIQ=="""

result = process_string(input_string)

for encoded_text, decoded_text in result.items():
    print(f"{encoded_text} | {decoded_text}")
```

Output:

```
SGVsbG8sIFdvcmxkIQ== | Hello, World!
```