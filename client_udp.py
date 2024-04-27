# client_udp.py
# This client program interacts with a server to manage a student database using UDP.
# It supports operations such as adding, displaying, and deleting student information.

import socket

def send_command(sock, server_address, command):
    """
    Sends a command to the server using UDP and prints the server's response.
    
    Parameters:
    - sock: The socket object for UDP communication.
    - server_address: Tuple containing the server's IP address and port number.
    - command: The command string to be sent to the server.
    """
    try:
        sock.sendto(command.encode(), server_address) # UDP uses sendto to send messages
        sock.settimeout(2)  # Set a timeout for UDP response
        response, _ = sock.recvfrom(1024) # UDP uses recvfrom to receive messages
        print("Server responded:", response.decode())
    except socket.timeout:
        print("Request timed out. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    server_host = 'eros.cs.txstate.edu'  # Server hostname or IP address update to eros.cs.txstate.edu
    server_port = 13000  # Server port number

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        server_address = (server_host, server_port)

        # Main loop to display the menu and handle user input
        while True:
            print("1. Add student")
            print("2. Display students by ID")
            print("3. Display student above score")
            print("4. Display all students")
            print("5. Delete student by ID")
            print("6. Exit")
            choice = input("Please select an option: ")

            if choice == '1':
                # Collect necessary information for adding a student
                id = input("Enter ID: ")
                while not (id.isdigit() and len(id) == 6):
                    print("Invalid ID. ID must be exactly 6 digits long and numeric.")
                    id = input("Enter ID: ")
                fname = input("Enter first name: ")
                while not fname.isalpha():
                    print("Invalid first name. Name must not contain numbers.")
                    fname = input("Enter first name: ")
                lname = input("Enter last name: ")
                while not lname.isalpha():
                    print("Invalid last name. Name must not contain numbers.")
                    lname = input("Enter last name: ")
                score = input("Enter score: ")
                while not (score.isdigit() and 0 <= int(score) <= 100):
                    print("Invalid score. Score must be a number between 0 and 100.")
                    score = input("Enter score: ")
                # Construct and send the add command
                command = f"add,{id},{fname},{lname},{score}"
                send_command(client_socket, server_address, command)

             # Option 2: Prompt the user to enter a student ID
            elif choice == '2':
                id = input("Enter ID: ")
                # A valid ID must be numeric and exactly 6 digits long.
                while not (id.isdigit() and len(id) == 6):
                    # If the ID is invalid (either not all digits or not exactly 6 digits),
                    # inform the user and prompt for the ID again.
                    print("Invalid ID. ID must be exactly 6 digits.")
                    id = input("Enter ID: ")
                command = f"display_id,{id}"
                # Construct and send the add command
                send_command(client_socket, server_address, command)

            # Option 3: Prompt the user to enter a score
            elif choice == '3':
                score = input("Please enter a score: ")
                while not (score.isdigit() and 0 <= int(score) <= 100):
                    print("Invalid score. Score must be a number between 0 and 100.")
                    score = input("Enter score: ")
                command = f"display_score,{score}"
                # Construct and send the command
                send_command(client_socket, server_address, command)

            # Option 4: Prompt the user to enter a student ID `Display All`
            elif choice == '4':
                command = "display_all"
                # Construct and send the command
                send_command(client_socket, server_address, command)

            # Option 5: Prompt the user to enter an ID they would like to delete
            elif choice == '5':
                id = input("Enter ID you'd like to delete: ")
                # Validate ID: only numbers and exactly 6 digits
                while not (id.isdigit() and len(id) == 6):
                    print("Invalid ID. ID must be exactly 6 digits long and numeric.")
                    id = input("Enter ID you'd like to delete: ")
                command = f"delete,{id}"
                # Construct and send the command
                send_command(client_socket, server_address, command)

            # Option 6: Exit the program
            elif choice == '6':
                # Construct and send the exit command
                send_command(client_socket, server_address, "exit")
                print("Exiting...")
                break # Exit the while loop to end the program
            else:
                # Handle general invalid input option selection
                print("Invalid selection! Please try again.")
                

def get_validated_input(prompt, error_message, validation_func):
    """
    Generic input validation function.
    """
    user_input = input(prompt)
    while not validation_func(user_input):
        print(error_message)
        user_input = input(prompt)
    return user_input


if __name__ == '__main__':
    main()