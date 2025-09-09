import time,threading
def gf(n):
    for i in range(n):
        print("Speaking to Girl Friend")
        time.sleep(1)
def exgf(n):
    for i in range(n):
        print("Spaeaking to Ex Girl friend")
        time.sleep(1)
it=time.time()
gf(5)
exgf(5)
ft=time.time()
gf=threading.Thread(target=gf,args=(5,))
exgf=threading.Thread(target=exgf,args=(5,))
gf.start()
exgf.start()
print(gf.is_alive())
gf.join()
print(threading.enumerate())
print(ft-it)
threading.active_count()
#print(gf.name())
exgf.join()




