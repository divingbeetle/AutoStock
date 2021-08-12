import win32com.client

instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
# print(instCpStockCode.GetCount())
# >>3410 Stocks (0 to 3409)as index

print(instCpStockCode.GetData(1, 0))
print(instCpStockCode.GetData(0, 0))
print(instCpStockCode.GetData(2, 0))
# 1st arg (0: return code, 1: return name, 2: return FullCode)
# 2nd arg (index)

naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)