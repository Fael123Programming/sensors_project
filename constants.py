CITY = 'Braganca,Braganca,Portugal'
TEMP_TOPIC = 'temperature/' + CITY.lower()
HUM_TOPIC = 'humidity/' + CITY.lower()
LIGHTS_TOPIC = 'lights/status'
LIGHTS_SENSOR = 'lights/sensor'
BROKER = {'url': 'broker.hivemq.com', 'port': 1883}
WAIT = 3