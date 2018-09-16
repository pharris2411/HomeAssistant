
now = datetime.datetime.now()
hour = now.hour

state = hass.states.get(data['master']).state

if state == 'on':
    hass.services.call('homeassistant', 'turn_off',
                       {'entity_id': data['slave']})
else:

	level = 100

	if hour >= 0 and hour < 8:
		level = 10
	elif hour >= 8 and hour <= 20:
		level = 100
	else:
		level = 50

	data = { "entity_id" : data['slave'], "brightness" : level }
	hass.services.call('light', 'turn_on', data)