import threading

def one(age):
    while True:
        print('i am a child',age)
    return

def two(age):
    while True:
        print('i am second child',age)
    return


if __name__ == '__main__' : 
    
    first = threading.Thread(target=one, args=(5,))
    second = threading.Thread(target=two, args=(3,))
    first.start()
    second.start()
    first.join()
    second.join()

    
    while True:
        print('i am parent')
        
    pass