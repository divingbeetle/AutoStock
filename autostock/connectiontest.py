# $condna install pywin32
import win32com.client

instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)
# >>> 1 if Connected to CYBOS Plus
