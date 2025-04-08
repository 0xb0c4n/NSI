import threading 

verrou1 = threading.Lock()
verrou2 = threading.Lock()
verrou3 = threading.Lock()

def f1():
    verrou1.acquire()
    print("verrou 1 : p1")
    verrou2.acquire()
    print("verrou 2 : p1")
    verrou2.release()
    verrou1.release()

def f2():
    verrou2.acquire()
    print("verrou 2 : p2")
    verrou3.acquire()
    print("verrou 3 : p2")
    verrou3.release()
    verrou2.release()

def f3():
    verrou1.acquire()
    print("verrou 1 : p3")
    verrou3.acquire()
    print("verrou 3 : p3")
    verrou3.release()
    verrou1.release()

t1 = threading.Thread(target=f1, args=[])
t2 = threading.Thread(target=f2, args=[])
t3 = threading.Thread(target=f3, args=[])

t1.start()
t2.start()
t3.start()