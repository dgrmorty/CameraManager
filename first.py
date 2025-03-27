from abc import ABC, abstractmethod

# Интерфейс ICamera
class ICamera(ABC):
    @abstractmethod
    def get_information(self):
        pass

# Абстрактный класс CameraItem
class CameraItem(ICamera):
    total_installed = 0

    def __init__(self, camera_type="Unknown", installation_location="Unknown", price=0.0):
        self.camera_type = camera_type
        self.installation_location = installation_location
        self.price = price
        CameraItem.total_installed += 1

    def __del__(self):
        CameraItem.total_installed -= 1

    @abstractmethod
    def show_details(self):
        pass

    def update_price(self, new_price):
        self.price = new_price

    @staticmethod
    def get_total_installed():
        return CameraItem.total_installed

    def get_information(self):
        print(f"Type: {self.camera_type}, Location: {self.installation_location}, Price: {self.price} USD")

# Производный класс DigitalCamera
class DigitalCamera(CameraItem):
    def __init__(self, location, cost, wifi):
        super().__init__("Digital", location, cost)
        self.supports_wifi = wifi

    def show_details(self):
        print("[Digital Camera]", end=" ")
        self.get_information()
        print(f"WiFi Support: {'Yes' if self.supports_wifi else 'No'}")

# Производный класс IPCamera
class IPCamera(CameraItem):
    def __init__(self, location, cost, ip_address):
        super().__init__("IP Camera", location, cost)
        self.ip_address = ip_address

    def show_details(self):
        print("[IP Camera]", end=" ")
        self.get_information()
        print(f"IP Address: {self.ip_address}")

# Главная программа
if __name__ == "__main__":
    SIZE = 20
    cameras = [None] * SIZE  # Создаем массив

    # Добавляем 3 цифровые камеры и 2 IP-камеры
    cameras[0] = DigitalCamera("Entrance", 150, True)
    cameras[1] = DigitalCamera("Yard", 130, False)
    cameras[2] = DigitalCamera("Hallway", 170, True)
    cameras[3] = IPCamera("Street", 200, "192.168.1.10")
    cameras[4] = IPCamera("Parking", 250, "192.168.1.11")

    # Вывод информации о камерах
    print("\nInitial Camera List:")
    for cam in cameras:
        if cam:
            cam.show_details()
            print("--------------------")

    # Заменяем данные 2-й камеры
    cameras[1] = IPCamera("Garage", 180, "192.168.1.12")

    # Обновляем цены
    cameras[0].update_price(160)
    cameras[2].update_price(180)

    # Вывод после обновления
    print("\nAfter price updates:")
    for cam in cameras:
        if cam:
            cam.show_details()
            print("--------------------")

    # Увеличиваем цену 5-й камеры
    cameras[4].update_price(270)

    # Финальный вывод информации
    print("\nFinal Camera List:")
    for cam in cameras:
        if cam:
            cam.show_details()
            print("--------------------")
