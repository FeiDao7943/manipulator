# -- coding: utf-8 --
# @time : 17 Dec, 2022
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

import numpy as np
import math
import warnings

warnings.filterwarnings("ignore")


class matrix_class:
    def __init__(self):
        self.joint_num = None
        self.pi = math.pi
        self.tiny = 10e-8

    def single_step(self, position_list, data, axis_list):
        """
        calculate the position coordinate for each joint
        :param axis_list: the n*9 list about axis
        :param position_list: an n*3 list to store the positions
        :param data: the 1*4 list about (length, ang_x, ang_y, ang_z)
        :return: the n*3 list to store the positions, the n*9 list about axis
        """

        # joint position
        self.joint_num = position_list.shape[0]
        if self.joint_num == 1:
            current_coordinate = [self.tiny, 0, 0]
        else:
            current_coordinate = position_list[self.joint_num - 1][:]
        changed_coordinate = get_last_vector(current_coordinate,
                                             position_list[self.joint_num - 2][:],
                                             data[0])

        step1 = x_rot(changed_coordinate, data[1])
        step2 = y_rot(step1, data[2])
        step3 = z_rot(step2, data[3])
        output_position = step3 + position_list[self.joint_num - 1]

        output_position = np.array(output_position).reshape(-1, 3)
        position_list = np.append(position_list, output_position, axis=0)

        # axis position

        axis_list_new = np.zeros((9, 3))
        for axis_num in range(9):
            axi_ori = axis_list[self.joint_num-1][axis_num] - position_list[self.joint_num - 1]
            step1 = x_rot(axi_ori, data[1])
            step2 = y_rot(step1, data[2])
            step3 = z_rot(step2, data[3])
            output_axi = step3 + output_position
            axis_list_new[axis_num] = output_axi

        axis_list_new = np.array(axis_list_new).reshape(1, 9, 3)
        axis_list = np.append(axis_list, axis_list_new, axis=0)

        return position_list, axis_list


def get_last_vector(current, last, length):
    """
    move the new link to origin for calculation
    :param current: position of current joint
    :param last: position of last joint
    :param length: the current length of link
    :return: the new position before rotating
    """
    last_vector = current - last
    magnitude = math.pow((math.pow(last_vector[0], 2) +
                          math.pow(last_vector[1], 2) +
                          math.pow(last_vector[2], 2)), 0.5)
    new_coordinate = last_vector * length * (1 / magnitude)
    return new_coordinate


def x_rot(ori, q_in):
    ang = -q_in
    x_mat = [[1, 0, 0],
             [0, math.cos(ang), -math.sin(ang)],
             [0, math.sin(ang), math.cos(ang)]]
    return np.dot(ori, x_mat)


def y_rot(ori, q_in):
    ang = -q_in
    y_mat = [[math.cos(ang), 0, math.sin(ang)],
             [0, 1, 0],
             [-math.sin(ang), 0, math.cos(ang)]]
    return np.dot(ori, y_mat)


def z_rot(ori, q_in):
    ang = -q_in
    z_mat = [[math.cos(ang), -math.sin(ang), 0],
             [math.sin(ang), math.cos(ang), 0],
             [0, 0, 1]]
    return np.dot(ori, z_mat)
