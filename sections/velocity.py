# -- coding: utf-8 --
# @time :
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

import numpy as np
import math


def jacobian(end_data):
    l_1 = 0
    q_1x = 0
    q_1y = 0
    q_1z = 0
    a_1x = 0
    a_1y = 0
    a_1z = 0

    l_2 = 0
    q_2x = 0
    q_2y = 0
    q_2z = 0
    a_2x = 0
    a_2y = 0
    a_2z = 0

    l_3 = 0
    q_3x = 0
    q_3y = 0
    q_3z = 0
    a_3x = 0
    a_3y = 0
    a_3z = 0
    if end_data['link_num'] >= 1:
        l_1 = end_data['configuration_data'][0][0]
        q_1x = end_data['configuration_data'][0][1]
        q_1y = end_data['configuration_data'][0][2]
        q_1z = end_data['configuration_data'][0][3]
        a_1x = end_data['configuration_data'][0][4]
        a_1y = end_data['configuration_data'][0][5]
        a_1z = end_data['configuration_data'][0][6]
    if end_data['link_num'] >= 2:
        l_2 = end_data['configuration_data'][1][0]
        q_2x = end_data['configuration_data'][1][1]
        q_2y = end_data['configuration_data'][1][2]
        q_2z = end_data['configuration_data'][1][3]
        a_2x = end_data['configuration_data'][1][4]
        a_2y = end_data['configuration_data'][1][5]
        a_2z = end_data['configuration_data'][1][6]
    if end_data['link_num'] >= 3:
        l_3 = end_data['configuration_data'][2][0]
        q_3x = end_data['configuration_data'][2][1]
        q_3y = end_data['configuration_data'][2][2]
        q_3z = end_data['configuration_data'][2][3]
        a_3x = end_data['configuration_data'][2][4]
        a_3y = end_data['configuration_data'][2][5]
        a_3z = end_data['configuration_data'][2][6]

    # x direction
    j_1x = [0, -l_1 * math.sin(q_1x) - l_2 * math.sin(q_1x + q_2x) - l_3 * math.sin(q_1x + q_2x + q_3x),
            l_1 * math.cos(q_1x) + l_2 * math.cos(q_1x + q_2x) + l_3 * math.cos(q_1x + q_2x + q_3x)]
    j_2x = [0, -l_2 * math.sin(q_1x + q_2x) - l_3 * math.sin(q_1x + q_2x + q_3x),
            l_2 * math.cos(q_1x + q_2x) + l_3 * math.cos(q_1x + q_2x + q_3x)]
    j_3x = [0, -l_3 * math.sin(q_1x + q_2x + q_3x), l_3 * math.cos(q_1x + q_2x + q_3x)]
    j_1x = np.asarray(j_1x, dtype=float)
    j_2x = np.asarray(j_2x, dtype=float)
    j_3x = np.asarray(j_3x, dtype=float)
    velocity_z = j_1x * a_1x + j_2x * a_2x + j_3x * a_3x

    # y direction
    j_1y = [l_1 * math.cos(q_1y) + l_2 * math.cos(q_1y + q_2y) + l_3 * math.cos(q_1y + q_2y + q_3y), 0,
            -l_1 * math.sin(q_1y) - l_2 * math.sin(q_1y + q_2y) - l_3 * math.sin(q_1y + q_2y + q_3y)]
    j_2y = [l_2 * math.cos(q_1y + q_2y) + l_3 * math.cos(q_1y + q_2y + q_3y), 0,
            -l_2 * math.sin(q_1y + q_2y) - l_3 * math.sin(q_1y + q_2y + q_3y)]
    j_3y = [l_3 * math.cos(q_1y + q_2y + q_3y), 0, -l_3 * math.sin(q_1y + q_2y + q_3y)]
    j_1y = np.asarray(j_1y, dtype=float)
    j_2y = np.asarray(j_2y, dtype=float)
    j_3y = np.asarray(j_3y, dtype=float)
    velocity_x = j_1y * a_1y + j_2y * a_2y + j_3y * a_3y

    # z direction
    j_1z = [-l_1 * math.sin(q_1z) - l_2 * math.sin(q_1z + q_2z) - l_3 * math.sin(q_1z + q_2z + q_3z),
            l_1 * math.cos(q_1z) + l_2 * math.cos(q_1z + q_2z) + l_3 * math.cos(q_1z + q_2z + q_3z), 0]
    j_2z = [-l_2 * math.sin(q_1z + q_2z) - l_3 * math.sin(q_1z + q_2z + q_3z),
            l_2 * math.cos(q_1z + q_2z) + l_3 * math.cos(q_1z + q_2z + q_3z), 0]
    j_3z = [-l_3 * math.sin(q_1z + q_2z + q_3z), l_3 * math.cos(q_1z + q_2z + q_3z), 0]
    j_1z = np.asarray(j_1z, dtype=float)
    j_2z = np.asarray(j_2z, dtype=float)
    j_3z = np.asarray(j_3z, dtype=float)
    velocity_y = j_1z * a_1z + j_2z * a_2z + j_3z * a_3z

    final_velocity = velocity_x + velocity_y + velocity_z

    # end_data['final_velocity'] = final_velocity + end_data["position_data"][-1][:]
    end_data['final_velocity'] = final_velocity
    print(end_data['final_velocity'])

    return end_data

