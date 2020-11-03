import  Pyro4

ns= Pyro4.locateNS()

uri = ns.lookup('obj')

o= Pyro4.Proxy(uri)

j=int(input("Squar of Number:"))
print(o.sq(j))


#start server first pyro4-ns