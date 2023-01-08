# -- coding: utf-8 --
# @time : 17 Dec, 2022
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

"""
Hints:
-i https://pypi.tuna.tsinghua.edu.cn/simple some-package
pip freeze > requirements/requirements.txt
"""

import wx
import os
import sys
import argparse
import math
import time
import warnings
warnings.filterwarnings("ignore")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = BASE_DIR
sys.path.append(os.path.join(ROOT_DIR, 'sections'))
sys.path.append(os.path.join(ROOT_DIR, 'define'))
sys.path.append(os.path.join(ROOT_DIR, 'operator'))

from gui import gui_collection
from configuration import configuration_class
from position import position_class
from velocity import jacobian
from drawer import draw_fig
from printer import print_data

parser = argparse.ArgumentParser()
parser.add_argument('--pi', type=float, default=math.pi, help='number of joints')
parser.add_argument('--other', action='store_true', help='calculate position')
FLAG = parser.parse_args()


def main_calculation():
    """
    the main calculation code
    :return: All calculation data as a dictionary
    """

    end_data = {"pi": FLAG.pi}

    """collect the configuration data from GUI"""
    # configuration_collection = configuration_class(end_data)
    # end_data = configuration_collection.get_configuration(end_data)
    end_data = gui_collection(end_data)

    """position calculation"""
    position_calculation = position_class(end_data["configuration_data"])
    end_data = position_calculation.get_position(end_data)

    """velocity calculation"""
    end_data = jacobian(end_data)

    """print part"""
    print_data(end_data)

    """drawing part"""
    draw_fig(end_data)


if __name__ == '__main__':
    main_calculation()





