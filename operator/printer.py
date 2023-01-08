# -- coding: utf-8 --
# @time : 17 Dec, 2022
# @author : unusualroutetaker
# @email : feidaofeidao@outlook.com

def print_data(end_data):
    if end_data['print_check']:
        if end_data['position_check']:
            # print position coordinates
            position_list = end_data["position_data"]
            print('\nPosition Coordinates')
            print('Origin  : ', end='')
            print('[%.3f, %.3f, %.3f]' % (position_list[0][0],
                                          position_list[0][1],
                                          position_list[0][2]))
            for i in range(position_list.shape[0] - 1):
                print('Joint', str(i+1), ': ', end='')
                print('[%.3f, %.3f, %.3f]' % (position_list[i + 1][0], position_list[i + 1][1], position_list[i + 1][2]))

        if end_data['velocity_check']:
            print('\nEnd effector velocity: ')
            print('[%.3f, %.3f, %.3f]' % (end_data['final_velocity'][0], end_data['final_velocity'][1], end_data['final_velocity'][2]))


if __name__ == '__main__':
    print("test printer.py")
    print(1)
