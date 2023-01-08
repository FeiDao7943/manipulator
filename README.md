# Manipulator

### Example figures

<div align=center>
<img src="https://github.com/FeiDao7943/manipulator/figure/example_1.png" width="400px">
<img src="https://github.com/FeiDao7943/manipulator/figure/example_2.png" width="400px">
</div>

### Usage
>* Code is developed on `Python3.7` in `Mac OS`, mian package such as `matplotlib==3.5.3`, 
`numpy==1.21.6`, `wxpython==4.1.0`, `argparse==1.1` in requirement.txt are required.
>* Run `python main.py` will open the GUI for define the parameters, enter the values and choose the checkboxes.
>* Before click the【Draw】bottom, the parameter should all pass the check. The error place will display in `Hint` label.

### Current shortcomings (will be improved in the future)
>* Fractional input is not currently supported and parameters can only be entered as decimals.
>* The parameters entered last time are not saved, but will be cleared on the next run. This is not very convenient for debuggers.
>* Feel free to point out other shortcomings in `issure` or `email` if possible.

### Update Record
**2023/1/7**
>* Update the only `position` part and GUI design.
>* I'm too sleepy tonight, so I'll come back to refine the code when I'm awake.

**2023/1/8**
>* Update the `velocity` calculation part, only the `torque` part leave.