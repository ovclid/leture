import sys
import binascii
import ctypes
import bitstring

def obj_hex(obj):
    hex = binascii.hexlify(ctypes.string_at(id(obj), sys.getsizeof(obj)))
    print(sys.getsizeof(obj), hex)
    return hex

x = 10000

obj_hex(x)
#obj_hex('1')

for i in range(10):
    obj_hex(i)
                       
                       
