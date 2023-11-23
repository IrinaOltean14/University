import socket, struct, random, time

if __name__ == '__main__':
    try:
        s = socket.create_connection(('127.0.0.1', 1234))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    finished = False
    st = 1
    dr = 10000
    random.seed()
    try:
        data = s.recv(1024)
        print(data.decode('ascii'))
    except socket.error as msg:
        print("Error: ", msg.strerror)
        exit(-1)

    step_count = 0
    while not finished:
        my_num = random.randint(st,dr)
        try:
            s.send(struct.pack('!I', my_num))
            answer = s.recv(1)
        except socket.error as msg:
            print("Error: ", msg.strerror)
            s.close()
            exit(-1)
        step_count += 1
        answer = answer.decode('ascii')

        print('Sent ', my_num, ' to the server, received back ', answer)
        if answer == 'H':
            st = my_num
        elif answer == 'S':
            dr = my_num
        else:
            finished = True
        time.sleep(0.5)

    s.close()
    if answer == 'G':
        print("I am the winner with", my_num, "in", step_count, "steps")
    else:
        print("I lost !!!")



