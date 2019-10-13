# -*- coding:utf-8 -*-

#-------------------------------------------------------------------------------
# Note1:       身份证信息验证，根据GB11643-1999《公民身份号码》标准
# Class1：     IdentiyCard
# Author:      WenSan
# Created:     2019-10-09
#-------------------------------------------------------------------------------

import sys

#身份证的验证
class IdentityCard():
    def __init__(self):
        #加权因子
        self.__Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        #校验位换算值
        self.__Ci = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

    def check(self, id):
        if (len(id) != 18):
            return False
        return True
        
    def calculate(self, id):
        idm = map(int, id[0:17])
        sumn = sum(map(lambda x, y: x * y, idm, self.__Wi))
        if id[17] == self.__Ci[sumn % 11]:
            return True
        return False
        
