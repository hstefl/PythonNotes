"""
We want you to write a simple CLI (Command Line Interface) tool which can be used in order to diagnose the current status
 of a particular http server. The tool should accept one or two command line arguments:

 * (obligatory) the address (IP or qualified domain name) of the server to be diagnosed (the diagnosis will be
   extremely simple, we just want to know if the server is dead or alive)
 * (optional) the server's port number (any absence of the argument means that the tool should use port 80)
 * use the HEAD method instead of GET — it forces the server to send the full response header but without any content;
   it's enough to check if the server is working properly; the rest of the request remains the same as for GET.

We also assume that:

 * the tool checks if it is invoked properly, and when the invocation lacks any arguments, the tool prints an error
   message and returns an exit code equal to 1;
 * if there are two arguments in the invocation line and the second one is not an integer number in the range 1..65535,
   the tool prints an error message and returns an exit code equal to 2;
 * if the tool experiences a timeout during connection, an error message is printed and 3 is returned as the exit code;
 * if the connection fails due to any other reason, an error message appears and 4 is returned as the exit code;
 * if the connection succeeds, the very first line of the server’s response is printed.

Hints:

    to access command line arguments, use the argv variable from the sys module; its length is always one more than the actual number of arguments, as argv[0] stores your script's name; this means that the first argument is at argv[1] and the second at argv[2]; don't forget that the command line arguments are always strings!
    returning an exit code equal to n can be achieved by invoking the exit(n) function.

"""
import socket
import sys

return_code = 0
connection_established = False


if len(sys.argv) not in [2, 3]:
    print('Incorrect program arguments, expected: ')
    print('\tpython training_1.py IP_or_qualified_domain_name" [port]')
    exit(1)
else:
    end_point_address = sys.argv[1]
    end_point_port = int(sys.argv[2]) if (len(sys.argv) > 2) else 80
    sck = None

    if end_point_port <= 0 or end_point_port > 65536:
        print("Invalid port")
        exit(2)
    try:
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sck.connect((end_point_address, end_point_port))
        connection_established = True

        sck.sendall(b'HEAD / HTTP/1.1\r\n'
                 + b'Host: ' + bytes(end_point_address, 'UTF-8') + b'\r\n'
                 + b'Connection: close\r\n'
                 + b'\r\n')

        response = sck.recv(10000).decode().split('\r\n')

        code = int(response[0].strip().split(' ')[-1])
        proto_code = response[0].strip()

        if code == 200:
            print(f"{proto_code}")
    except socket.timeout as e:
        print('Connection timeout')
        return_code = 3

    except ConnectionRefusedError as e:
        print('Connection refused')
        return_code = 4

    except Exception as e:
        print('Connection error {}', e)
        return_code = 4

    finally:
        if connection_established:
             # Disable further sends or receives on an active connection.
             sck.shutdown(socket.SHUT_RDWR)

        # Frees the socket resources. This can still be safely called even if the connection was refused,
        # as it simply ensures the socket is properly closed.
        sck.close()

        exit(return_code)
