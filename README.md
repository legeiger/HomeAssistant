
<p align="center">
  <img src="https://github.com/home-assistant/home-assistant-assets/blob/master/loading-screen.gif">
</p>

These are the [Home Assistant](https://home-assistant.io/) configuration files used in my Home Assistant (HA) setup. I relied on repositories of other HA users quite a bit when I was getting started for ideas and example code.  Hopefully this repository will help someone else who is getting started. 

# Automations:
A detailed description of each of my automations and a link to the yaml file is located [HERE](https://github.com/SilvrrGIT/HomeAssistant/tree/master/automation#automations)

This is the most important part of Home Assistant!  Remote control and voice commands are nice, however, that is not home automation, just remote control.  Automations should make your life easier, look at what you do every day, the simplest things, and automate them.  To me Home Automation is collecting data about your home and automatically acting based on that data.

# My Home Assistant Setup:

I run my home assistant instance on a [HP ProDesk 600 G1 Desktop Mini PC](https://support.hp.com/us-en/document/c04240180#AbT0) with i5 4590T low power processor. I am running [VMware ESXi](https://my.vmware.com/en/web/vmware/downloads/info/slug/datacenter_cloud_infrastructure/vmware_vsphere/6_7) to allow multiple virtual machines no the same hardware. The base operating system of the VM is [HomeAssistant Operating System](https://github.com/home-assistant/operating-system) and it runs the [Home Assistant ](https://www.home-assistant.io/hassio/installation/) core. It also runs the following add-ons: 

* [Backup to Google Drive](https://github.com/sabeechen/hassio-google-drive-backup)
* [Mosquitto MQTT broker](https://www.home-assistant.io/addons/mosquitto/)
* [Network UPS Tools](https://github.com/hassio-addons/addon-nut)
* [RPC Shutdown](https://www.home-assistant.io/addons/rpc_shutdown/)
* [SSH](https://www.home-assistant.io/addons/ssh/)
* [Samba](https://www.home-assistant.io/addons/samba/)
* [Unifi Controller](https://github.com/hassio-addons/addon-unifi)
* [VScode](https://github.com/hassio-addons/addon-vscode)

I'm currently running [Home Assistant](https://home-assistant.io) version __0.116.2__.

# Connected Devices:

### Cloud Controlled Devices:

* [Google Nest Hub](https://store.google.com/us/product/google_nest_hub) Used for voice commands to turn devices on/off and casting a view with a few switches
* [iPhone 11](https://www.apple.com/iphone-11/) Used for presence detection

### Wifi Connected Devices
* [Xiaomi Yeelight RGBW E27 Smart LED Bulbs](http://www.gearbest.com/smart-lighting/pp_361555.html) *
* [Xiaomi Yeelight E27 Smart LED Bulbs](http://www.gearbest.com/smart-light-bulb/pp_278478.html) *
* [Sonoff Basic (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Wireless-Modified-Low-cost-Compatible/dp/B06WWNBD3Y?ref=ast_p_ei)*
* [Sonoff POW (Flashed with Tasmota)](https://www.amazon.com/Sonoff-Consumption-Monitoring-Appliances-Compatible/dp/B06XSD6PD6?ref=ast_p_ei)*
* [Sonoff TH16 (Flashed with Tasmota)](https://www.amazon.com/Sonoff-TH16-Temperature-Monitoring-Compatible/dp/B06XTNSJ46)*
* [OpenGarage Door Controller ](https://www.amazon.com/OpenGarage-WiFi-enabled-Garage-Door-Opener/dp/B01M4RL0CL)*
* [Kuled WiFi Light Switches (Flashed with Tasmota)](https://www.amazon.com/Required-Wireless-Requires-Schedule-Compatible/dp/B079FDTG7T)*
* [Firefly Electronix Wifi Doorbell](https://www.fireflyelectronix.com/product/wifidoorbell)*
* [Lifx Mini Color Bulb](https://www.lifx.com/collections/lamps-and-pendants/products/lifx-mini-color)*
* [Wifi RGBW LED Strip](https://www.amazon.com/gp/product/B07QBKRCW1)*
* [Reolink E1 Zoom](https://reolink.com/product/e1-zoom/)*
* [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)* with 2 DS18B20 and 1 DHT22 sensors connected

### Zwave Devices
* [Mono Price Z-wave Door Tilt Sensor ](https://www.monoprice.com/product?p_id=11987)
* [GE Z-Wave Plus Hinge Pin Door Sensors ](https://www.amazon.com/GE-Wireless-Attaches-Existing-32563/dp/B01KQDIUAW/)
* [Aeotec Z-wave Range Extender ](https://www.amazon.com/Aeotec-Range-Extender-Z-Wave-repeater/dp/B01M6CKJXC)
* [Dome Miniature, Z-Wave Plus Door/Window Sensor](https://www.amazon.com/Dome-Home-Automation-Miniature-DMWD1/dp/B01JGMZNNG)
* [Go Control Thermostat](https://www.gocontrol.com/detail.php?productId=3)
* [Aeotec Home Energy Meter Gen2 ](https://aeotec.com/z-wave-home-energy-measure/)
* [Zooz Z-wave Dimmer Switches ](https://www.amazon.com/Z-Wave-Switch-Existing-Switches-Add-Ons/dp/B07K37BNMC?th=1)
* [GoControl WA00Z-1 Z-Wave Scene-Controller Wall Switch](https://www.amazon.com/gp/product/B01BKWG9XS/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)

### Hardwired Devices
* [Cyberpower CP1500PFCLCD UPS ](https://www.amazon.com/CyberPower-CP1500PFCLCD-Sinewave-Outlets-Mini-Tower/dp/B00429N19W) used to detect power outages and keep network and HA running in a power outage.
* [Ubiquiti Unifi AP-AC Long Range - Wireless Access Point](https://www.ui.com/unifi/unifi-ap-ac-lr/) used for presence detection
* [Ubiquiti Unifi Security Gateway](https://www.ui.com/unifi-routing/usg/) used for network stats
* [Yamaha RX-V481 Network AV Receiver](https://usa.yamaha.com/products/audio_visual/av_receivers_amps/rx-v481_u/index.html#product-tabs) *

*Block these from external network access and they will still work on your local network with Home Assistant.

# Front End Screen Shots:

## Home
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/rooms.png">
</p>

## Weather
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/weather.png">
</p>

## Data
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/data.png">
</p>

## Switches
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/switches.png">
</p>

## Device Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/devicestatus.png">
</p>

## Home Assistant Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/ha.png">
</p>

## Network Status
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/network.png">
</p>

## Automations
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/automations.png">
</p>

## Cameras
<p align="center">
  <img src="https://raw.githubusercontent.com/SilvrrGIT/HomeAssistant/master/www/cameras.png">
</p>

# UI Based Integrations:
The following integrations are setup in the User Interface (UI) and may be a missing peice as to the full configuration of my HA setup. 

* [Internet Printing Protocol (IPP)](https://www.home-assistant.io/integrations/ipp/)
* [iOS](https://www.home-assistant.io/integrations/ios/)
* [LIFX](https://www.home-assistant.io/integrations/lifx/)
* [MQTT](https://www.home-assistant.io/integrations/mqtt/)
* [NUT](home-assistant.io/integrations/nut/)
* [Samsung TV](https://www.home-assistant.io/integrations/samsungtv/)
* [Speedtest](https://www.home-assistant.io/integrations/speedtestdotnet/)
* [Unifi Controller](https://www.home-assistant.io/integrations/unifi/)
* [Yeelight](https://www.home-assistant.io/integrations/yeelight)
* [ZWave](https://www.home-assistant.io/docs/z-wave/installation)

# A Few Stats On my Setup:
| Tracked Devices | Lights | Helpers | Switches | Automations | Scripts | Sensors | Zwave Devices |
|:---------------:|:------:|:-------:|:--------:|:-----------:|:-------:|:-------:|:-------------:|
|63               |22      |9        |26        |74           |12       |136      |13             | 

# Themes
I created a repository with the theme(s) I use and also a version of the default theme.  It is structured to help you identify the base variables available in Home Assistant to aide in tweaking a theme or creating a new one.  The repository is [HERE](https://github.com/SilvrrGIT/Home-Assistant-Themes)