"""
Finds Stocks that matches the following Condition
    1) Massive Trading Volume : increasing more than 1,000%
    2) Low PBR : PBR <4 at Massive Trading point
"""

import win32com.client
import time


def check_volume(instStockChart, code): # TODO: Program too slow, use database to improve
    # SetInputValue
    instStockChart.SetInputValue(0, code)
    instStockChart.SetInputValue(1, ord('2'))
    instStockChart.SetInputValue(4, 60)
    instStockChart.SetInputValue(5, 8)
    instStockChart.SetInputValue(6, ord('D'))
    instStockChart.SetInputValue(9, ord('1'))

    # BlockRequest
    instStockChart.BlockRequest()

    num_data = instStockChart.GetHeaderValue(3)
    volumes = [instStockChart.GetDataValue(0, i) for i in range(num_data)]

    average_volume = (sum(volumes) - volumes[0]) / (len(volumes) - 1)

    return True if volumes[0] > average_volume * 10 else False


if __name__ == "__main__":
    instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
    instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    code_list = instCpCodeMgr.GetStockListByMarket(1)
    buy_list = []
    for code in code_list:
        if check_volume(instStockChart, code) == 1:
            buy_list.append(code)
        print(code)
    print(buy_list)