from time import sleep
import paho.mqtt.client as mqtt
from os import system, name
import constants as c


def clear_cmd():
    system('cls' if name == 'nt' else 'clear')
    

def print_out(msg_dict):
    print('|', f'{msg_dict["subject"]}: {msg_dict["val"]}'.center(21), '|')
        
        
def reorder(msgs):
    msgs.sort(key=lambda msg_dict: msg_dict['subject'])


def displays():
    def on_connect(client, userdata, flags, rc):
        client.subscribe([(c.TEMP_TOPIC, 0), (c.HUM_TOPIC, 0), (c.LIGHTS_TOPIC, 0)])

    def on_message(client, userdata, msg):
        if len(client.msgs) == 3:
            clear_cmd()
            reorder(client.msgs)
            print('-' * 25)
            for msg_dict in client.msgs:
                print_out(msg_dict)
                print('-' * 25)
            sleep(c.WAIT)
            client.msgs.clear()
        else:
            msg_dict = dict()
            msg_dict['subject'] = msg.topic.split('/')[0].capitalize()
            val = str(int(msg.payload))
            if msg_dict['subject'] == 'Temperature':
                val += '°C'
            elif msg_dict['subject'] == 'Humidity':
                val += '%'
            elif msg_dict['subject'] == 'Lights':
                val = 'ON' if val == '1' else 'OFF'
            msg_dict['val'] = val
            client.msgs.append(msg_dict)
    
    client = mqtt.Client()
    client.msgs = list()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(c.BROKER['url'], c.BROKER['port'], 60)
    client.loop_forever()
    
    
if __name__ == '__main__':
    displays()
    