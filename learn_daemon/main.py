import simple_daemon

class test(simple_daemon.simple_daemon):
    #override simple_daemon's run
    def run(self):
        while True:
            pass


testclass = test()

testclass.start()
