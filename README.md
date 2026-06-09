# simple-qdd
A small and cheap quasi-direct driven planetary robotic actuator. It uses an 8:1 planetary reduction powered by a 5010 BLDC drone motor recoiled in star configuration to get ~100KV.

<img width="918" height="920" alt="image" src="https://github.com/user-attachments/assets/bf0173b0-e8c6-4c8c-b125-4ede10e62771" />

This is not the first actuator that I have made, and it certainly won't be the last either. I was aiming to design something small and cheap that could still have a decent amount of power. In order to do this, I have to recoil a small motor that is intended to be used for drones to be more optimal for high load applications.

If you are interested in building this yourself, the BOM below is a good starting place for getting materials, but anything will similar specifications will work just as well. You can download the CAD files either directly from the Onshape document (below) or from the files listed in the CAD folder.

[CAD](https://cad.onshape.com/documents/57a8ef0242364670953218e9/w/659145295f694f0fa79f9cef/e/7b9566cf06dc05a88ad73bb1)

# BOM

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

NOTE: A bulk of the price is because a lot of the fastners come in packs with way more of the item then is needed.

# Assembly

<img width="2547" height="3296" alt="Main (1)" src="https://github.com/user-attachments/assets/f1f0638a-0bb7-436c-8d74-37f7243cceee" />
<img width="995" height="768" alt="image" src="https://github.com/user-attachments/assets/98c6e246-422b-4c48-b328-1ab64ddc8545" />

Use these exploded and section views as well as the CAD link above while assembling. Some important notes, assemble the gear carriage, the bottom retention flange, and the bearing at once before putting it into the motor carriage. Make sure the motor is fully installed in the carriage and the sun gear is installed on the motor before inserting the bearing and gear carriage assembly. Make sure the heat-set inserts in the gear carriage are fully inserted, or else the countersunk bolts won't fit correctly.

If you are going to recoil the motor, use 26 AWG magnet wire with 46 turns-per-slot if you want to get to the same KV I used. Use the following diagram when you are recoiling:
<img width="700" height="700" alt="image" src="https://github.com/user-attachments/assets/df721449-4257-437d-b8e5-80618dd2673c" />
