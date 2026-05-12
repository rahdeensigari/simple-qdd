---
title: "Quasi-Direct Drive Actuator"
author: "Rahdeen Sigari"
description: "A small and cheap quasi-direct driven planetary robotic actuator."
created_at: "2026-05-09"
---

# May 9: Start

Essentially, my goal is to create a full 6-axis robotic arm, but in order to actually do that, I first need to design and build a powerful enough actuator. I've actually already built a similar actuator! Here's a photo:

![image](docs/oldQDD.jpg)

The problem with this actuator however is that it is too large, heavy, and expensive to use for an actual 6-axis arm. That's why I'm making this, a smaller, lighter, and cheaper robotic actuator that can still be powerful enough to effectively drive a robotic arm.

In mechatronics applications like this, it is important for actuators to be somthing called *Quasi-Direct Drive.* Quasi-Direct Drive (QDD) actuators have a high enough gear ratio so that they can actually move signficant loads while not being so powerful that they cannot be backdriven. This is important as QDD actuators like this can completely eliminate the need for external touch sensors, as the actuator cannot overpower the external forces that are put upon it. This allows for the firmware to detect the resulting current increase and register that it has came in contact with an object.

I was kind of inspired to do this by Aaed Musa's [video](https://www.youtube.com/watch?v=GFLa1b1juUo) of him making another robot dog. He actually used something called a capstan drive, which is a gear reduction achieved by using ropes. Instead, I'm using a planetary gearbox, as it's the cheapest option and the best for small reductions like the ones in a QDD actuator as opposed to something like a cylcoidal drive. What really intrested me though was the hardware he used, specifically the motors and motor controllers. He used the following:

- Makerbase XDrive Mini (motor controller)
- TYI 5008 Brushless Motor

For my old actuator, I used:

- ODrive S1 (motor controller)
- Eaglepower LA8308 KV90 (motor)

Don't get me wrong, the hardware I bought worked excellently, but it would absurd to use them for something like a robotic arm, they're just too expensive. Luckily, the amount of power that I got from my old actuator is way more than I need for my eventual goal of making a robotic arm, as long as I keep everything else lightweight. In comparison, without accounting for extra fees, all the hardware that Aaed Musa used is $177.71 cheaper than what I used, which is absolutely absurd. For the record, if I had tried making a 6-axis arm with my old hardware, it would cost $1066.26 more!

I'm happy with the XDrive Mini as my new motor controller, but not entirely confident in the motor's strength, as it has a very high KV, which is not ideal for QDD actuators. The easiest way to fix this without increasing the gear reduction (which would result in it not being QDD anymore) is to recoil the motor stator, which I would like to avoid if I can. Will do some more research later on any alternative motors I can use.

**Total time spent: 1 hour**

# May 10: Researching Motors

I already established the TYI 5008 as good option, but its problem is mainly that it would need me to recoil the stator to decrease its KV (and subsequently increase its torque) to around 100. Ideally, I'm looking for a motor around 50mm in diameter.

- After a bit of research, I found [this](https://www.rctimer.com/rctimer-gbm5010-150t-gimbal-brushless-motor-p0446.html) motor. It is already 90KV, which means that I won't have to recoil it, but the main problem is that it is most likely too small.
- [Here's](https://rctimer.com/rctimer-5010-260kv-multirotor-brushless-motor40mm-shaft-p0132.html) another one, this one still needs to be recoiled, but the KV is much lower so it will be easier. Kind of slow shipping time though.
- [Another one](https://www.aliexpress.us/item/3256808560627221.html). This one is probably the most promising, its cheap, decent shipping time, and similar specs to the TYI 5008, of course, it will, of course, still need recoiling.

Sadly, thats all I could really find. To be honest, all these motors are pretty similar, but I think I'm going to with the third option, which is a 5010 360KV motor off Aliexpress. If I'm being honest, this is mostly because it ships the fastest out of any of the alternatives, all these motors are either 5010 or 5008 motors, and pretty much all of them except for the first one I found need to be recoiled (translation: I chose the third one based off vibes). I might buy one so that I can test its capabilites.

<img width="638" height="428" alt="image" src="https://github.com/user-attachments/assets/31e86f0e-7899-4d02-a923-39ff22e14435" />

**Total time spent: 1 hour**

# May 11: Starting CAD (Or not)

Think I'm ready to start actually planning this out in CAD. I found [this](https://grabcad.com/library/bldc-motor-5010-1) CAD model of the motor, its supbar, but it will do for now:

<img width="1057" height="744" alt="image" src="https://github.com/user-attachments/assets/0dd468e9-d847-4ce6-94c4-073db644d95f" />

Ok I did a bit more research, and I want to slightly pivot my plans. Instead of jumping straight into modeling this in CAD, I want to buy a motor first and see how well it performs, and also see its actual shape in real life as opposed to the, for lack of a better term, shitty CAD model that I found. This will let me actually CAD effectively instead of guessing. I can still work on the actual gearbox and the output stage while I wait. I've got finals to study for though so I'll save that for another time.

**Total time spent: 35 minutes**
