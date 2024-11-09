'''
receive command line script arguments and use them to communicate with PLC

read_tag(tag_name)
write_tag(tag_name, value)

'''

import sys
from plc_api import read_tag, write_tag

# get total arguments
n = len(sys.argv)

# if arguments number is two then we are reading tag from PLC
if n == 2:

	comm = PLC()
    comm.IPAddress = '10.5.10.120'
    ret = comm.Read('MyTagName')
    #print(ret.TagName, ret.Value, ret.Status)
    return(ret)

# if arguments number is three then we are writing tag value to PLC
elif n == 3:

	comm = PLC()
    comm.IPAddress = '10.5.10.120'
    ret = comm.Read('MyTagName')
    #print(ret.TagName, ret.Value, ret.Status)
    return(ret)

else:

	print("wrong arguments")



'''
# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
'''