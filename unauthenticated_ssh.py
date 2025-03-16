#!/usr/bin/python3

import sys
import paramiko
import socket

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <IP> <Port> <Command>")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]

try:
    s = socket.socket()
    s.connect((ip, port))
    m = paramiko.message.Message()
    t = paramiko.transport.Transport(s)
    t.start_client()
    m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
    t._send_message(m)
    c = t.open_session(timeout=5)
    c.exec_command(command)
    out = c.makefile("rb", 2048)
    output = out.read().decode()
    out.close()

    for line in output.split("\n"):
        print(line.strip())

except Exception as e:
    print(f"Error: {e}")

