# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com
import wx
import time
import numpy as np
import math

def gui_collection(end_data):
    app = wx.App()
    user_input = GUI(end_data)
    user_input.Show()
    app.MainLoop()
    if not user_input.gui_data['check_result'] == 1:
        exit()

    end_data['link_num'] = user_input.gui_data['joint0_check'] + \
                           user_input.gui_data['joint1_check'] + \
                           user_input.gui_data['joint2_check']
    end_data['link_num'] = int(end_data['link_num'])

    total_configuration = np.zeros((end_data['link_num'], 7))
    length_list = np.zeros(end_data['link_num'])
    angle_list = np.zeros((end_data['link_num'], 3))
    angular_velocity_list = np.zeros((end_data['link_num'], 3))

    for joint_num in range(end_data['link_num']):
        length_list[joint_num] = user_input.gui_data[user_input.joint_list[joint_num] + '_length_value']

        angle_list[joint_num][0] = user_input.gui_data[user_input.joint_list[joint_num] + '_angle_x_value']
        angle_list[joint_num][1] = user_input.gui_data[user_input.joint_list[joint_num] + '_angle_y_value']
        angle_list[joint_num][2] = user_input.gui_data[user_input.joint_list[joint_num] + '_angle_z_value']

        angular_velocity_list[joint_num][0] = user_input.gui_data[user_input.joint_list[joint_num] +
                                                                  '_angular_velocity_x_value']
        angular_velocity_list[joint_num][1] = user_input.gui_data[user_input.joint_list[joint_num] +
                                                                  '_angular_velocity_y_value']
        angular_velocity_list[joint_num][2] = user_input.gui_data[user_input.joint_list[joint_num] +
                                                                  '_angular_velocity_z_value']

    total_configuration[:, 0] = length_list
    total_configuration[:, 1:4] = angle_list * end_data['pi']
    total_configuration[:, 4:7] = angular_velocity_list * end_data['pi']

    end_data['configuration_data'] = total_configuration

    end_data['position_check'] = user_input.gui_data['position_check']
    end_data['velocity_check'] = user_input.gui_data['velocity_check']
    end_data['torque_check'] = user_input.gui_data['torque_check']
    end_data['print_check'] = user_input.gui_data['print_check']
    end_data['draw_check'] = user_input.gui_data['draw_check']
    end_data['sub_axis_check'] = user_input.gui_data['sub_axis_check']

    return end_data


class GUI(wx.Frame):
    def __init__(self, end_data):
        self.check_result = -1
        self.joint_list = ['joint0', 'joint1', 'joint2']

        self.parameter_list = ['length', 'angle_x', 'angle_y', 'angle_z',
                               'angular_velocity_x', 'angular_velocity_y', 'angular_velocity_z']
        self.gui_data = {'check_result': 0}
        self.check_list = []
        self.value_list = []
        with open("./define/configuration_save.txt", "r") as config_save:
            safe_data = config_save.readlines()
        for data_count in range(len(safe_data)):
            safe_data[data_count] = str(safe_data[data_count]).replace('\n', '')
            safe_data[data_count] = str(safe_data[data_count]).replace("'", '')
            safe_data[data_count] = str(safe_data[data_count]).replace('True', '1')
            safe_data[data_count] = str(safe_data[data_count]).replace('False', '0')
        wx.Frame.__init__(self, None, title='Parameters', size=(800, 550))
        gui = wx.Panel(self)
        Title = wx.StaticText(gui, label='Manipulator Calculator and Draughtsman', pos=(220, 20))
        Title.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL))
        author = wx.StaticText(gui, label='Author: unusualroutetaker', pos=(550, 50))
        email = wx.StaticText(gui, label='Email: feidaofeidao@outlook.com', pos=(550, 70))

        self.Button_Draw = wx.Button(gui, label='Draw', pos=(420, 480), size=(60, 25))
        self.Button_Check = wx.Button(gui, label='Check', pos=(310, 480), size=(60, 25))
        self.Button_Reset = wx.Button(gui, label='Reset', pos=(710, 480), size=(60, 25))

        Hint = wx.StaticText(gui, label='Hint:', pos=(25, 340))
        self.Hint_word = wx.TextCtrl(gui, pos=(25, 360), size=(400, 110), value='')

        Function = wx.StaticText(gui, label='Function choose:', pos=(450, 340))
        self.position_check = wx.CheckBox(gui, label='Position calculation', pos=(450, 360))
        self.velocity_check = wx.CheckBox(gui, label='Velocity calculation', pos=(450, 380))
        self.torque_check = wx.CheckBox(gui, label='Torque calculation', pos=(450, 400))
        self.print_check = wx.CheckBox(gui, label='Print result', pos=(450, 430))
        self.draw_check = wx.CheckBox(gui, label='Draw figure', pos=(450, 450))
        self.sub_axis_check = wx.CheckBox(gui, label='sub axis draw', pos=(630, 360))

        self.position_check.SetValue(bool(int(safe_data[24])))
        self.velocity_check.SetValue(bool(int(safe_data[25])))
        self.torque_check.SetValue(bool(int(safe_data[26])))
        self.print_check.SetValue(bool(int(safe_data[27])))
        self.draw_check.SetValue(bool(int(safe_data[28])))
        self.sub_axis_check.SetValue(bool(int(safe_data[29])))


        joint_label_x = 25
        joint_joint_begin_y = 100
        joint_joint_value_x = 150
        joint_joint_unit_x = 210

        element_count = 0
        for joint_num in range(len(self.joint_list)):

            joint0_head_label = wx.StaticText(gui, label=('JOINT ' + str(joint_num)),
                                              pos=(joint_label_x, joint_joint_begin_y))
            globals()[self.joint_list[joint_num] + '_check'] = wx.CheckBox(gui, label='',
                                              pos=(joint_label_x + 60, joint_joint_begin_y))
            globals()[self.joint_list[joint_num] + '_check'].SetValue(bool(int(float(safe_data[element_count]))))
            step_y = joint_joint_begin_y + 5
            element_count += 1

            for elements in range(len(self.parameter_list)):
                if not (elements - 1) % 3:
                    step_y += 10
                tem_name_list = [self.joint_list[joint_num] + '_' + self.parameter_list[elements] + '_' + 'label',
                                 self.joint_list[joint_num] + '_' + self.parameter_list[elements] + '_' + 'value',
                                 self.joint_list[joint_num] + '_' + self.parameter_list[elements] + '_' + 'unit']

                if elements == 0:
                    unit = 'm'

                elif elements <= 3:
                    unit = 'pi'

                elif elements > 3:
                    unit = 'pi*rad/s'

                globals()[tem_name_list[0]] = wx.StaticText(gui, label=self.parameter_list[elements],
                                                            pos=(joint_label_x, step_y + 25))
                globals()[tem_name_list[1]] = wx.TextCtrl(gui, pos=(joint_joint_value_x, step_y + 23), size=(60, 25),
                                                          value=str(safe_data[element_count]))
                globals()[tem_name_list[2]] = wx.StaticText(gui, label=unit, pos=(joint_joint_unit_x, step_y + 25))
                step_y += 25
                element_count += 1

            joint_label_x += 250
            joint_joint_value_x += 250
            joint_joint_unit_x += 250

        self.Bind(wx.EVT_BUTTON, self.Button_Draw_click, self.Button_Draw)
        self.Bind(wx.EVT_BUTTON, self.Button_Check_click, self.Button_Check)
        self.Bind(wx.EVT_BUTTON, self.Button_Reset_click, self.Button_Reset)

    def Button_Draw_click(self, event):
        if self.check_result == 1:
            self.gui_data['check_result'] = 1
            with open("./define/configuration_save.txt", "w") as f:
                for joint_num in range(len(self.joint_list)):
                    f.write(str(self.gui_data[self.joint_list[joint_num] + '_check']) + '\n')
                    for elements in range(len(self.parameter_list)):
                        f.write(str(self.gui_data[str(self.joint_list[joint_num] + '_' +
                                          self.parameter_list[elements] + '_' + 'value')]) + '\n')

                f.write(str(self.gui_data['position_check']) + '\n')
                f.write(str(self.gui_data['velocity_check']) + '\n')
                f.write(str(self.gui_data['torque_check']) + '\n')
                f.write(str(self.gui_data['print_check']) + '\n')
                f.write(str(self.gui_data['draw_check']) + '\n')
                f.write(str(self.gui_data['sub_axis_check']) + '\n')


            self.Close()
        if self.check_result == -1:
            self.Hint_word.AppendText('[Error]: Not checked, please run the???Check???first! \n')
        if self.check_result == 0:
            self.Hint_word.AppendText('[Error]: The check procedure did not pass, please correct the \n\t'
                                      'parameters first! \n')

    def Button_Check_click(self, event):
        self.Hint_word.Clear()
        # collect the information from the GUI
        self.gui_data['position_check'] = self.position_check.GetValue()
        self.gui_data['velocity_check'] = self.velocity_check.GetValue()
        self.gui_data['torque_check'] = self.torque_check.GetValue()
        self.gui_data['print_check'] = self.print_check.GetValue()
        self.gui_data['draw_check'] = self.draw_check.GetValue()
        self.gui_data['sub_axis_check'] = self.sub_axis_check.GetValue()

        for joint_num in range(len(self.joint_list)):
            self.gui_data[self.joint_list[joint_num] + '_check'] = \
                globals()[self.joint_list[joint_num] + '_check'].GetValue()
            for elements in range(len(self.parameter_list)):
                self.gui_data[str(self.joint_list[joint_num] + '_' +
                                  self.parameter_list[elements] + '_' + 'value', )] = \
                    globals()[str(self.joint_list[joint_num] + '_' +
                                  self.parameter_list[elements] + '_' + 'value', )].GetValue()

        # start to check
        check_flag_list = []

        # weather value is number
        number_check_flag = 1
        for joint_num in range(len(self.joint_list)):
            for elements in range(len(self.parameter_list)):
                digit = 0
                molecular_value = 0
                denominator_value = 0
                Fractional_flag = 0
                value_str = str(self.gui_data[str(self.joint_list[joint_num] + '_' +
                                                  self.parameter_list[elements] + '_' + 'value', )])
                for letter in range(len(value_str)):
                    if value_str[letter] == '/':
                        Fractional_flag = 1

                if Fractional_flag:
                    frac_correct_flag = 1
                    for letter in range(len(value_str)):
                        if value_str[letter] == '/':
                            digit = letter
                            for letter in range(digit):
                                try:
                                    molecular_value += float(value_str[letter]) * math.pow(10, digit - letter - 1)
                                except:
                                    frac_correct_flag = 0

                            for letter in range(digit + 1, len(value_str)):
                                try:
                                    denominator_value += float(value_str[letter]) * math.pow(10,
                                                                                             len(value_str) - letter - 1)
                                except:
                                    frac_correct_flag = 0

                            if not frac_correct_flag:
                                self.Hint_word.AppendText('[Error]: Value of???' + str(self.joint_list[joint_num] + '_' +
                                                                                     self.parameter_list[
                                                                                         elements] + '???is Error.\n'))
                                number_check_flag = 0

                            else:
                                final_value = molecular_value / denominator_value

                                self.gui_data[str(self.joint_list[joint_num] + '_' +
                                                  self.parameter_list[elements] + '_' + 'value', )] = final_value
                else:
                    try:
                        self.gui_data[str(self.joint_list[joint_num] + '_' +
                                          self.parameter_list[elements] + '_' + 'value', )] = \
                            float(self.gui_data[str(self.joint_list[joint_num] + '_' +
                                                    self.parameter_list[elements] + '_' + 'value', )])
                    except:
                        self.Hint_word.AppendText('[Error]: Value of???' + str(self.joint_list[joint_num] + '_' +
                                                                             self.parameter_list[
                                                                                 elements] + '???is Error.\n'))
                        number_check_flag = 0

        check_flag_list.append(number_check_flag)

        # joint choose check

        joint_check_flag = 0
        total_add = self.gui_data['joint0_check'] + self.gui_data['joint1_check'] + self.gui_data['joint2_check']
        if total_add == 3:
            joint_check_flag = 1
        if total_add == 2:
            if self.gui_data['joint1_check'] and self.gui_data['joint0_check']:
                joint_check_flag = 1
            else:
                self.Hint_word.AppendText('[Error]: Previous joints not enabled \n')
        if total_add == 1:
            if self.gui_data['joint0_check']:
                joint_check_flag = 1
            else:
                self.Hint_word.AppendText('[Error]: Previous joints not enabled \n')
        if total_add == 0:
            self.Hint_word.AppendText('[Error]: No any joints are enabled \n')

        check_flag_list.append(joint_check_flag)

        # length check
        length_check_flag = 1
        for joint_num in range(len(self.joint_list)):
            if self.gui_data[self.joint_list[joint_num] + '_check']:
                if self.gui_data[self.joint_list[joint_num] + '_length_value'] == 0:
                    length_check_flag = 0
                    self.Hint_word.AppendText("[Error]: Link-Length of " + self.joint_list[joint_num] + " can't be zero! \n")
        check_flag_list.append(length_check_flag)

        # total check result
        self.check_result = -1
        for counter in range(len(check_flag_list)):
            self.check_result *= check_flag_list[counter]
        if self.check_result == -1:
            self.check_result = abs(self.check_result)
            self.Hint_word.AppendText('[Done]: Check has passed. Now???Draw???is available! \n')



    def Button_Reset_click(self, event):
        for joint_num in range(len(self.joint_list)):
            if joint_num == 0:
                globals()[self.joint_list[joint_num] + '_check'].SetValue(True)
            else:
                globals()[self.joint_list[joint_num] + '_check'].SetValue(False)

            for elements in range(len(self.parameter_list)):
                if elements == 0:
                    globals()[str(self.joint_list[joint_num] + '_' +
                              self.parameter_list[elements] + '_' + 'value', )].SetLabel('1.0')
                else:
                    globals()[str(self.joint_list[joint_num] + '_' +
                              self.parameter_list[elements] + '_' + 'value', )].SetLabel('0.0')
        globals()['joint0_check'].SetValue(True)
        self.position_check.SetValue(True)
        self.velocity_check.SetValue(True)
        self.torque_check.SetValue(False)
        self.print_check.SetValue(True)
        self.draw_check.SetValue(True)
        self.sub_axis_check.SetValue(True)


if __name__ == "__main__":
    app = wx.App()
    window = GUI()
    window.Show()
    app.MainLoop()

