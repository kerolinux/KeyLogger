# Keylogger Project

This project is intended for educational purposes only. Please use it responsibly and only on systems that you have explicit permission to monitor.

## Introduction

This repository contains a basic keylogger implementation in Python. It includes three main components:

1. **Main Keylogger**: Captures keystrokes from the keyboard and sends them to a specified IP address and port.
2. **Keylogger Reader**: Listens for incoming keystrokes on the specified IP address and port, then displays them.
3. **Keylogger GUI**: Provides a graphical interface for starting and stopping the keylogger, displaying captured keystrokes, and indicating the status of the keylogger.

## Components

### Main Keylogger

The `main_keylogger.py` file contains the code for capturing keystrokes from the keyboard and sending them to a remote host.

### Keylogger Reader

The `keylogger_reader.py` file contains the code for listening to incoming keystrokes on a specified IP address and port, then displaying them on the console.

### Keylogger GUI

The `keylogger_gui.py` file contains the code for a graphical user interface (GUI) that allows users to start and stop the keylogger, view captured keystrokes, and monitor the status of the keylogger.

## Usage

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the desired keylogger component:

    - For the Main Keylogger: Run `python main_keylogger.py`.
    - For the Keylogger Reader: Run `python keylogger_reader.py`.
    - For the Keylogger GUI: Run `python keylogger_gui.py`.

## Disclaimer

This project is for educational purposes only. The authors are not responsible for any misuse of this software.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
