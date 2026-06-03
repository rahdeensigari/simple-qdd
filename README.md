# simple-qdd
A small and cheap quasi-direct driven planetary robotic actuator. It uses an 8:1 planetary reduction powered by a 5010 BLDC drone motor recoiled in star configuration to get ~90KV.

<img width="918" height="920" alt="image" src="https://github.com/user-attachments/assets/bf0173b0-e8c6-4c8c-b125-4ede10e62771" />

This is not the first actuator that I have made, and it certainly won't be the last either. I was aiming to design something small and cheap that could still have a decent amount of power. In order to do this, I have to recoil a small motor that is intended to be used for drones to be more optimal for high load applications.

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

NOTE: It's mainly expensive because a lot of the fastners come in packs with way more of the item then is needed, without counting fasteners, it's $143.65.
