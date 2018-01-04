# -*- coding:utf-8 -*-
import math


class ImpedanceMatching(object):
    def __init__(self):
        self.w = 13.56e6
        self.pi = math.pi
        pass

    def cal_xp(self, data):

        """
        输入测量数据，求解Xp及总电容
        :param data: {Rs, Xs, Rl}，Q：品质因数，Ct：负载电路及匹配网络总电容
        :return: Xp, Ct
        """
        Q = data['Xs']/data['Rs']
        Xp = data['Rl']/Q
        Ct = 1 / (2 * self.pi * self.w * Xp)
        con_data = {'Xp': Xp, 'Ct': Ct}
        return con_data

data = {'Rs': 1.777, 'Xs': 182.858, 'Rl': 11340}
listener_1 = ImpedanceMatching()
print listener_1.cal_xp(data)





