# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

import socket

from chapter02 import settings

with socket.socket() as client:
    try:
        client.connect((settings.HOST, settings.PORT))
    except ConnectionRefusedError:
        print('Server is out of service.')
    else:
        while True:
            data = input('> ')
            if not data:
                break
            client.send(bytes(data, settings.ENCODING))
            data = client.recv(settings.BUFFER_SIZE)
            if not data:
                break
            print(data.decode(settings.ENCODING))
