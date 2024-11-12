import bluetooth

devices = bluetooth.discover_devices(lookup_names=True, lookup_class=True)
number_of_devices = len(devices)
list_of_devices = {}

for addr, name, device_class in devices:
        for i in range(0, number_of_devices):
            print(f"Device:")
            print("Device Name: %s" % (name))
            print("Device MAC Address: %s" % (addr))
            print("Device Class: %s" % (device_class))
            list_of_devices[f'Имя устройства {i}'] = name
            list_of_devices[f'MAC-Адрес {i}'] = addr
            list_of_devices[f'Класс устройства {i}'] = device_class
            print(list_of_devices)

# Получаем информацию о текущем процессе