from xmlrpc.server import SimpleXMLRPCServer
import math as m

def sr(i):
    return 2**i
def countCoin(n):
    for _ in range(1):
        p=0
        for i in range(0,n):
            #print(sr(i),i)
            if n>=sr(i):
                p+=1
            else:
                break
    return(p)

server = SimpleXMLRPCServer(("localhost",8000))
print("server listening on 8000")
server.register_function(countCoin,"countCoin")
server.serve_forever()