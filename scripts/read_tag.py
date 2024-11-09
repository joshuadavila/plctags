'''
Uses pylogix module running inside virtual enviroment to communicate with PLC
'''
from pylogix import PLC

def read_tag():

    comm = PLC()
    comm.IPAddress = '10.5.10.120'
    ret = comm.Read('ie_i_150_TestRunning')
    comm.Close()
    return ret.Value



