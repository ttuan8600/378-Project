#this file will be what is called by the webserver(website) and will handle the input data.
import sys
import main
import time
import os
import socket

#ask user to input port and validate it
def get_port():
    #make sure input is a number not radom text
    try:
        port = int(input("what is the Port: "))
    except:
        print("invalid port")
        get_port()
    #check if input is valid port range
    if port < 1 or port >65535:
        print("invalid Port")
        get_port
    else:
        return port
#set local host to listen to all ips trying to connect to our server and set port to input
HOST = '0.0.0.0'
PORT = 1024
#create a socket called sock
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    #bind the socket to the ip and port
    sock.bind((HOST, PORT))
    #let server to connect to one address
    sock.listen(1)
    #accept the connection to the socket
    #conn is the socket itself and addr is the ip
    conn, addr = sock.accept()
    with conn:
        print('Connected by', addr)
        while True:
            #receive 1024 bytes from the client.
            data = conn.recv(1024)
            if not data: break
            print(addr,":",data.decode())
            #turn received data back into caps and send it back 
            conn.sendall(data.upper())

# #code from random website

# def main():
#     # [0] is used for filename
#     email = sys.argv[1]
#     password = sys.argv[2]
    
#     return 1

#     main.login_email(email,password)
    
    

    
#     while not os.path.exists(email+"call.txt"):
#         time.sleep(2)
#     with open(email+"call.txt") as file:
#         var_return = file.readline().strip()
    
#         if var_return == "1":
#             main.call()
#         else:
#             main.text(email)

#     main.open_mycsulb()
#     main.log_info(email,password)
#     main.driver.close
#     # for i, arg in enumerate(sys.argv):
#     #    with open("test.txt",'+a') as file:
#     #        file.write(arg)
           
#     #     # print(f"Argument {i:>6}: {arg}")
# if __name__ == "__main__":
#     main()