from nornir import InitNornir

kp = InitNornir(config_file="config.yaml")


def my_task(task):
    host= task.host
    print("hostname: " + host.hostname)
    #print({host['dns1']})
    print("DNS1: " + host.data['dns1'])
    print("DNS1: " + host['dns1'])
    print("DNS2: " + host.data['dns2'])


def main():
    kp.run(task=my_task)

if __name__ == "__main__":
    main()