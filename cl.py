import xmlrpc.client

with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
    print("For 77 is %s" %str(proxy.countCoin(77)))
    print("For 20 is %s" %str(proxy.countCoin(20)))
    