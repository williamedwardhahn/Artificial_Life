from networkzero import *

address = discover("news1")

while True:
    topic, humidity = wait_for_news_from(address, "humidity")
    print("Humidity is:", humidity)
