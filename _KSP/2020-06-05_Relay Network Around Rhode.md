---
title: Relay Network Around Rhode
collection: KSP
date: 2020-06-05T19:21:53Z
---


![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_001_t1oUqD7.png)

So… Let's start with drawings already!

This mission is a bit different from the other ones. We're not in the Kerbol system anymore! The humanity has colonized a different system, and that's where we are.
We depart from the Planet "Rhode", which is smaller and has a thinner atmosphere than Kerbin.

Usually, I would get the data I need from the KSP wiki, which is incredibly useful for a ton of things. But here, this data doesn't exist, everything needs to be done manually!

So what's the plan here? Put a network of relay satellites on a geostationary orbit of Rhode. This network will enable us to launch unmaned probes in the future around the planet.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_002_3ohwfhr.png)

So, what's a geostationary orbit? It's a geosynchronous orbit with an inclination of 0°. That probably didn't help so it's basically an orbit with a period as long as a day on the planet. Meaning it takes 1 day to do a full rotation. 
The satellite is always staying on the same spot above the planet since the planet is also moving.

With some Wikipedia maths and python scripting, we get the geosync orbit for Rhode, about 3 993km.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_003_QWjvVjt.png)

Ok so we have our geosync orbit.
Now we'd like to know what's the distance between two satellites in our relay network.
If the satellites are too far away, they won't be able to communicate, and that's kinda shitty.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_004_2YIcb08.png)

With some highschool maths we get roughly 6 916km.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_005_ykAyKyx.png)

One of our satellites with 4 antennas.
Why 4 antennas actually? How did I choose that number?

The probes didn't have enough the first time I did my calculations and launched the network. They couldn't communicate, not very helpful.
I decided then to properly get the strength of the vessel and see how many antennas I'd need.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_006_63Ero1d.png)

b00m, easy maths once again.
KSP has a formula that gives us the range of two vessels.
We only have access to the HG-5 antenna for relay purposes for now, so it's gotta be this one.

One antenna is clearly not enough, and 2 are quite enough for what we want to do.
So why 4? Because I had room for more and it's never a bad idea to be able to communicate farther.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_007_RoeJLQx.png)

The resonance orbit is an orbit that's either faster or slower than the circular orbit.
The idea is to detach our satellite at the periapsis (which is our geosync altitude) and then circularize around Rhode.

After one rotation, the main ship will be either forward or backward relatively to the detached probe. With a correct resonance orbit, the satellites will be evenly spaced after each rotation.
Here, we only need to detach 3 satellites, it's quite fast.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_008_zlxYnGt.png)

The circular orbit, in green, is where one satellite has already been detached.
The blue elliptical orbit is our resonance orbit.

It's interesting to note that the orbit here isn't 3 993km but 2 000km. There's actually a moon, Lua, orbiting Rhode at that altitude. It's nearly impossible to get the perfect orbit or period for our probes, the satellites would get captured one day or another by the moon.
I then decided to put the relay at 2 000km. I had to redo the calculations but that's Science! If you trip and fall, just get up and try again.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_009_WErWXFP.png)

So now that we got our period from the previous equations, it could be nice to also have the apoapsis!
The periapsis will be the injection altitude, i.e. geosync orbit (3 993km).

When putting a relay in orbit, the more important thing is the orbital period. All satellites need to have the same so they don't fall out of sync after a few years.
The apoapsis and periapsis can be a bit off, as long as the period is ok.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_010_6S91rfP.png)

Some wikipedia maths later…

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_011_HMYX42Q.png)

The fairing encloses our 3 satellites on top of the command pod where Jeb happily sits.
This thing has way too much Δv for the mission but I wouldn't risk it.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_012_ew53aJt.png)

It's finally time to launch!
Jeb is quite eager :)

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_013_VOk2yy0.png)

Doing a standard gravity turn, slightly lower than on Kerbin because the atmosphere here is quite thin (50km instead of 70).

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_014_1ObHvBF.png)

Circularizing first and then reaching the orbit we need:
Apo: 5 872km
Peri: 3 993km
Period: 2 days, 5 hours, 30 minutes, 38 seconds.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_015_nAw21HP.png)

Detaching our second probe and circularizing shortly after.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_016_GYys9Xp.png)

After some rotations we manage to detach all of our satellites!
The network is in place and works correctly.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_017_9d0rN8m.png)

It's then time for Jeb to go back home.
Slowing his descent, Jeb hopes he won't burn.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_018_jzEexOP.png)

After totally not burning, the stage is detached and it's time to open the chutes.

![](/assets/images/KSP/imgur/BKI3O5d%20-%20Relay%20Network%20Around%20Rhode/imgur_BKI3O5d_019_2hkO8FT.png)

waow, mission success!

I encountered some problems before though as stated:
- not enough antennas on the probes, couldn't communicate
- Lua's on our way and would capture our satellites

Those things needed to be taken into account to reengineer our network.
It took some time but we chose to put that satellite network in orbit, not because it's easy, but because it is hard (well not really, you could eyeball everything and it would still work smh).
