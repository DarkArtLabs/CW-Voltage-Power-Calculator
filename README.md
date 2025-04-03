# CW Voltage-Power Calculator (CWVPC)
Simple GUI application that allows the user to enter a value for either Vpp, Vrms, mW, or dBm of a CW signal and the program will calculate the other three values based on the entered value.

<p align="center">
  <img width="364" height="296" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/GUI1.png">
</p>

<p align="center">
  <img width="364" height="296" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/GUI2.png">
</p>

Features
- Reliable and accurate calculations
- Failsafe design will not report incorrect results
- May enter arbitrary impedance values (defaults to 50 Ohms)
- Able to change any value and re-calculate without clearing form
- Light and dark mode (selectable at compile time)

Ready to be complied using auto-py-to-exe with included icons. Or comment out lines 227/228 and uncomment lines 225/226 to run as a Python script. Or download a precompiled executable. 

Reccomend compiling as "single-file" which results in 30MB executable.
