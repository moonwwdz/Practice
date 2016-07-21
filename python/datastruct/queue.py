#! /usr/bin/python

queue = []

def PushQueue():
    print('+'*20)
    queue.append(raw_input("Please putin:"))

def PopQueue():
    print('='*20)
    if len(queue) < 1:
        print('Empty Queue!!!')
    else:
        print(queue.pop(0))

CMDs = {'U':PushQueue,'O':PopQueue}

def meauList():
    while True:
        while True:
            cmd = raw_input("Choice Option:").upper()
            if cmd == 'Q':
                exit()
            CMDs[cmd]()
            print('='*20)
            print(str(queue))
            print('='*20)


if __name__ == '__main__':
    meauList()
