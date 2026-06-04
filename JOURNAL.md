<img width="1068" height="1011" alt="image" src="https://github.com/user-attachments/assets/f429d06f-565c-44be-ba92-d4482c17a77d" />---
title: "Quasi-Direct Drive Actuator"
author: "Rahdeen Sigari"
description: "A small and cheap quasi-direct driven planetary robotic actuator."
created_at: "2026-05-09"
---

# May 9: Start

Essentially, my goal is to create a full 6-axis robotic arm, but in order to actually do that, I first need to design and build a powerful enough actuator. I've actually already built a similar actuator! Here's a photo:

![image](docs/oldQDD.jpg)

The problem with this actuator however is that it is too large, heavy, and expensive to use for an actual 6-axis arm. That's why I'm making this, a smaller, lighter, and cheaper robotic actuator that can still be powerful enough to effectively drive a robotic arm. Specifically, I want this actuator to be at most 3" in diameter.

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

# May 18: More CAD Work - Physical Parts

I started by starting to make the motor carriage, but I think there's a very big (literally) problem:

<img width="1028" height="980" alt="image" src="https://github.com/user-attachments/assets/37363dc4-3b24-4753-85bd-382495c858fa" />

As you can see, if I want my motor controller to fit nicely in the actuator profile, I would need to make it much larger in diameter. This would cause it go out of my 3" diameter design constraint. So, the only option would be to find a motor controller with a smaller profile. My first thought was the ODrive Mini. It's more expensive, but it has the same features as the XDrive while being much smaller plus having the added benefit of having a GUI. Another option would be to use a cheaper controller like the moteus-c1 that doesn't have UCB-C compatibility, then making my own CAN to USB-C adapter. The price difference is negligible enough that it's not worth doing that though, so I'm just going to pivot to the ODrive Micro for now. Unfortunately this means I'm going to have to change a lot of stuff. Because of this change, I can actually go back to using a 1/16" tall magnet!

Redid the layout sketch:

<img width="731" height="780" alt="image" src="https://github.com/user-attachments/assets/48778d6c-2270-4763-838b-408de8ea3d92" />

Didn't really journal as I was working on it so I'm just to explain what happened. I started modeling the motor carriage. Since there are components under the pcb as well, I had to slightly offset it from the base of the motor carriage. At first, I tried adding a large flange at the bottom, but it still interfered with some of the components at the very edge of the board so I'm just going to use some 3dp spacers instead:

<img width="678" height="555" alt="image" src="https://github.com/user-attachments/assets/c64fbc03-8f11-4111-b112-ae4e1aa4b2fa" />

Like I mentioned before, the motor is mounted by some countersunk bolts right below the motor controller. The actual controller is mounted with [these](https://www.mcmaster.com/94459A769/) heat-set inserts. I also started thinking about the gears. I decided to bring the dp up to 22.5 instead of 20 as that allow the pitch diameter of the ring gear to sit slightly further in from the inside of the motor carriage:

<img width="649" height="381" alt="image" src="https://github.com/user-attachments/assets/0b0e5e1e-b719-4858-b2fb-1b1328e2b979" />

The entire assembly so far:

<img width="1148" height="950" alt="image" src="https://github.com/user-attachments/assets/795ce0a5-3703-4853-ba2c-050ebb7c2cdf" />

**Total time spent: 2.4 hours**

# May 22: CAD Work + Motor Came

Look what came today!

<img width="3072" height="4080" alt="image" src="https://github.com/user-attachments/assets/4af4d4db-c58f-48cd-921a-b74a987cc9e8" />

And, as I guessed, the CAD was inaccurate after all. Turns out where I thought there was just a nub on the bottom on the motor was actually a screw:

<img width="1440" height="1920" alt="image" src="https://github.com/user-attachments/assets/5d634341-f90f-444b-98e1-29b3dc2d3acb" />

Because of this I have to change the magnet mount. I started by updating the CAD to be accurate:

<img width="849" height="620" alt="image" src="https://github.com/user-attachments/assets/7ebb63d3-0ae4-4e3a-933d-03594091e318" />

Then I redid the magnet mount:

<img width="848" height="668" alt="image" src="https://github.com/user-attachments/assets/a180b837-7a2f-4e76-91db-7f1e977a99f1" />

Then, I made the entire casing smaller, there was a lot of unnecessary extra space between the motor and the casing before that I got rid of:

<img width="980" height="959" alt="image" src="https://github.com/user-attachments/assets/6454e0d1-dc98-4263-87b0-b33803c632a8" />

Because of this, I had to increase the dp of the gears again to 27.5. The gears need a carriage to ride on, and said carriage must be able to rotate freely. This can be done using a large bearing with the carriage riding inside. For my old gearbox, I used [these](https://wcproducts.com/products/WCP-1870) bearings, and they worked wonderfully, so I'm going to continue using those. From here I moved on to modelling the sun gear. However, I encountered a problem very quickly:

<img width="794" height="758" alt="image" src="https://github.com/user-attachments/assets/a2349cbe-62c6-4eed-9314-308889b2049d" />

The gear itself was blocking the countsink holes. To fix this, I had to have the gear itself snap fit onto the mounting base. I had to spend a lot of time figuring out a shape that I could actually print. This is what I have right now, but I'm definitely going to have to change it:

<img width="915" height="736" alt="image" src="https://github.com/user-attachments/assets/1389dc21-3155-415a-8b29-12bba9973d0c" />

**Total time spent: 1.75 hours**

# May 24: CAD Work - Sun Gear and Gear Carriage

Continued where I left off yesterday by continuing to iterate on ways to solve the sun gear mounting problem. At first, I tried making another of a snap fit design that could actually reasonably work:

<img width="971" height="784" alt="image" src="https://github.com/user-attachments/assets/f4082810-5fa4-4868-83c3-42d356f3c3b7" />

After trying to print it though, it was evident that this was not the solution, as my printer cannot print in enough detail to be able to create small features like these. Because of this, I decided to pivot to a simpler solution, which was to simply raise the gear up vertically, giving some space to get bolts into:

<img width="683" height="439" alt="image" src="https://github.com/user-attachments/assets/8662b1d0-2ff6-4dbe-ab27-1cf8424436c4" />

Testing it out, I found that because of the low amount of material at the base, it was very easy for the gear to snap off the mounting base. However, I could actually fit the bolts in the holes now with this modification. To increase the strength at the base, I kept some of the original gear profile intact:

<img width="1133" height="666" alt="image" src="https://github.com/user-attachments/assets/759c6e18-e612-45d9-a536-3a6aa6c25f8e" />

Even with this modification, the gear was still weaker than I'm happy with. For the actual production parts I am definitely going to have to use a more ductile material like PETG instead of PLA, but PLA is fine to prototype with for now. I briefly had a problem of the clearance hole for the motor shaft in the sun gear being too short, but this was a quick fix. Here's what the gear looks like on the motor, I couldn't bolt it in because I don't have the right length flathead bolts:

<img width="3072" height="4080" alt="image" src="https://github.com/user-attachments/assets/69e7fd39-989e-4861-af0b-3d864295be43" />

Noticed this, the motor carriage is interfering with the motor. Very easy fix:

<img width="223" height="507" alt="image" src="https://github.com/user-attachments/assets/a938a631-fb8e-43a6-9eb4-f02ad0e04b3b" />

(Forgot to mention this earlier, [this](https://cad.onshape.com/documents/f349bdd78c53f3325055aefc/v/0ca31cd0b35e796be912d9e2/e/53214cbff7d86d5817cf8efb?showReturnToWorkspaceLink=true) is the featurescript I used to generate the gear.

I then started working on the planet gear carrier. First, I made the basic shape. The flange on the bottom rests on top of the x-contact bearing, and the cutout and hole in the middle is to give the sun gear clearance:

<img width="1025" height="521" alt="image" src="https://github.com/user-attachments/assets/73a49a2a-a24e-4e02-bfe5-29095535da03" />
<img width="927" height="265" alt="image" src="https://github.com/user-attachments/assets/098a0e15-b95b-4f12-8688-90e10f32f582" />

**Total time spent: 1.32 hours**

# June 1: CAD Work

First I made the planet gear, just to get a visual of the geometry, I'm going to have to change some things about it.

<img width="659" height="404" alt="image" src="https://github.com/user-attachments/assets/3905b17b-8df1-44a5-9db0-58fcea03b764" />

So here's the problem, there are two solutions to get the gears to move smoothly with as little friction as possible. Either:

- Completely coat the carriage with a lubricant, reducing friction without the need for any external hardware.
- Have the planet gears rotate on bearings to smooth out movement.

Since this project is completely 3D printed, and I want to reduce the mess as much as possible, I'm going to go with the second option of using bearings. Now, here's the actual issue. Bearings are huge. This is what I did in my last gearbox:

<img width="901" height="587" alt="image" src="https://github.com/user-attachments/assets/e1e90b9b-f878-45db-8c1a-5941bf4135d8" />

The problem is that since I'm reducing the size of my gears, I don't have enough space to fit in a full sized ball bearing set into the gear. To fix this, I need to different type of bearing. I did a bit of research, and I stumbled upon [these](https://www.mcmaster.com/5905K496/) needle-roller bearings. They're technically not as smooth as ball bearings, but with some lubrication they should still work perfectly fine.

With these changes in mind, here is the planet gear I created. Unfortunately, this meant upping the heigt of the gears, and by result, the gearbox. Unfortunately just one of the results of using a stock motor for an actuator:

<img width="918" height="819" alt="image" src="https://github.com/user-attachments/assets/cd944dba-8310-410e-9527-4cb98039b1dc" />

I then designed these extrusions on the the gear carrier for the planet gears to rotate on. The hole in the middle is for a heat-set insert.

<img width="1070" height="671" alt="image" src="https://github.com/user-attachments/assets/10af8eea-73fc-441a-acc1-6c615a4dc842" />

Assembly:

<img width="782" height="644" alt="image" src="https://github.com/user-attachments/assets/eef61f56-f472-4e29-bef9-7acf15d02cf8" />

I'm not modelling the motion right now because I really don't care enough to. Here's the ring gear:

<img width="974" height="679" alt="image" src="https://github.com/user-attachments/assets/f22f56f7-e28f-4898-8a83-a1b43e52a7ce" />

Next, I mmade the output plate. There are three countersunk holes to secure it to the gear carriage, as well as three heat set inserts to mount other components to it:

<img width="895" height="679" alt="image" src="https://github.com/user-attachments/assets/53417aab-99f3-4510-8f53-9070ba9cdf97" />

Then, I made a top cover for the entire gearbox. I also added 5 M5 holes to put bolts through in order to secure the entire assembly:

<img width="1033" height="925" alt="image" src="https://github.com/user-attachments/assets/fd3f65b5-6116-4150-97c9-634fb56dc95e" />

I also added these "vents" so I could see the motor turning + because it looked cool:

<img width="625" height="483" alt="image" src="https://github.com/user-attachments/assets/92f47562-7be4-4aa2-a584-7bb115caeb88" />

Also, I added this wire cutout in the base of the motor carriage, without it there's nowhere for the wires to go:

<img width="546" height="582" alt="image" src="https://github.com/user-attachments/assets/ffa8aff8-a27f-4bfd-a771-1a998235760e" />

With that, the CAD is actually complete! I was originally going to add a motor controller cover, but I see no need to as it would just limit my access to the port:

<img width="957" height="927" alt="image" src="https://github.com/user-attachments/assets/ca5b2610-3848-4c12-a962-86e1bb3efe9f" />

**Total time Spent: 3 hours**

# June 2 - Touchups and Docs

Before I start uploading all my documentation, I printed everything out just for a quick fit check.

<img width="4080" height="3072" alt="image" src="https://github.com/user-attachments/assets/cb874c86-a226-438a-afa9-8fe1a8ff0700" />

Some problems I found:

- M3 clearance holes were too small. (For some reason I had it set to close fit?)
- The actual mounting on the motor weren't aligned with the wires. I'm not going to fix this yet because I'm going to be recoiling the motor anyways.
<img width="3072" height="4080" alt="image" src="https://github.com/user-attachments/assets/a9eac9ff-b29f-4c17-b48c-5381561da1e8" />

Everything else seems to be fine right now.

I added some stuff in my README, then created my BOM. A lot of cost comes from the fasteners, but I already have a lot of them.
| Quantity | Name                  | Vendor     | Cost    | Link                                                  | Notes  |
|----------|-----------------------|------------|---------|-------------------------------------------------------|--------|
| 1        | 5010 BLDC Motor       | AliExpress | $19.66  | https://www.aliexpress.us/item/3256808560627221.html  |        |
| 1        | 1.75"" X-Contact      | WCP        | $34.99  | https://wcproducts.com/products/WCP-1870              |        |
| 3        | Needle-Roller Bearing | MCM        | 23.58   | https://www.mcmaster.com/5905K496/                    |        |
| 7        | M3 Heatset x 3.4mm    | MCM        | 8.64    | https://www.mcmaster.com/94459A769/                   | 1 Pack |
| 3        | M3 Heatset x 5.9mm    | MCM        | 5.48    | https://www.mcmaster.com/94459A421/                   | 1 Pack |
| 1        | ODrive Micro          | ODrive     | 89      | https://shop.odriverobotics.com/products/odrive-micro |        |
| 4        | M3x0.5 8mm FH         | MCM        | 5.82    | https://www.mcmaster.com/91294A128/                   | 1 Pack |
| 4        | M3x0.5 5mm FH         | MCM        | 5.57    | https://www.mcmaster.com/91294A125/                   | 1 Pack |
| 3        | M3x0.5 10mm FH        | MCM        | 6.36    | https://www.mcmaster.com/91294A130/                   | 1 Pack |
| 4        | M3x0.5 10mm BH        | MCM        | 7.91    | https://www.mcmaster.com/92095A182/                   | 1 Pack |
| 5        | M4x0.7 50mm SH        | MCM        | 15.85   | https://www.mcmaster.com/91290A186/                   | 1 Pack |
| 5        | M4x0.7 Nuts           | MCM        | 13.25   | https://www.mcmaster.com/94645A101/                   |        |
|          |                       |            | $236.11 |                                                       |        |

**Total Time Spent: 1.25 hours**

# June 3 - Bearing Changes

Ok I got some opinions on using the X-Contact bearing, because it is ridiculously expensive, and I've decided that something that high quality is not needed at all. Instead, I found [this](https://www.aliexpress.us/item/3256807233759178.html) bearing on AliExpress. It's slightly different in size, so I had to change some parts to get it to fit properly, but this is definitely going to be the more cost effective option:

<img width="919" height="775" alt="image" src="https://github.com/user-attachments/assets/21c1541b-01e0-4d37-9c28-a86688b966d4" />

Here is the updated BOM:

| Quantity | Name                  | Vendor     | Cost    | Link                                                  | Notes  |
|----------|-----------------------|------------|---------|-------------------------------------------------------|--------|
| 1        | 5010 BLDC Motor       | AliExpress | $19.66  | https://www.aliexpress.us/item/3256808560627221.html  |        |
| 1        | Output Bearing        | AliExpress | $4.39   | https://www.aliexpress.us/item/3256807233759178.html  |        |
| 3        | Needle-Roller Bearing | MCM        | 23.58   | https://www.mcmaster.com/5905K496/                    |        |
| 7        | M3 Heatset x 3.4mm    | MCM        | 8.64    | https://www.mcmaster.com/94459A769/                   | 1 Pack |
| 3        | M3 Heatset x 5.9mm    | MCM        | 5.48    | https://www.mcmaster.com/94459A421/                   | 1 Pack |
| 1        | ODrive Micro          | ODrive     | 89      | https://shop.odriverobotics.com/products/odrive-micro |        |
| 4        | M3x0.5 8mm FH         | MCM        | 5.82    | https://www.mcmaster.com/91294A128/                   | 1 Pack |
| 4        | M3x0.5 5mm FH         | MCM        | 5.57    | https://www.mcmaster.com/91294A125/                   | 1 Pack |
| 3        | M3x0.5 10mm FH        | MCM        | 6.36    | https://www.mcmaster.com/91294A130/                   | 1 Pack |
| 4        | M3x0.5 10mm BH        | MCM        | 7.91    | https://www.mcmaster.com/92095A182/                   | 1 Pack |
| 5        | M4x0.7 50mm SH        | MCM        | 15.85   | https://www.mcmaster.com/91290A186/                   | 1 Pack |
| 5        | M4x0.7 Nuts           | MCM        | 13.25   | https://www.mcmaster.com/94645A101/                   |        |
|          |                       |            | $205.51 |                                                       |        |

**Total Time Spent: 0.58 hours**

# June 4 - Preparing for Recoiling the Motor

Alright first, I actually forgot to include the [diametric magnet](https://www.mcmaster.com/5862K413/) in the BOM, so I quickly updated it to reflect that.

Here's the updated BOM:

| Quantity | Name                     | Vendor     | Cost    | Link                                                  | Notes  |
|----------|--------------------------|------------|---------|-------------------------------------------------------|--------|
| 1        | 5010 BLDC Motor          | AliExpress | $19.66  | https://www.aliexpress.us/item/3256808560627221.html  |        |
| 1        | Output Bearing           | AliExpress | $4.39   | https://www.aliexpress.us/item/3256807233759178.html  |        |
| 3        | Needle-Roller Bearing    | MCM        | 23.58   | https://www.mcmaster.com/5905K496/                    |        |
| 7        | M3 Heatset x 3.4mm       | MCM        | 8.64    | https://www.mcmaster.com/94459A769/                   | 1 Pack |
| 3        | M3 Heatset x 5.9mm       | MCM        | 5.48    | https://www.mcmaster.com/94459A421/                   | 1 Pack |
| 1        | ODrive Micro             | ODrive     | 89      | https://shop.odriverobotics.com/products/odrive-micro |        |
| 4        | M3x0.5 8mm FH            | MCM        | 5.82    | https://www.mcmaster.com/91294A128/                   | 1 Pack |
| 4        | M3x0.5 5mm FH            | MCM        | 5.57    | https://www.mcmaster.com/91294A125/                   | 1 Pack |
| 3        | M3x0.5 10mm FH           | MCM        | 6.36    | https://www.mcmaster.com/91294A130/                   | 1 Pack |
| 4        | M3x0.5 10mm BH           | MCM        | 7.91    | https://www.mcmaster.com/92095A182/                   | 1 Pack |
| 5        | M4x0.7 50mm SH           | MCM        | 15.85   | https://www.mcmaster.com/91290A186/                   | 1 Pack |
| 5        | M4x0.7 Nuts              | MCM        | 13.25   | https://www.mcmaster.com/94645A101/                   |        |
| 1        | Diametric Encoder Magnet | MCM        | 1.48    | https://www.mcmaster.com/5862K413/                    |        |
|          |                          |            | $206.99 |                                                       |        |

Anyways, while I wait for this to be reviewed on Forge, I'm going to start doing the calculations on how I'm going to recoil the motor. To review, the motor that I have right now is wired in delta-configuration, which means that the three stator windings are connected in a closed loop that resembles a triangle. Each winding's end is connected to the other winding's beginning, making a continuous circuit. There are a couple advantages of a motor wired in delta-configuration. The main advantage of this type of winding is that it can achieve higher torque at higher speeds as opposed to star-configuration coiled motors. Although this sounds like a good thing, these motors are much less efficient at low speeds, as it draws more current for the same amount of torque. Heat generation is also increased with delta-configuration. They are ideal for high-speed applications, but for a robotic actuator, star-configuration is definitely the way to go.

<img width="547" height="370" alt="image" src="https://github.com/user-attachments/assets/fd2efa8b-0a2a-4dfd-b6a8-0824a289a512" />

Star configuration is different as all three stator windings are connected to a central point called the neutral point. This forms a star, or Y shape. The other ends of the windings are then connected to the motor controller. This configuration is better suited to give high effeciency at low speeds, which is why it is ideal for this application. A general rule between delta and star-configuration is that delta-configuration coiled motors have a $\sqrt{3}$x higher KV then star-configuration coiled motors.

<img width="547" height="370" alt="image" src="https://github.com/user-attachments/assets/7d437aaf-3c9a-49ca-ba1d-1ce0d82d7b90" />

Here's the problem: If I were to recoil the motor with the exact same turns/slot and wire awg as the manufacturer, I would get ~208 KV, which is way higher than what I'm aiming for. Luckily, the KV rating is proportional to the number of turns/slot on the motor. So I can divide $208/100$ (100 being the KV I'm aiming for) to get $2.08$.
