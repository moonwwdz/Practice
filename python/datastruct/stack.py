#! /usr/bin/python

stack = []

def pushStack():
    stack.append(raw_input('Place input element:'))

def popStack():
    if len(stack) <= 0:
        print 'Empty Stack'
    else:
        print 'Element %s be delete\n' % `stack.pop()`

CMDs = {'U':pushStack,'O':popStack}

def menuList():
    while True:
        while True:
            cmd = raw_input('Choice Which Option :').upper()
            if cmd not in 'UOQ':
                print 'There is a forbidden option!'
                break
            if cmd == 'Q':
                exit()
            CMDs[cmd]()
            break

        print "Stack's elements are : \n %s" % stack



if __name__ == '__main__':
    menuList()
