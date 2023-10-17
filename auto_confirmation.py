# -*- coding: utf-8 -*-
# @Time    : 2023/8/2 22:53
# @Author  : Derrick Xu
# @FileName: auto_confirmation.py
# @Abstract: 通过调取高德API的方式获得输入地址的省市区

import requests
import json
import pandas as pd


class AddressTranslation:

    def __init__(self, path, key='cc63e1ebbd766a037400303430ba23d0', save_path='auto_confirmation.xlsx'):
        self.key = key
        self.path = path
        self.save_path = save_path

    # 加载excel内容
    def _load(self):
        sheet = pd.read_excel(io=self.path, header=None)
        return sheet

    def _amap_request(self, row_address):
        url = 'http://restapi.amap.com/v3/geocode/geo?parameters'
        params = {
            'address': row_address,
            'key': self.key,
        }
        new_address = json.loads(requests.get(url, params).content)['geocodes'][0]
        # 仅保存省市区信息
        new_line = {'province': new_address['province'], 'city': new_address['city'],
                    'district': new_address['district'], 'formatted_address': row_address}
        return new_line

        这些就是猜测你的逻辑给你补的，有时候直接能用，有时候稍微改一改就能用，有时候就是个参考，你自己再改改
        好的，我试试，谢谢老师
        你看右小角，那个图标，你输入东西的时候，他会转圈，转圈的时候就是正在生成，生成完了就不转了
        我服了 好神奇   我试试
        可以
        那我退了？
        好的
    # 调取高德API获取位置信息
    def _amap_request(self, row_address):
        url = 'http://restapi.amap.com/v3/geocode/geo?parameters'
        params = {
            'address': row_address,
            'key': self.key,
        }
        new_address = json.loads(requests.get(url, params).content)['geocodes'][0]
        # 仅保存省市区信息
        new_line = {'province': new_address['province'], 'city': new_address['city'],
                    'district': new_address['district'], 'formatted_address': row_address}
        return new_line

    # 持久化存储
    def _persistent_save(self, save_table):
        write = pd.ExcelWriter(self.save_path)  # 新建xlsx文件
        save_table.to_excel(write, sheet_name='Sheet1', index=False)
        write.save()
        return

    # 主函数
    def query_address(self):
        old_table = self._load()
        new_sheet = []
        for line in old_table[0]:
            new_sheet.append(self._amap_request(line))
        self._persistent_save(pd.DataFrame(new_sheet))
        return print('已保存至{}'.format(self.save_path))

AddressTranslation('自动识别.xlsx').query_address()

def query_address(self):
    old_table = self._load()
    new_sheet = []
    for line in old_table[0]:
        new_sheet.append(self._amap_request(line))
    self._persistent_save(pd.DataFrame(new_sheet))
    return print('已保存至{}'.format(self.save_path))
#写一个排序函数，正序
def sort_list(self):
    old_table = self._load()
    new_sheet = []
    for line in old_table[0]:
        new_sheet.append(self._amap_request(line))
    self._persistent_save(pd.DataFrame(new_sheet))
    return print('已保存至{}'.format(self.save_path))
#帮我写个时间序列预测模型
def time_series(self):
    old_table = self._load()
    new_sheet = []
    for line in old_table[0]:
        new_sheet.append(self._amap_request(line))
    self._persistent_save(pd.DataFrame(new_sheet))
    return print('已保存至{}'.format(self.save_path))
# 调取高德API获取位置信息
def _amap_request(self, row_address):
    url = 'http://restapi.amap.com/v3/geocode/geo?parameters'
    params = {
        'address': row_address,
        'key': self.key,
    }
    new_address = json.loads(requests.get(url, params).content)['geocodes'][0]
    # 仅保存省市区信息
    new_line = {'province': new_address['province'], 'city': new_address['city'],
                'district': new_address['district'], 'formatted_address': row_address}
    return new_line
# 加载excel内容
def _load(self):
    sheet = pd.read_excel(io=self.path, header=None)
    return sheet
# 读取excel中的sheet1和sheet3
def _load(self):
    sheet = pd.read_excel(io=self.path, header=None)
    return sheet
# 读取excel中的sheet1和sheet3
def _load(self):
    sheet = pd.read_excel(io=self.path, header=None)
    return sheet
# 读取excel中的sheet1和sheet3
def _load(self):
    sheet = pd.read_excel(io=self.path, header=None)
    return sheet
    #只读取sheet1和3
    def _load(self):
        sheet = pd.read_excel(io=self.path, header=None)
        return sheet
    #只读取sheet1和3

    
    
