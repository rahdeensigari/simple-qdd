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

# May 17: CAD Work

I found [this](https://grabcad.com/library/mks-odrive-mini-1) model of the motor controller, the step file that they provided did not work, so I had to import the .dwg file they gave into Fusion 360, then export that as a .step for it to work inside of OnShape:

<img width="938" height="793" alt="image" src="https://github.com/user-attachments/assets/35519730-ee0e-4793-888b-a00f0aa326fc" />

The problem now is how I'm going to mount everything. Mounting the motor controller is pretty straight forward, really all I need are some heat-set inserts in the base motor casing that I can use to bolt it directly on. The problem is the motor itself. The CAD is very unclear about this (so is the listing on aliexpress itself) but I'm assuming that the shaft in the center of the bolt circle rotates independently from the bolt holes:

<img width="818" height="879" alt="image" src="https://github.com/user-attachments/assets/88e6d4ed-7d00-459b-911c-e76cd5789410" />

Most motors like this have some sort of bearing around the shaft, but it isn't visible in the CAD, and for some reason all the distributors of the motor seem to be allergic to giving any views other than the front of the motor, so I'm hoping this is actually how it's going to function. The best way to mount this is probably to have some countersunk holes on the bottom of the motor carriage, on the same face as the motor controller's heat-set inserts, where I can fasten the motor with some countersunk bolts. Now, for the motor controller to actually find the position that the motor is in, there needs to be a diametric magnet on the motor shaft that the motor encoder located on the back of the controller can read the position of. A diametric magnet is essentially just a magnet magnetized along its diameter as opposed to its vertical midplane. This allows the encoder to read the position of the poles, which translates to the position of the motor. [McMaster-Carr](https://www.mcmaster.com/products/magnets/direction-of-magnetization~through-diameter/) has a pretty large catalogue of diametric magnets. An 1/8" magnet will fit pretty well on the shaft of the motor. [This](https://www.mcmaster.com/5862K411/) magnet meets my specifications pretty well. It's almost the perfect size to fit directly on the shaft. I designed this small 3D printed part to mount the magnet:

<img width="783" height="677" alt="image" src="https://github.com/user-attachments/assets/0629f334-e15d-4821-a044-f07fc8d4289e" />

I'm going to quickly print it to ensure it can be printed, it's a really small part so I'm concerned if it can be printed or not.

<img width="3072" height="4096" alt="image" src="https://github.com/user-attachments/assets/462f281f-0d91-4fb1-89cd-5871a2e88644" />

It printed, its so small though that I'm not sure if the parts will actually fit? If not, I will just directly glue the magnet on with a template.

I started making a layout sketch of the entire actuator, what I realized was that in order to keep a 2mm distance from the onboard motor controller and the magnet, there would only be around 1mm of clearance for a countersunk hole... which is not enough. To fix this, I'm using [this](https://www.mcmaster.com/5862K202/) magnet instead, which is a 1/16" taller. I have around 2.5mm of room now, which is definitely enough. Here is the sketch so far:

<img width="1162" height="866" alt="image" src="https://github.com/user-attachments/assets/23aba789-3f0c-478f-8171-5519c5fc2c40" />

Alright it's time to talk about the gear reduction I'm using. In the past, I've used 8:1 with success, and I think I'm going to stick with 8:1 for this as well. I would like to use 4 planet gears, but it's not quite possible to get them to fit...

<img width="1170" height="901" alt="image" src="https://github.com/user-attachments/assets/39888982-8ca5-4409-adb1-317c86c85303" />

Which is why I'm just sticking with 3. With some playing around, I found that the perfect size for the gears are:

- Sun: 8 teeth
- Planet: 24 teeth
- Ring: 56 teeth

Using all of that, I made a (VERY!!!!) rough layout sketch of the actuator:

<img width="745" height="582" alt="image" src="https://github.com/user-attachments/assets/8145a717-760f-4def-80a0-04ebc9186660" />
<img width="815" height="801" alt="image" src="https://github.com/user-attachments/assets/97eecfa5-131b-457f-a970-ce96932e7804" />

I very much expect to change all of this later but for now it's good enough for me to start cadding the actual parts :)

**Total time spent: 2.33 hours**
