import threading
	
def synchronized(func):
	
    func.__lock__ = threading.Lock()
		
    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func


def sum_n(nn):
    total = 0
    for n in range(1, nn+1):
        total +=n
    return total

def sum_n_smart(n):
    return (n*(n + 1)) /2