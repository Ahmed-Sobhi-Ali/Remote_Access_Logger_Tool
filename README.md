# Keylogger and Reverse Shell Payload

## Overview

This Python script is designed to perform several advanced functions on a target machine, providing the attacker with comprehensive control and monitoring capabilities:

1. **Netcat Downloader**:
   - **Function**: Automatically downloads a Netcat executable from a remote server.
   - **Purpose**: Netcat is used to facilitate communication between the target machine and the attacker's server, enabling remote access.

2. **Netcat Reverse Shell**:
   - **Function**: Executes the downloaded Netcat binary to open a reverse shell connection.
   - **Purpose**: Establishes a command-line interface back to the attacker, allowing them to execute commands remotely on the target machine.

3. **Keylogger**:
   - **Function**: Records all keystrokes typed on the target machine.
   - **Purpose**: Captures sensitive information such as passwords, personal messages, and other typed data, which is saved into a file for later retrieval.

4. **Data Exfiltration**:
   - **Function**: Periodically uploads the keylogger data file to a remote server.
   - **Purpose**: Ensures that the captured keystrokes are transmitted to the attacker even if the target machine is not continuously monitored.

## Features

- **Automated Tool Downloading**: Downloads and installs necessary tools without manual intervention.
- **Persistent Remote Access**: Maintains a reverse shell for continuous control over the target system.
- **Comprehensive Keystroke Logging**: Captures and logs every keystroke, including special keys, and handles them appropriately.
- **Regular Data Transmission**: Periodically sends the logged data to a remote server to ensure data is collected and available to the attacker.
## Disclaimer

**This script is intended for educational and research purposes only.** It is crucial to use such tools responsibly and within the boundaries of the law. Unauthorized use of this script for accessing or compromising systems without permission is illegal and unethical. The author disclaims all liability for any misuse or illegal activities involving this script.
