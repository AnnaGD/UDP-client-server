# server_udp.py
# This server program handles client requests to manage a student database using UDP.
# Supported operations include adding, displaying, and deleting student information.

import socket

def handle_client(dta, client_address, sock, db_file):
    """
    Handles a single client request received via UDP

    Parameters:
    - data: The data received from the client.
    - client_adress: The address of the client that sent the data.
    - db_file: The path to the database file storing student inforamation.
    """

    print(f"Received from {client_address}: {data.devode()}")
    command, *args = data.decode().split(',')

    

def main():
    server_port = 12000
    db_file = "students_db.txt" # The database file path

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.blind(('', server_port))
        print("Server is listening for UDP trsafic")

        while True:
            data, client_address  = server.recvfrom(2048)
            handle_client(data, client_address, server_socket, db_file)

if __name__ == '__main__':
    main()
