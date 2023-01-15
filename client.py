import socket



HOST = 'localhost'
PORT = 10000

# Создать сокет UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = (HOST, PORT)

# Инициализация счетчика для количества отправленных сообщений
counter = 0

while True:
    message = input("Введите сообщение для отправки или 'q' для выхода: ")
    if message == 'q':
        break

    # Увеличить счетчик сообщений
    counter += 1

    print('----------------------------------')
    print(f"Номер сообщения: {counter}")
    print('Отправка {!r}'.format(message))
    print('----------------------------------')
    # Отправить сообщение на сервер
    sent = sock.sendto(message.encode(), server_address)

    # Получить ответ от сервера
    print('ожидание получения')
    data, server = sock.recvfrom(4096)
    print('Получено {!r}'.format(data.decode()))
    print('----------------------------------')

