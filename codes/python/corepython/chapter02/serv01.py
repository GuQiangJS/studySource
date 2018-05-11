# Copyright (C) 2018 GuQiangJs.
# Licensed under https://www.gnu.org/licenses/gpl-3.0.html <see LICENSE file>

import os
import socketserver
from time import ctime

from chapter02 import settings


class tcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 每次handle执行完成后，就相当于结束了本次Client与Server间的会话
        # 如果需要保持连接，则此处需要增加循环
        # https://stackoverflow.com/questions/8627986/how-to-keep-a-socket-open-until-client-closes-it
        while True:
            cmd = self.request.recv(settings.BUFFER_SIZE)
            if not cmd:
                return
            cmd = str(cmd, 'utf-8').strip().lower()
            print('handler cmd:' + cmd)
            if cmd == "date":
                self.request.sendall(self.b('Server Date is:' + ctime()))
            elif cmd == 'os':
                self.request.sendall(self.b('Server operator is:' + os.name))
            elif cmd == 'ls':
                self.request.sendall(self.b('Server file list:\n' + '\n'.join(os.listdir())))
            else:
                self.request.sendall(self.b('Unkonw cmd.'))

    def b(self, s: str):
        return bytes(s, settings.ENCODING)


if __name__ == "__main__":
    HOST, PORT = 'localhost', 5555
    with socketserver.TCPServer((HOST, PORT), tcpHandler) as server:
        print('waiting for connection...')
        server.serve_forever()
