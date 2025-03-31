# CW Voltage-Power Calculator (CWVPC)
Simple GUI application that allows the user to enter a value for either Vpp, Vrms, mW, or dBm of a CW signal and the program will calculate the other three values based on the entered value.

<p align="center">
  <img width="364" height="296" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/GUI1.png">
</p>

<p align="center">
  <img width="364" height="296" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/GUI2.png">
</p>

Features
  -Reliable and accurate calculations
  -Failsafe design will not report inccorect results
  -May enter arbitrary impedance value (defaults to 50 Ohms)
  -Able to change any value and re-calculate without clearing form
  -Light and dark mode versions (selectable at compile time)

An real impedance value may be set, with a default of 50 Ohms.

Ready to be complied using auto-py-to-exe with included icons. Edit line 154 to set path of icon.png before compiling.

Reccomend compiling as "single-file" which results in 30kB executible.
