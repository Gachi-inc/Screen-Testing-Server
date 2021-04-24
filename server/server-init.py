from Socket import Socket


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.users = []

    def set_up(self):
        self.socket.bind(("192.168.1.7", 6543))
        self.socket.listen()
        print("Server is started!")
        # self.accept_sockets()
        self.socket.setblocking(False)

    # Отправка данных
    async def send_data(self, data):
        for user in self.users:
            await self.main_loop.sock_sendall(user, data)

    # Принимает данные
    async def listen_socket(self, listened_socket):
        if not listened_socket:
            return

        # Обработка данных
        while True:
            data = await self.main_loop.sock_recv(listened_socket, 2048)
            print(data)
            # await self.send_data(data)
            if not data:
                print("Client disconnected")
                self.users.remove(listened_socket)
                return

    async def accept_sockets(self):
        while True:
            # Принимает входящее подключение
            try:
                user_socket, address = await self.main_loop.sock_accept(
                    self.socket
                )
                print(f"User {address[0]} was connected!")
                self.users.append(user_socket)
                self.main_loop.create_task(self.listen_socket(user_socket))
            except BaseException:
                print("Something wrong happen")
                return

    async def main(self):
        await self.main_loop.create_task(self.accept_sockets())


if __name__ == '__main__':
    server = Server()
    server.set_up()

    server.start()
