import paho.mqtt.client as mqtt
import constants as c
from os import system, name


# def on_connect(client, userdata, flags, rc):
#     client.subscribe(c.LIGHTS_TOPIC)


# def on_message(client, userdata, msg):
#     client.home_lights = str(int(msg.payload))
#     client.disconnect()
    

# def get_home_lights_status():
#     client = mqtt.Client()
#     client.on_connect = on_connect
#     client.on_message = on_message
#     client.connect(c.BROKER['url'], c.BROKER['port'], 60)
#     client.loop_forever()
#     return client.home_lights


def send_toggle_signal():
    client = mqtt.Client()
    client.connect(c.BROKER['url'], c.BROKER['port'], 60)
    client.loop_start()
    client.publish(c.LIGHTS_SENSOR, 'toggle')


def clear_cmd():
    system('cls' if name == 'nt' else 'clear')
    
    
if __name__ == '__main__':
    while True:
        clear_cmd()
        print('-' * 100)
        print('Toggle Home Lights'.center(100))
        print('-' * 100)
        opt = input('ENTER to toggle (0 to finish): ')
        if opt == '0':
            break
        send_toggle_signal()
    clear_cmd()
    