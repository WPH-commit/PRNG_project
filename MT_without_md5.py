#import
from time import time

#global var
index = 624
MT = [0]*index

def inter(t):
    return(0xFFFFFFFF & t) #取最后32位

def twister():
    global index
    for i in range(624):
        y = inter((MT[i] & 0x80000000)+(MT[(i + 1) % 624] & 0x7fffffff)) #取第32位 + 取后31位
        MT[i] = MT[(i + 397) % 624] ^ y >> 1
        if y % 2 != 0:
            MT[i] = MT[i] ^ 0x9908b0df #vector
    index = 0

def output():
    global index
    if index == 624:
        twister()
    y = MT[index]
    #tempering
    y = y ^ (y >> 11)
    y = y ^ ((y << 7) & 0x9d2c5680)#10011101001011000101011010000000  
    y = y ^ ((y << 15) & 0xefc60000) #11101111110001100000000000000000
    y = y ^ (y >> 18)
    index = index + 1
    return (y)

def initial(seed):
    MT[0] = seed    
    for i in range(1,624):
        MT[i] = inter(0x6c078965 * (MT[i - 1] ^ MT[i - 1] >> 30) + i)
    return output()

    
    
br = input("请输入随机数产生的范围(用,隔开):")
mi = eval(br.split(',')[0])
ma = eval(br.split(',')[1])
f = open('random-numberstime.txt','w')
for _ in range(1000):    
    so = initial(int(time())) / (2**32-1)
    rd = mi + int((ma-mi)*so)
    f.write(str(rd))
    f.write('\n')
f.close()