# server_udp.py
# This server program handles client requests to manage a student database using UDP.
# Supported operations include adding, displaying, and deleting student information.

import socket

def handle_client(data, client_address, sock, db_file):
    """
    Handles a single client request received via UDP

    Parameters:
    - data: The data received from the client.
    - client_adress: The address of the client that sent the data.
    - db_file: The path to the database file storing student inforamation.
    """

    print(f"Received from {client_address}: {data.decode()}")
    command, *args = data.decode().split(',')

    if command == "add":
        with open(db_file, "a") as f:
            f.write(','.join(args) + "\n")
        response = "Student added successfully"
    elif command == "display_id":
        id = args[0]
        response = "Student not found"
        with open(db_file, "r") as f:
            for line in f:
                if line.startswith(id + ","):
                    response = line.strip()
                    break
    elif command == "display_score":
        score = int(args[0])
        reponse = ""
        with open(db_file, "r") as f:
            for line in f:
                if int(line.split(',')[3]) > score:
                    response += line
        response = response or "Np students found above the score."
    elif command == "display_all":
        with open(db_file, "r") as f:
            response = f.read().strip()
        response = response or "No student found"
    elif command == "delete":
        id = args[0]
        found = False
        lines = []
        with open(db_file, "r") as f:
            lines = f.readlines()
        with open(db_file, "w") as f:
            for line in lines:
                if line.startswith(id + ","):
                    found = True
                else:
                    f.write(line)
        response = "Student delete successfully." if found else "ID does not exit."
    elif command == "exit":
        response = "Program completed, Exiting..."
    else:
        response = "Invalid Command!"

    sock.sendto(response.encode(), client_address)

def main():
    server_port = 13000
    db_file = "students_db.txt" # The database file path

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('', server_port))
        print("Server is listening for UDP trsafic")

        while True:
            data, client_address  = server_socket.recvfrom(2048)
            handle_client(data, client_address, server_socket, db_file)

if __name__ == '__main__':
    main()
