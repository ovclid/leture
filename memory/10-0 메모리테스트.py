import sys
import binascii
import ctypes
import bitstring


def mem_info(var_x, var_name):
    print(f"변수 {var_name} 정보")
    print("---------------------------------------------------------------")
    print("타입 : ", type(var_x))

    if (type(var_x) == int):
        print("값(10진수), 값(16진수) : ", var_x, hex(var_x))

    print("메모리 주소(10진수) : ", id(var_x))
    print("메모리 주소(16진수) : ", hex(id(var_x)))
    print("메모리 주소(16진수) : ", var_x.__str__)

    print("메모리 사이즈(바이트) : ", sys.getsizeof(var_x))
    
    print("메모리 내용(바이트) : ", binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x))))

    hex1 = binascii.hexlify(ctypes.string_at(id(var_x), sys.getsizeof(var_x)))
    hex_string = '0x' + hex1.decode()
    
    print("메모리 내용(비트) : ", bitstring.BitArray(hex_string).bin)


x = 542956

print(f" x = {x} 명령에 의한 {type(x)} 형의 변수 생성 과정")
print("---------------------------------------------------------------")
print(f"1 단계 : 파이썬 객체(PyObject) 하나를 생성")

hex1 = binascii.hexlify(ctypes.string_at(id(x), sys.getsizeof(x)))
print(f"2 단계 : 생성된 객체의 타입 코드를 {hex1[16:28]}로 설정, {type(x)}형 코드")

if (type(x) == int):
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정, 16진수로는 {hex(x)}")
elif (type(x) == str and len(x) == 1):
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정, 16진수로는 {hex(ord(x))}")
else:
    print(f"3 단계 : 생성된 객체의 값을 {x}로 설정")
    

print(f"4 단계 : x라 불리우는 이름 생성")

print(f"5 단계 : x의 id를 생성된 객체의 (시작)주소 {hex(id(x))}로 설정")

print(f"6 단계 : x의 참조 갯수를 1개 증가 {hex1[0:4]} ")
print("---------------------------------------------------------------")

print(f"생성된 {x} 객체 크기 : ", sys.getsizeof(x))
print(f"생성된 {x} 객체 메모리 : ", hex1)

print()
#mem_info(x, 'x')




"""
mem_info(x, 'x')


y = x
mem_info(y, 'y')
if (id(x) == id(y)):
    print(" x and y refer to the same object")

x = x + 1
mem_info(x+1, 'x+1')
if (id(x) != id(y)) :
    print(" x and y refer to the Different object")

z = 10
mem_info(z, 'z')
if (id(y) == id(x)):
    print("y and z point to the Same memory!!")
else:
    print("y and z point to Different memory!!")
"""
