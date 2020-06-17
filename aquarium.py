import requests
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/temperature?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print(r)

