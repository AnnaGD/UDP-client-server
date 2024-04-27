# Student Database Management System

This system comprises two main components: a client application (`client_udp.py`) and a server application (`server_udp.py`). The system allows for managing a simple student database through a TCP connection. The database supports adding, displaying, and deleting student information.

## System Requirements

- Python 3.x
- Access to two servers (or local environments) for deploying the client and server applications. The client application will be deployed on `zeus`, and the server application on `eros`.

## Server Application

The server application handles requests from the client to manage student information stored in a text file database (`students_db.txt`).

### Deployment on `eros`

1. Copy `server_udp.py` and `students_db.txt` to the `eros` server.
2. Run the server application using Python:

   ```bash
   python3 server_udp.py
   The server will start listening for incoming connections on port 12000.

## Client Application

The client application sends commands to the server to add, display, or delete student information.

### Deployment on `zeus`

1. Copy `client_udp.py` to the `zeus` server.
2. Ensure `server_host` is set to `eros.cs.txstate.edu` within `client_udp.py` to target the correct server.
3. Run the client application using Python: `python3 client_udp.py`
4. Follow the on-screen menu to interact with the student database.

## Usage

After starting the client application, you will be presented with the following options:

- **Add Student**: Enter a student's ID, first name, last name, and score to add them to the database.
- **Display Student by ID**: Enter a student's ID to display their information.
- **Display Students Above Score**: Enter a score to display information for all students with scores above the entered value.
- **Display All Students**: Displays information for all students in the database.
- **Delete Student by ID**: Enter a student's ID to delete their information from the database.
- **Exit**: Exits the client application.

## Validations

- **Student ID**: Must be numeric and exactly 6 digits long.
- **First Name and Last Name**: Must not contain numbers.
- **Score**: Must be a numeric value between 0 and 100.

## Additional Notes

- Ensure both `zeus` and `eros` servers can communicate over the network through port 13000.
- The server must be running before starting the client application.