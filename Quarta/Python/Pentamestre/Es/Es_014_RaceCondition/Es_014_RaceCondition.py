from threading import Thread, Lock
import time
lock = Lock()#mutex
class MyThread(Thread):
    def __init__(self,file,data):
        Thread.__init__(self)
        self.file = file
        self.data = data
    def run(self):
        lock.acquire()
        for riga in self.data:
            self.file.write(riga)#sezione critica
            time.sleep(0.2)
        lock.release()
def main():
    fileName = "racecondition.txt"
    AliceData =["Alilce\n"]*10
    BobData =["Bob\n"]*10
    f = open(fileName,"w")
    alice = MyThread(f,AliceData)
    bob = MyThread(f,BobData)
    alice.start()
    bob.start()
    alice.join()
    bob.join()
    f.close()
if __name__=="__main__":
    main()