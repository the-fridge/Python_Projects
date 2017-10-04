"""
This program prints the base64 encoding of a string 
and then prints the base64 encoding of the obtained encoding 
and so on until the program is stopped by the user.
"""

import base64
x = 'hacktoberfest'
while True:  # Runs the program until stopped by the user
    x = base64.b64encode(str(x).encode('ascii'))  # Encodes the string in base64
    print(x)
