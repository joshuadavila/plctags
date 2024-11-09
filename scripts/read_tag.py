'''
This script uses pylogix module running inside a virtual enviroment to communicate with PLC
'''
from pylogix import PLC

comm = PLC()
comm.IPAddress = '192.168.1.9'
ret = comm.Read('CurrentScreen')
print(ret.Value)
comm.Close()


