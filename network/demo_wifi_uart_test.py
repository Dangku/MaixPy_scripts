# Untitled - By: dangku - Thu Nov 28 2019

from fpioa_manager import fm
from machine import UART
from board import board_info
from fpioa_manager import fm

fm.register(board_info.WIFI_TX, fm.fpioa.UART1_TX, force=True)
fm.register(board_info.WIFI_RX, fm.fpioa.UART1_RX, force=True)

uart_A = UART(UART.UART1, 115200,8,0,0, timeout=1000, read_buf_len=4096)

write_str = 'AT\r\n'
uart_A.write(write_str)
for i in range(20):
    uart_A.write(write_str)
    read_data = uart_A.read()
    if read_data:
        read_str = read_data.decode('utf-8')
        print("string = ",read_str)
        if read_str == write_str:
            print("baudrate:115200 bits:8 parity:0 stop:0 ---check Successfully")

uart_A.deinit()
del uart_A

