from nornir import InitNornir

kp = InitNornir(config_file="config.yaml")


def my_task(task):
    print("wtf?")
    print("hostaname: " + task.host.hostname)
    print("password: " + task.host.password)
    print("DNS1: " + task.host.data['dns1'])
    print("DNS2: " + task.host.data['dns2'])


def main():
    kp.run(task=my_task)

if __name__ == "__main__":
    main()