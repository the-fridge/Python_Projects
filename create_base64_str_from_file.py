import base64


# Create a base64 encoded string of a file (e.g. PDF, jpg)
def get_b64_string(file_path):
	# Use a context managager to open and close the file
    with open(file_path, 'rb') as fp:
		# Encode the file using base64
        enc_file = base64.b64encode(fp.read())
		# Decode the base64 encoded file to a string
        dec_enc_file = enc_file.decode('utf-8')
        return dec_enc_file
