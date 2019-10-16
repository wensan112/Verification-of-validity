# -*- coding:utf-8 -*-

#-------------------------------------------------------------------------------
# Note:        身份证信息验证，根据GB11643-1999《公民身份号码》标准
# Author:      WenSan
# Created:     2019-10-09
#-------------------------------------------------------------------------------

from datetime import datetime, date, timedelta
import calendar
import re

class IdentityCard:
    def __init__(self, id):
        #加权因子
        self.__wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        #校验位换算值
        self.__ci = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        self.__id = id
        self.__area_id = int(self.__id[0:6])
        self.__birth_year = int(self.__id[6:10])
        self.__birth_month = int(self.__id[10:12])
        self.__birth_day = int(self.__id[12:14])
        self.__sex = int(self.__id[16])
        
    def valid_check(self):
        id_regex = r'^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$'
        if (re.match(id_regex, self.__id)):
            return True
        return False

    def get_birthday(self):
        pass

    def get_sex(self):
        '''
        返回性别：1男，0女
        '''
        return self.__sex

    def get_area(self):
        pass

    def out_id(self):
        '''
        保存最后一位为X
        '''
        if re.findall('X|x', self.__id[17]):
            valid_id = self.__id[:17] + 'X'
        else:
            valid_id = self.__id
        
        return valid_id    
    
    @classmethod
    def calculate(cls, id):
        '''
        计算最后一位校验值，并与输入比较
        正确 True  错误 False
        '''
        idm = map(int, id[0:17])
        sumn = sum(map(lambda x, y: x * y, idm, cls(id).__wi))
        if cls(id).out_id()[17]== cls(id).__ci[sumn % 11]:
            return True
        return False

    def valid_month(self):
        '''
        根据年月计算这月有几天，并查看输入的日是否在这个范围内。
        正确 True  错误 False
        '''
        days_in_month = calendar.monthrange(int(self.__birth_year), int(self.__birth_month))
        if self.__birth_day <= days_in_month[1]:
            return True
        return False
