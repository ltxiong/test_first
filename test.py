#coding:utf8
import time

def show_time():
    t = time.time()
    int_t = int(t)
    print '---t----',t, '---int_t---',int_t
    return True

def print_f():
    print '1'
    

# show result     201707171544
show_time()

print_f()
