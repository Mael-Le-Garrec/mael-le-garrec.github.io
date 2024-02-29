---
title: "WiFi ESP8266 Thermometer"
date: 2024-02-27+T10:30:00+02:00
categories:
  - blog
toc: true
toc_sticky: true
toc_label: "Table of Contents"
tags:
  - Hardware
  - ESP
  - PCB
---


# Introduction

I've been wanting for a while to be able to measure the temperature of my flat
and act upon those measurements, basically making a thermostat.
The commercial options are quite often absolutely not opensource, and often
require to use some kind of cloud when the chosen protocol is WiFi. Of course
I could find something decent in Zigbee but I don't have a HUB.  

<img class="align-left" src="/assets/images/esp01s_thermometer/esp01s.jpg" width="40%"/>

So I decided I'd make that sensor myself. I had always wanted to design my own
PCB, solder the components and get something that works made from the very
basics. The only thing I would not make myself, is the software.

Many current _smart_ devices use a ESP8266 chip, that can handle WiFi. The 
cheapest way to integrate such a chip in a project without too much hassle is
to use a ESP-01S module as pictured just on the right.  
This project is overall very easy as it was intended to be a learning project. 

This post goes over the requirements of the project, the design of the PCB,
a glance over the Home Assistant panel, the design and printing of a case and
then finally the possible improvements that could be made.


## Requirements

The project requirements are:

* Measure kinda accurately the temperature
* Send it over WiFi to Home Assistant via MQTT

An open source firmware called [Tasmota](https://4tasmota.github.io/) can be 
installed on ESP8266 and ESP32 chips, the former being the less capable ones
but also the cheaper. This firmware includes an interface to connect to the
WiFi access point, can transmit over MQTT and most importantly is compatible
with many sensors.
ESP8266 modules can be bought for almost nothing on aliexpress. The ESP-01 is a
classic, I just had to make sure to buy the 01S, which includes 4MB of flash 
size instead of 1MB, as Tasmota wouldn't fit.

There are only a few other parts:

* DS18B20 temperature sensor, quite accurate but many copies around.
  * With its pull-up resistor on the 1-wire bus
* USB-C connector for 5V
* Linear regulator to supply 3.3V to the chip
  * With its two capacitors
* Some connector for the ESP-01S to avoid soldering it

