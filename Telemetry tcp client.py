import socket
import threading
import os
import struct


def receive_data(client_socket):

    while True:
        try:
            data = client_socket.recv(1024)
            if not data: 
                break
            # if endian == 'big':
                int_array = struct.unpack(f">{len(data) //4}1", data)
            # else: #endian == 'little'
                int_array - struct.unpack(f"‹{len(data)//4}i", data)
            # print ("Received:", int_array)


            with open(r"C: (Users\harip\OneDrive\Desktop\Hari FYP\Codes\COP_Requests\outputtestbigdata.txt","wb") as file:
                file.write(data)
                    
        except ConnectionResetError:
            print ("Connection closed by server.")
            client_socket.close()
            break
        
def send_file(client_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            while True:
                data = file.read()
                if not data: 
                    break
                client_socket.sendall(data)
    except FileNotFoundError:
        print(file_path)
        print("File not found.")
    except Exception as e:
        print("Error sending file:", e)

#Set up the TCP client
server_ip = '127.0.0.1'  # Server IP address
server_port = 52001
# Server port
client_socket = socket. socket (socket.AF_INET, socket.SOCK_STREAM)
#current_directory - os. path. dirname(os.path.abspath(file_))
cop_req_directory = r"C:\Users\harip\OneDrive\Desktop\Hari FYP\Codes\COP_Requests"
endian = 'big' # CHANGE ENDIANESS HERE: 'big'/'little'


try:
    client_socket.connect((server_ip, server_port))
    print (f"Connected to server {server_ip}:{server_port}")

    # Start a separate thread for receiving data
    receive_thread = threading. Thread (target=receive_data, args=(client_socket,))
    receive_thread. start()

    while (True):
        # Input file path from the user
        file = input("Enter the file path to send: ") 
        file_path = os.path.join (cop_req_directory, file)
        # Send file from main thread
        send_file(client_socket, file_path)
except ConnectionRefusedError:
    print ("Connection refused, Make sure the server is running.")
finally:
    client_socket .close()