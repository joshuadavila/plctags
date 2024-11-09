'''
This script uses pylogix module running inside a virtual enviroment to communicate with PLC
'''
from pylogix import PLC

comm = PLC()
comm.IPAddress = '10.5.10.120'
ret = comm.Read('ie_i_150_TestRunning')
print(ret.Value)
comm.Close()


