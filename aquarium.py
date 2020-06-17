Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@VGMasterA 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.

Read the guide

edmond0167
/
aquarium_wed
 Watch 1
 Star 0  Fork 0
 Code
 Issues 0
 Pull requests 0  Actions
 Projects 0
 Wiki
 Security 0
 Insights
Branch: master 
aquarium_wed/aquarium.py  / Jump to 
Find file Copy path
@edmond0167 edmond0167 adding all files barr one
07a01bb 5 minutes ago
1 contributor
66 lines (43 sloc)  1.68 KB
RawBlameHistory
   
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more


import requests
import html
import datetime

# get temperature data from sensor
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/temperature?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print("temperature")
print(r.json()["result"])
temp = ("%.2f" % r.json()['result'])
print()

# get conductivity data from sensor
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/conductivity?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print("conductivity")
cond = ("%.2f" % r.json()['result'])
print(cond)
print()

# get pH data from sensor
r = requests.get('https://api.particle.io/v1/devices/33003b000b47373336373936/ph?access_token=1c476acb47bd0b944a031e2859ef7160e4b72a66')
print("ph")
print(r.json()["result"])
ph = ("%.2f" % r.json()['result'])
print()


# get time
now = datetime.datetime.now()
date_stamp = now.strftime("%Y-%b-%d %H:%M")
print(date_stamp)

# update aquarium.csv file
f = open('/var/www/html/aquarium/aquarium.csv', 'a')
f.write(date_stamp + ',' + temp + ',' + cond + ',' + ph + '\n')
f.close()

# update web page
f = open('/var/www/html/aquarium/aquarium.html','w')
message = """
<h1>Environmental parameters</h1>
<p>The temperature of the aquarium is %s </p>
<p>The conductivity of the aquarium is %s </p>
<p>The ph of the aquarium is %s </p>
<p>Follow these links to see some graphs</p>
<p><a href="aquarium_temp.html">Temperature graph</p>
""" % (html.escape(temp), html.escape(cond), html.escape(ph))

f.write(message)
f.close()
print("finished")




#r = requests.get('https://api.particle.io/v1/devices/330 03b 000 b47 373 336 373 936/temperature?access_token=1c4 76a cb4 7bd 0b9 44a 031 e28 59e f71 60e 4b7 2a6 6')





