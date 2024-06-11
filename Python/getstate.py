# -*-coding:UTF-8-*-
import multiprocessing
from serial.tools import list_ports
import psutil
import serial
import binascii
import multiprocessing as mp
import time


class GetState:
    def __init__(self):
        self.wirerope_move_state = multiprocessing.Value('i')
        self.pos_state = multiprocessing.Value('i')
        # print(self.wirerope_move_state)
        self.lock = mp.Lock()

    def get_from_rs485(self):
        # 创建串口连接
        ser1 = serial.Serial('COM1', 9600,timeout=1)
        ser2 = serial.Serial('COM2', 9600,timeout=1)
        list = [b'0103',b'0103',b'0103',b'0103',b'0104',b'0104',b'0104',b'0104',b'0104',b'0104'
                b'0104',b'0104',b'0104',b'0104',b'0104',b'0105',b'0105',b'0105',b'0105',b'0105'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01',b'01'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                # b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00',b'00'
                b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005'
                b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005',b'0005'
                b'0105',b'0105',b'0105',b'0105',b'0104',b'0104',b'0104',b'0104',b'0104',b'0104'
                b'0104',b'0104',b'0104',b'0104',b'0104',b'0103',b'0103',b'0103',b'0103',b'0103'
                b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003'
                b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003',b'0003'

        ]

        while True:
            for i in list:
                # 从COM1发送数据到COM2
                ser1.write(i)
                # 从COM2接收数据
                data = ser2.read(100)
                data = binascii.unhexlify(data)
                # print(data[0])
                with self.lock:
                    self.wirerope_move_state.value = data[0]
                    self.pos_state.value = data[1]
                    print('state is ',self.wirerope_move_state.value)
            print('一轮了')


        # 关闭串口连接
        ser1.close()
        ser2.close()

    # def get_from_rs485(self,position=6, running_state=5):
    #     '''
    #     获取485串口数据
    #     position: 见协议手册，数据位的的第4位，3是数据位的第一位
    #     running_state:见协议手册，数据位的的第2位，3是数据位的第一位
    #     running_state=4
    #     '''
    #     # 创建串口连接
    #     # todo 修改串口名称 修改读取字节串的位置
    #     # ports = list_ports.comports()[0]
    #     ser = serial.Serial('COM4', 9600, timeout=1)
    #     # port = ports.device
    #     # ser = serial.Serial(port, 9600, timeout=1)
    #
    #     while True:
    #         # 校验码不知道是多少？
    #         # ser.write(b'01 64 00 00 02 00 71 62')
    #         ser.write(bytes.fromhex('0164000002007162'))
    #         data = (ser.read(100))
    #         if data:
    #             with self.lock:
    #                 self.pos_state.value = data[position]
    #                 print(data[position],'位置信息')
    #                 self.wirerope_move_state.value = int(bin(data[running_state])[4])
    #                 # print(bin(data[running_state])[2],'!!!!!!!!!!!!!!!!!!!!!!!!')
    #
    #                 print(self.wirerope_move_state.value,'运行状态')
    #         else:
    #             print('Do receive Response')
    #         # todo 修改串口读取速度
    #         time.sleep(0.01)

        # 关闭串口连接
        ser.close()
    #
    def test(self):
        while True:
            time.sleep(1)
            # print(f'i am {self.wirerope_move_state.value}')




if __name__ == '__main__':
    get_state = GetState()
    processes = [mp.Process(target=get_state.test),
                 mp.Process(target=get_state.get_from_rs485),]
    [setattr(process, "daemon", True) for process in processes]
    [process.start() for process in processes]
    [process.join() for process in processes]



