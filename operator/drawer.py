# -- coding: utf-8 --
# @time : 17 Dec, 2022
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import numpy as np


def draw_fig(end_data, draw_type='None'):
    if end_data['draw_check']:
        position_dic = end_data["position_data"]
        axi_dic = end_data["axi_data"]
        if not draw_type == 'None':
            fig = plt.figure()
            ax = Axes3D(fig)
            ax.set_xlim3d(0, 6)
            ax.set_ylim3d(0, 6)
            ax.set_zlim3d(0, 6)
            if draw_type == 'joint':
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                ax.plot(position_dic[:, 0], position_dic[:, 1], position_dic[:, 2], 'o-', color=[0, 0, 1])
                ax.plot(position_dic[0, 0], position_dic[0, 1], position_dic[0, 2], 'o', color=[1, 0, 0])
                for i in range(axi_dic.shape[0]):
                    ax.plot(axi_dic[i, :, 0], axi_dic[i, :, 1], axi_dic[i, :, 2], '-', color=[0.8, 0.8, 0.2])
            plt.show()


if __name__ == '__main__':
    print("test drawer.py")
    test_position = np.asarray([[0, 0, 0], [1, 1, 1], [1, 1, 0]])
    test_aix = np.asarray([[[1, 1, 3], [1, 1, 1], [3, 3, 1]]])
    test_end_data = {"position_data": test_position, "axi_data": test_aix}
    draw_fig(test_end_data, "joint")



