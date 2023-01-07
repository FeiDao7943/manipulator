# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

import numpy as np
import math
import warnings
warnings.filterwarnings("ignore")


class configuration_class:
    def __init__(self, link_num):
        """
        Prepare the parameters for configuration collection
        :param link_num: number of hte links of manipulator
        """
        self.pi = math.pi*1
        self.link_num = link_num

    def get_configuration(self, end_data):
        """
        Collect the configuration of the manipulator
        :return: n*7 list, which are n*(length, ang_x, ang_y, ang_z, an_ve_x, an_ve_y, an_ve_z)
        """

        """joint 0"""
        length_0 = 3

        angle_0x = self.pi * 0
        angle_0y = self.pi * 0
        angle_0z = self.pi * 1 / 6

        angular_velocity_0x = self.pi * 0
        angular_velocity_0y = self.pi * 0
        angular_velocity_0z = self.pi * 0

        """joint 1"""
        length_1 = 2

        angle_1x = self.pi * 0
        angle_1y = self.pi * 0
        angle_1z = self.pi * 1 / 3

        angular_velocity_1x = self.pi * 0
        angular_velocity_1y = self.pi * 0
        angular_velocity_1z = self.pi * 0

        """joint 2"""
        length_2 = 1

        angle_2x = self.pi * 0
        angle_2y = self.pi * 0
        angle_2z = self.pi * 1 / 2

        angular_velocity_2x = self.pi * 0
        angular_velocity_2y = self.pi * 0
        angular_velocity_2z = self.pi * 0

        """pack"""
        length_list = np.zeros(self.link_num)
        angle_list = np.zeros((self.link_num, 3))
        angular_velocity_list = np.zeros((self.link_num, 3))
        total_configuration = np.zeros((self.link_num, 7))
        xyz_list = ["x", "y", "z"]

        for link_nums in range(self.link_num):
            length_list[link_nums] = locals()["length_" + str(link_nums)]
            for column_xyz in range(3):
                name_of_angle_data = str("angle_" + str(link_nums) + xyz_list[column_xyz])
                angle_list[link_nums][column_xyz] = locals()[name_of_angle_data]
                name_of_angular_velocity_data = str("angular_velocity_" + str(link_nums) + xyz_list[column_xyz])
                angular_velocity_list[link_nums][column_xyz] = locals()[name_of_angular_velocity_data]

        total_configuration[:, 0] = length_list
        total_configuration[:, 1:4] = angle_list * end_data['pi']
        total_configuration[:, 4:7] = angular_velocity_list * end_data['pi']

        # print(total_configuration)
        end_data["configuration_data"] = total_configuration
        return end_data


if __name__ == '__main__':
    print("test configuration.py")
    test = configuration_class(3)
    test.get_configuration()
