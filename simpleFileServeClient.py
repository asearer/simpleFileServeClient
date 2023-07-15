import socket

def download_file(file_name):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 8888))

    server_socket.sendall(file_name.encode('utf-8'))
    response = server_socket.recv(1024)

    if response == b'OK':
        data = b''
        while True:
            chunk = server_socket.recv(1024)
            if not chunk:
                break
            data += chunk

        with open(file_name, 'wb') as file:
            file.write(data)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Error: {response.decode('utf-8')}")

    server_socket.close()

file_name = input("Enter the name of the file you want to download: ")
download_file(file_name)
