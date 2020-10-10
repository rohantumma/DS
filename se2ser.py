import Pyro4

@Pyro4.expose
class Sq:
    def sq(self,j):
    	return (j**2)


daemon = Pyro4.Daemon()

uri = daemon.register(Sq)

ns = Pyro4.locateNS()

ns.register('obj', uri)
print(uri)

daemon.requestLoop()