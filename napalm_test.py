import napalm 

def main():
    driver_ios = napalm.get_network_driver("ios")
    ios_router = driver_ios(hostname = "10.227.32.1", username = "kpurcell", password = "Cliet32balc!")

    print ("Connecting to IOS Router...")
    ios_router.open()
    print("Checking IOS Router Conenction Status:")
    print(ios_router.is_alive())
    config = ios_router.get_config()
    print(config['running'])
    interfaces = ios_router.get_interfaces()
    print(interfaces)
    vlans = ios_router.get_vlans()
    print(vlans)
    int_ip = ios_router.get_interfaces_ip()
    print(int_ip)
    ios_router.close()
    print("Test Completed")



if __name__ == "__main__":
    main()