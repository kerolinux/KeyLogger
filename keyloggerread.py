import socket


IP = '127.0.0.1'  
PORT = 12345  # Choose the same port number

def receive_keys():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((IP, PORT))
            s.listen()
            print(f"Listening for connections on {IP}:{PORT}")
            while True:
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print('Received:', data.decode())
    except Exception as e:
        print("Error receiving keys:", e)

def main():
    receive_keys()

if __name__ == '__main__':
    main()
