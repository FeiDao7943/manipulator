# Manipulator Calculator and Draughtsman

### Example figures

<div align=center>
<img src="https://github.com/FeiDao7943/manipulator/blob/main/figure/example_1.png" width="400px">
<img src="https://github.com/FeiDao7943/manipulator/blob/main/figure/example_2.png" width="320px">
</div>

### Usage
>* Code is developed on `Python3.7` in `Mac OS`, which had test in `Windows 10`.
>* mian package in `requirement.txt` are required, run `pip install -r requirements/requirements.txt` to install.
>* Run `python main.py` will open the GUI for define the parameters, enter the values and choose the checkboxes.
>* Before click the【Draw】bottom, the parameter should all pass the check. The error place will display in `Hint` label.

### Current shortcomings (will be improved in the future)
>* ~~Fractional input is not currently supported and parameters can only be entered as decimals.~~ **(Fixed at 2023/1/10)**
>* ~~The parameters entered last time are not saved, but will be cleared on the next run. This is not very convenient for debuggers.~~
   **(Fixed at 2023/1/9)**
>* Feel free to point out other shortcomings in `issure` or `email` if possible.

### Update Record
**2023/1/7**
>* Update the only `position` part and GUI design.
>* ~~I'm too sleepy tonight, so I'll come back to refine the code when I'm awake.~~ **(Already waking up)**

**2023/1/8**
>* Update the `velocity` calculation part, only the `torque` part leave.

**2023/1/9**
>* Update the function that saving the parameters from the last drawing and you can open and load them directly the next time
you run it, including the value and checkbox. This is friendly for those who need to modify parameters frequently.
>* Fixed an issue where the parameter configuration window could be closed directly to skip the checking session and draw directly.
>* Fixed an issue that some redundant printing for debugging purposes.
>* Test the script in Windows10, and the file `requirements.txt` has added.

**2023/1/10**
>* Update the function that the input value can be type in fraction format, such as `1/3`, `3/4`, `1/12`. 
This is easier to enter for special angles in trigonometric functions.