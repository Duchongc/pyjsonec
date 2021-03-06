#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/6 16:21
# @Author  : Anran
# @File    : EscapeCompression.py
# @Function:

class EscapeCompression:
    def __init__(self):
        pass



if __name__ == "__main__":
    from lucpe import Lucpe
    l = Lucpe()
    l.init("/backend-api/get-transfer-info", "POST",
           "{}", "{'complaint_type': '', 'city_id': '', 'order_id': ''}", [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    result = l.get_interface_parameter()
    print(result)