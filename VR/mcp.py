# !/usr/bin/python3.7
'''
MCP3008 ,可變電阻
'''

from gpiozero import MCP3008

channel0 = MCP3008 (channel=0, max_voltage=5.0)

if __name__ == '__main__':
    while True:
        print('channel0:', channel0.value)