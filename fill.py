save_path = "E:/"

f = open("./macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s1100-c50.jpg", "rb").read()

def inttoname(num):
    i = 0
    n = num
    ret = ""
    while True:
        if 16**i > num:
            break
        i += 1
    for _ in range(0, i):
        ret += chr((n&0xf)+101)
        print(ret)
        n = n>>1
    return ret

i = 83344
while True:
    outF = open(f'{save_path}{i}.jpg', "wb")
    outF.write(f)
    outF.close()
    print(f'Put {i} monkeys in the box', end="\r")
    i += 1