import base64
x = 'hacktoberfest'
while True:
    x = base64.b64encode(str(x).encode('ascii'))
    print(x)
