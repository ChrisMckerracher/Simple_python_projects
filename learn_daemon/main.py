import simple_daemon

class ballsack(simple_daemon.simple_daemon):
    #override simple_daemon's run
    def run(self):
        while True:
            pass


ballclass = ballsack()

ballclass.start()
