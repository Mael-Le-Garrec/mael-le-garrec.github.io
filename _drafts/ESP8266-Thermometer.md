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


## Learning PCB Design

I've never designed a PCB in my life and I've always found that quite
frightening, as if you _had_ to be a professional to make them! Turns out it's
quite easy to make something simple and numerous resources exist online.
I started with the tutorials from [DigiKey on youtube](https://www.youtube.com/playlist?list=PL3bNyZYHcRSUhUXUt51W6nKvxx2ORvUQB) to learn how to use KiCad.
[Phil's Lab](https://www.youtube.com/@PhilsLab/search?query=kicad) also has
very high quality videos on designing even complex boards with KiCad.


# Schematics

The circuit is pretty simple. I found it cool to use labels and separate each
component "group" like I did just below.

![](/assets/images/esp01s_thermometer/schematic.svg)

After having worked on other projects, this is dumb. Don't do that. This
circuit is extremely simple, it does not require to separate everything. The
only thing it does, is making the circuit hard to read. A better drawing of
that same circuit is the following, smaller and quickly understandable. I am
sure there's always something to nitpick about but it looks OK to me right now.

![](/assets/images/esp01s_thermometer/schematic_better.svg)


# PCB

<img class="align-right" src="/assets/images/esp01s_thermometer/3d.png" width="20%"/>

The PCB part was quite fun! I am measuring temperature here, and I wanted to
make sure the 3.3V regulator was not going to interfere with the readings. I
empirically tested that the temperature of the regulator was negligible about 5
centimeters away. I also read an interesting [paper from TI](https://www.tij.co.jp/lit/an/snoa967a/snoa967a.pdf?ts=1709260459138&ref_url=https%253A%252F%252Fwww.google.com%252F)
on the guidelines for using a temperature sensor.

I implemented two of those guidelines: removing the ground plane near the sensor and adding a cut in the board to create an isolation island (Fig. 16).
Mounting holes will be used with M3 screws in a case and an additional
connector can be used to plug in a second sensor if needed.
In retrospective, I believe I could have gotten away with a smaller PCB.

An interactive webpage with the PCB, nets, components can be found on [github.io](http://htmlpreview.github.io/?https://raw.githubusercontent.com/Mael-Le-Garrec/ESP-01S_thermometer/v1.0.0/html/board.html)

# Designing a Case

FreeCAD tutorial  


# Final Product

<img src="/assets/images/esp01s_thermometer/case.jpg"/>

<img src="/assets/images/esp01s_thermometer/case_counter.jpg"/>

<img src="/assets/images/esp01s_thermometer/ha.png"/>


# Further Improvements

5.1k
