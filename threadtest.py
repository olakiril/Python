import threading
import time
global state
class SummingThread(threading.Thread):
     def __init__(self,low,high):
         super(SummingThread, self).__init__()
         self.low=low
         self.high=high
         self.total=0
         self.test=0
         global state
         state = 0

     def run(self):
         global state
         for i in range(self.low,self.high):
             self.total+=i
             print(i)
             time.sleep(i)
             if state==1:
                 quit()


thread1 = SummingThread(0,5)
thread2 = SummingThread(5,10)

thread1.start() # This actually causes the thread to run
thread2.start()
time.sleep(2)
state = 1
thread1.join()  # This waits until the thread has completed
thread2.join()
# At this point, both threads have completed
result = thread1.total + thread2.total
print(result)