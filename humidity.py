from common import getData, pushData
import time

if __name__ == "__main__":
    while True:
        sensor = 22
        pin = 4
        humidity, temp = getData(sensor,pin)
        pushData(temp,humidity)
        time.sleep(10)