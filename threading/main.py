import time
import threading
from src.xutils.xutils import synchronized

	
total = 0
		
@synchronized
def count():
    global total
    curr = total + 1
    time.sleep(0.1)
    total = curr
		
def counter():
    for i in range(0,20): count()
		
thread1 = threading.Thread(target = counter)
thread2 = threading.Thread(target = counter)

thread1.start()
thread2.start()
    
thread1.join()
thread2.join()

print('%d' % (total))