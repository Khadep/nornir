import time
import random
from nornir import InitNornir

nr = InitNornir(config_file="config.yaml")

def main():
    #nr = InitNornir()
    # for x in nr.inventory.hosts:
    #     print (1)
    #     print (x.platform)
    #nr.run(task=my_task)
    #group = nr.inventory.hosts['localhost']
    #for x in group:
    #    print (1)
    #    print (x.platform)
    group = nr.inventory.hosts
    for x in list(group):
        print ("hostname : " + nr.inventory.hosts[x].hostname)
        print ("groups : " + str(nr.inventory.hosts[x].groups))
        print ("platform : " + nr.inventory.hosts[x].platform)
        print ("username : " + nr.inventory.hosts[x].username)
        print ("password : " + nr.inventory.hosts[x].password)
        print ("port : " + str(nr.inventory.hosts[x].port))
       
    

        

    #    print(x)
    #print (task.host.hostname)
    #print (task.host.groups)
    #print (task.host.platform)
    #print (task.host.username)
    #print (task.host.password)
    #print (task.host.port)

if __name__ == "__main__":
    main()