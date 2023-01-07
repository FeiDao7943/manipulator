# -- coding: utf-8 --
# @time : 17 Dec, 2022
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

import os
import sys
import numpy as np
import math
import warnings

warnings.filterwarnings("ignore")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(os.path.join(ROOT_DIR, 'operator'))

from matrix_calculator import matrix_class

class position_class:
    def __init__(self, data):
        self.data = data
        self.pi = math.pi
        self.joints = data.shape[0]
        self.axis = [[[0, 0, 0], [0.5, 0, 0], [-0.1, 0, 0],
                      [0, 0, 0], [0, 0.5, 0], [0, -0.1, 0],
                      [0, 0, 0], [0, 0, 0.5], [0, 0, -0.1]]]
        self.axis = np.asarray(self.axis)

    def get_position(self, end_data):
        position_list = np.zeros((1, 3))
        rotate_process = matrix_class()
        for joint_num in range(self.joints):
            position_list, self.axis = rotate_process.single_step(position_list,
                                                                  self.data[joint_num][:4],
                                                                  self.axis)

        end_data["axi_data"] = self.axis
        end_data["position_data"] = position_list

        return end_data


if __name__ == '__main__':
    print("test position.py")
    test_data = np.zeros((3, 7))
    for row in range(3):
        test_data[row][0] = 1
        test_data[row][3] = math.pi * 1 / 6

    test = position_class(test_data)
    test.get_position()
