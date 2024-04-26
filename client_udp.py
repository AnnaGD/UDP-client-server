# client_udp.py
# This client program interacts with a server to manage a student database using UDP.
# It supports operations such as adding, displaying, and deleting student information.

import socket

"""
    Sends a command to the server using UDP and prints the server's response.

    Parameters:
    - sock: The socket object for UDP communication.
    - server_address: Tuple containing the server's IP address and port number.
    - command: The command string to be sent to the server.
    """

def send_command(sock, server_address, command):
    sock.sendto(command.encode(), server_address) # UDP uses sendto to send messages
    response, _ = sock.recvfrom(1024) # UDP uses recvfrom to receive messages
    print("server resopnded:", response.decode())

def main():
    server_host = 'eros.cs.txstate.edu'  # Server hostname or IP address
    server_port = 12000  # Server port number

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = (server_host, server_port)


if __name__ == '__main__':
    main()