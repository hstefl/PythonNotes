"""
https://edube.org/learn/pcpp1-working-with-restful-apis/server-checker-once-again

Now we want to you to return to the issues discussed in lab #1. In fact, you need to implement exactly the same
functionality as you embedded in your code previously, but this time you have to use the requests module
instead of the socket module. Everything else should remain the same: the command line arguments and outputs have
to be indistinguishable.

Hint: use the head() method instead of get(), as you don't need the whole root document the server sends to you —
the header is enough to test whether or not the server is responding. Fortunately, head() has exactly the same
interface as get(). Don't forget to handle all needed exceptions — don't leave your user without any clear
explanations about anything that went wrong.
"""

import sys
import requests

if len(sys.argv) in [2, 3]:
    address = sys.argv[1]
    port = sys.argv[2] if len(sys.argv) == 3 else 80

    reply = requests.head(address, allow_redirects=True)

    print(f'Status code: {reply.status_code}')
    if reply.status_code == 200:
        for header, value in reply.headers.items():
            print(f'{header}={value}')


else:
    print('Invalid nuber if arguments. Enter IP address [port] are expected')
