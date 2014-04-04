#coding:utf8
import time

def show_time():
    t = time.time()
    int_t = int(t)
    print '---t----',t, '---int_t---',int_t
    return True

# show result
show_time()

