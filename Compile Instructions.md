# CW Voltage-Power Calculator Compile Instructions
Tested with Python 3.11.4

1. Download and unzip the Python source, icon.png, icon.ico, and VERSION files.

   https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/archive/refs/tags/v0.1.1.zip

2. For light mode (leave as-is for dark mode):

   - Comment out lines 209/214 and uncomment lines 211/216
  
   - Change "darkly" to "cosmo" on line 223

3. Install Python dependencies.

   `pip install pywinstyles`
   
   `pip install tkinter`
   
   `pip install ttkbootstrap`

4. Install and launch auto-py-to-exe.

   `pip install auto-py-to-exe`

   `auto-py-to-exe`

5. Set the script location to point to CW Voltage-Power Calculator.py.

6. Set the Onefile option to "One File".

7. Set the Console Window option to "Window Based (hide the console)".

8. Set the option to point to the icon.ico file.

9. Add the icon.png as an additional file, keep the default location of "."

<p align="center">
  <img width="636" height="619" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/auto-py-to-exe1.png">
</p>

11. In the Advanced tab, Windows specific options, set the version file option to point to the "VERSION" file (optional).

<p align="center">
  <img width="636" height="619" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/auto-py-to-exe2.png">
</p>

13. In the Settings tab, under auto-py-to-exe specific options, set the output directory as desired.

14. Press the large blue "CONVERT .PY TO .EXE" button at the very bottom of the form and wait the approximately 60 seconds for the program to compile and generate an executable.

<p align="center">
  <img width="636" height="619" src="https://github.com/DarkArtLabs/CW-Voltage-Power-Calculator/blob/main/Documentation/auto-py-to-exe3.png">
</p>
