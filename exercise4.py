from nornir import InitNornir


kp = InitNornir(config_file="config.yaml")

def my_task(task):
    print("wtf?")
    print(task.host.hostname)
    print(task.host.password)
    print(task.host.data)


def main():
    kp.run(task=my_task)

if __name__ == "__main__":
    main()