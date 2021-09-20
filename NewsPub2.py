from networkzero import *
import random
import time

address = advertise("news1")

# Fake Data
temperatures = range(15, 20)
humidities = range(0, 100)
while True:
    temperature = random.choice(temperatures) + random.random()

    print(temperature)

    humidity = random.choice(humidities)
    send_news_to(address, "temperature", temperature)

    # time.sleep(random.random())

    send_news_to(address, "humidity", humidity)

    # time.sleep(random.random())
