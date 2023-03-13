import paho.mqtt.client as mqtt
import constants as c
from random import randint
from time import sleep


def sensors():
    def on_connect(client, userdata, flags, rc):
        client.subscribe(c.LIGHTS_SENSOR)
        
    def on_message(client, userdata, msg):
        client.home_lights = int(not client.home_lights)
        
    client = mqtt.Client()
    client.connect(c.BROKER['url'], c.BROKER['port'], 60)
    client.home_lights = 0
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start()
    while True:
        temp_val = randint(0, 30)
        hum_val = randint(50, 70)
        client.publish(c.TEMP_TOPIC, str(temp_val))
        client.publish(c.HUM_TOPIC, str(hum_val))
        client.publish(c.LIGHTS_TOPIC, str(client.home_lights))
        sleep(c.WAIT)
        
if __name__ == '__main__':
    sensors()
    