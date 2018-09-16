state = hass.states.get(data['master']).state

if state == 'on':
    hass.services.call('homeassistant', 'turn_off',
                       {'entity_id': data['slave']})
else:
    hass.services.call('homeassistant', 'turn_on', {
                       'entity_id': data['slave']})
