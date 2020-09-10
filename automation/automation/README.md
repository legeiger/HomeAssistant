## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/automations.png">
</p>

### Attic Fan.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/attic_fan.yaml)__

Automations to turn on/off the attic fan in our bedroom.  I wanted to track how hot it gets in the attic and how much of a difference the attic fan makes. The fan turns on/off based on a input_number so I can easily change the setpoint of the fan.

### Bedroom Fan.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/bedroom_fan.yaml)__

Automations to turn on/off the ceiling fan in our bedroom.  Its a vaulted ceiling and in the summer a lot of hot air gets trapped up there and in the winter the same thing happens to a less notable extent.
* When the HVAC turns on, turn on the fan to circulate the air
* When the HVAC turns off, turn off the fan

### Device Offline.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/deviceoffline.yaml)__

This notification is used to notify me if on of my home automation devices goes offline.  Generally this is someone flipping a switch which cuts the power or a network connectivity issue.
* Notify Me if a Home Automation Device is offline
* Notify Me if a Yeelight is offline
* Notify me if a Zwave device is dead

### Door Security.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/door_security.yaml)__

These automations are used to notify me when a door is opened when no one is home or the garage door is left open when we leave.
* Notify Me if the interior garage door is opened and I am away
* Notify Me if the exterior garage door is opened and I am away
* Notify Me if the front door is opened and I am away
* Notify Me if the back door is opened and I am away
* Notify Me if the garage door is left open when I leave
* Notify Me when the doorbell is pressed and flash a light in the house

### Feed the dog.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/feed_the_dog.yaml)__

These automations are used to turn a light on to signify the dog needs to be fed.  A zwave tilt sensor on the top of the doog food bin automatically signals that the dog has been fed and turns off the light. 
* Turn on Notification Light AM
* Turn on Notification Light PM
* Turn off the Notification Light when the dog food container is opened in the morning
* Turn off the Notification Light When the dog food container is opened in the evening
* Reset everything for the new day

### Freezer Temp.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/freezertemp.yaml)__

Send a notification when the basement deep freezer temperature is above 10 degrees fahrenheit.  

### Garage Light.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/garage_light.yaml)__

Simple automations to turn on an overhead light in the garage when the interior garage door opens.  If the light is left on for 5 mintues it automatically turns off. 
* Turn on the light when the garage door opens
* Turn Off Garage Light After 5 Minutes

### Holiday_Birthday.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/holiday_birthday.yaml)__

Notify me if its is a holiday or birthday. This is based off a data file I keep with holiday's and birthdays.  There is an example of how to setup the data file in the automation file.

### HomeAssistant.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/homeassistant.yaml)__

Some automations for Home Assistant related items.   
* Notify me when Home Assistant starts
* Notify me when Home Assistant is shutting down
* Notify me if an add-on stops working
* Notify me if an add-on update is available
* Manually update some sensor that will no longer auto update
* Send me a notification if my Home Assistant disk gets full
* Notify me if a battery power sensor battery is getting low
* Notify me if there is a new homeassistant version avaialble.

### hvac.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/thermostat.yaml)__

This set of automations is still in its infancy.  I replaced my nest thermostat with a basic Z-wave unit.  Given the presence detection of home assistant and the ability to control the thermostat, I can replace all the nest functions I used and have less reliance on 'the cloud'.

* Set the thermostat to 'away' temperature when everyone has left for the day. (weekdays only)
* Turn the thermostat back to our 'home' temperature at 4:00 to preheat the house so it is warm when my wife arrives home.
* If anyone comes home, turn the temperature back to the 'home' value.
* At bedtime lower the temperature 2 degrees.
* Pre-heat the house for when we wake up.

### Kuleddoubletap.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/kuleddoubletap.yaml)__

* This is a simple automation to toggle our bedside lights when the 'kuled1' switch is double pressed.  The automation looks for the topic set by the double press and toggles the light when it sees it.  This required the following commands to be entered into the tasmota console on that switch. 

```
buttontopic kuledbutton
setoption1 1
setoption11 1
```
* This is an automation that upon double press of the switch evaluates if the LED strip in the room is on or off. If its off, the automation turns the LED strip on to a set color/brightness.  If its on, it starts a sequence to slowly turn off the LED strip overtime.  We use use this as a reading light when my son goes to bed at night.  When leaving the room we can double tap again and the light will slowly transition off.  This reuired the following commands to be entered into the tasmota console on that switch. 

```
buttontopic kuledbutton3
setoption1 1
setoption11 1
```
* This is a simple automation to toggle the automation to turn off the interior garage light after 5 minutes.  Normally that automation keeps the light from remaining on when its not needed, however, sometimes the light should remain on.  A quick double tap of the swtich and it turns off the automation and keeps the light on. This reuired the following commands to be entered into the tasmota console on that switch. 

```
buttontopic kuledbutton5
setoption1 1
setoption11 1
```
### Leaving Home.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_home.yaml)__

An automation to turn off lights and switches when no one is home.  No sense in these being on with no one home.  

### Leaving_Notifications.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/leaving_notifications.yaml)__

These notifications are triggered when I leave my home zone and no one is home.  These send a iOS app notification with an action option to turn the device off. These are primarily a power saving item and are the same framework as the bedtime notification as above. 
* Notify Me if the Desktop PC is left on and no one is home 
* Notify Me if the Media Center is left on and no one is home. This is an effort to automate my 'dumb'TV based on power usage.   

<p align="center"> <img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/iosnotification.jpg"><img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/ios%20action.jpg">
</p>

### Living Room Lamps.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/living_room_lamps.yaml)__

These lamps are the main light source when you walk in through the garage (our primary point of entry).  
* Turn on the living room lamps 30 min before sunset 
* Turn on the living room lamps when somone comes home and its dark out
* Turn off the living room lamps at midnight

### Maintenance Reminders.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/maintenance_reminders.yaml)__

A series of automations that trigger monthly or weekly to help me remember to perform maintenance tasks around the house.  Reminders are sent via e-mail so they stick in my inbox until complete.  
* Trash Day Reminder
* Furnace Filter Reminder
* Dog Flea/Tick/Heartworm Reminder
* Water Softener Reminder
* Remind me to service our whole home humidifier before winter
* Remind me to service our water filter
* Notify me when our county tax bill is available for viewing

### Media Center.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/mediacenter.yaml)__

* When the TV turns on power draw will go above 50 watts, change the amplifier to the TV input. (This also would turn it on if it hasn't been turned on)
* This automation works with an iOS automation in the shortcuts app.  When I open a music app and am at home and connected to my WiFi, the receiver turns on, switches to airplay mode and my phone sets the output to airplay mode.  
<p align="center"> <img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/iosautomation1.png"><img src="https://github.com/SilvrrGIT/HomeAssistant/blob/master/www/iosautomation2.png">
</p>

### Morning Briefing.yaml Automation:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/morning_briefing.yaml)__

* Send my Wife and I a morning e-mail with the weather for the day current and upcoming holidays/birthdays and a random picture of the two of us. The filemove.py file in the main config directory is called by the automation to move a random file from a folder with many pitures to another which is then included in the e-mail. 

### Network.yaml Automation:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/network.yaml)__

* Notify if an item in my netwok has issues (Based on Ubiquiti Unifi Custom Component)
* Notify if the Unifi Gateway has an alert
* Notify if one of my Unifi devices has a firmware update available

### OKtowake.yaml Automations
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/oktowake.yaml)__

This is to mimic a the 'OK to wake' tools you can buy for kids.  If they wake up and see a red light they need to stay in bed, if its green they are OK to leave the bed.  

### Outside Lights.yaml Automations
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/outside_Lights.yaml)__

Some simple automations to turn my outside house lights on at sunset and off at sunrise.  They are initially set to 10% brightness but are set to full brightness if a door is opened, until it is closed.
* Turn on the outside lights at sunset
* Turn off the outside lights at sunrise
* Open back door Increase Brightness

### PC_Security.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/pc_security.yaml)__

* Notify me if the Desktop PC is turned on while away
* Notify me if there is a failed login attempt to the HA front end

### UPS.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/ups.yaml)__

* Notify me if there is a power outage
* Notify me when power is restored


### Zwave.yaml Automations:
__[File Link](https://github.com/SilvrrGIT/HomeAssistant/blob/master/automation/zwave.yaml)__

* When the button is pressed on the zwave remote, toggle the bedside lights