import socket

HOST = 'localhost'
PORT = 10000


# Создать сокет UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Привязать сокет к определенному адресу и порту
server_address = (HOST, PORT)
print('запуск на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Инициализация счетчика для количества полученных сообщений
counter = 0

while True:
    print('\nожидание получения сообщения')
    data, address = sock.recvfrom(4096)

    # Увеличить счетчик сообщений
    counter += 1
    print('----------------------------------')
    print('Получено {} байт от {}'.format(len(data), address))
    print(f"Номер сообщения --> {counter}")
    print(f"Сообщение --> {data.decode()}")
    print('----------------------------------')

    if data:
        message = f"Номер сообщения: {counter}"
        sent = sock.sendto(message.encode(), address)
        sent = sock.sendto(data, address)
        print('отправлено {} байт обратно на {}'.format(sent, address))


