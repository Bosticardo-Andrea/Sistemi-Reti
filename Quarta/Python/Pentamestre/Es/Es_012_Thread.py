from threading import Thread
import time
#ereditarietá
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        self.runnig = True
    def run(self):
        while self.runnig:
            print(f"Sono il thread {self.name}")
            time.sleep(1)
    def stop(self):
        self.runnig  =False
def main():
    t1 = MyThread("Bob")
    t1.start()
    t2 = MyThread("Alice")
    t2.start()
    for _ in range(5):
            t1.stop()
            t2.stop()
            t1.join()
            t2.join()
if __name__=="__main__":
    main()
