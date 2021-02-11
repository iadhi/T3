# same program but child thread is added
from threading import *
def   f1(x): # It is executed by child thread 't' and x is 10 due to args=[10]
        s=current_thread().name # name of child thread i.e. 'Hyd'
        while   True: # infinite loop
                print(s , ':' , x)
# main thread  executes following stmts
t = Thread(target = f1 , name = 'Hyd', args=[10]) # A new thread is created
t.start()  # thread is ready to execute
print('Num of threads : ',active_count()) # 2 threads are under execution i.e. main thread and child thread 't'
print('press ctrl+break or Fn+b to stop ')
# main thread is dead