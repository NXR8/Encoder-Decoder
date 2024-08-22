from random import choice

def ny_encode(data):
    encode = ''
    list1 = ',./'
    list2 = '!@#$%^&*()+=,./][}{'
    list3 = '!@#$%^&*()+=,./123}45]67[890?{'
    list4 = '1234567890'
    
    for i in range(data):
        encode += choice(list1)
        encode += choice(list2)
        encode += choice(list3)
        encode += choice(list4)
      
    return encode
  
while True:
    ny = ny_encode(1)
    print(ny)
    with open('encod.txt', 'a') as f:
        f.write(ny)
        f.write('\n')
        f.close
