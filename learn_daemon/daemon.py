import os

class simple_daemon():
    
    def __init__(self):
        pass 
    
    def daemonize(self):
        pid = os.fork()

        if pid > 0:
            #a forks to b, kills a, leaves b
            os._exit(0)
        
        os.setsid()
        os.umask(1) #read only 
        #double forking to ensure child process' parent pid is 1
        pid = os.fork()

        if pid > 0:
            #same as above
            os._exit(0)
    
    def start(self):
        self.daemonize()
        self.run()
    
    def run(self):
        pass

