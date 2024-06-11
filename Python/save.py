# -*-coding:UTF-8-*-
# import pymysql
import time
import cv2
import os
import psutil
import datetime
import multiprocessing as mp
from getstate import GetState
import Recording


class Record:
    def __init__(self, wirerope_move_state, pos_state, save_path=r'./videos'):
        self.wirerope_move_state = wirerope_move_state
        self.pos_state = pos_state
        self.save_path = save_path
        self.g_bExit = False
        self.pre_pos = pos_state.value
        self.after_pos = -1
        # 判断目录是否存在
        if not (os.path.exists(self.save_path) or os.path.isdir(self.save_path)):
            os.makedirs(self.save_path)

    def save(self):
        # print('i am in')
        # 相机基本参数设置
        Recording.record(self.wirerope_move_state)


    def record_start(self):
        while True:
            if self.wirerope_move_state.value == 1:
                # print('main')
                self.save()
                self.after_pos = self.pos_state.value
                # 获取当前日期
                today = datetime.date.today()
                # 将日期格式化为字符串
                today_str = today.strftime("_%Y-%m-%d")
                name = str(self.pre_pos)+'_to_'+str(self.after_pos)+f'{today_str}'+'.avi'
                if not os.path.isfile(f'./videos/{name}'):
                    os.rename('./videos/temp.avi',f'./videos/{name}')
                self.pre_pos = self.after_pos

            else:
                # todo 修改进程休息时间
                time.sleep(0.01)
                print('i do not record')


# def test(wirerope_move_state):
#     while True:
#         print(f'here{wirerope_move_state.value}')
#         time.sleep(2)


if __name__ == '__main__':
    # # record.save()
    get_state = GetState()
    wirerope_move_state = get_state.wirerope_move_state
    pos_state = get_state.pos_state
    record = Record(wirerope_move_state,pos_state, r'./videos')
    processes = [mp.Process(target=get_state.get_from_rs485),
                 mp.Process(target=record.record_start),
                 # mp.Process(target=test,args=(wirerope_move_state,))
                 ]
    [setattr(process, "daemon", True) for process in processes]
    [process.start() for process in processes]
    [process.join() for process in processes]
