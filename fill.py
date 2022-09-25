save_path = "E:/"

f = open("./macaca_nigra_self-portrait-3e0070aa19a7fe36e802253048411a38f14a79f8-s1100-c50.jpg", "rb").read()

i = 0
while True:
    outF = open(f'{save_path}{i}.jpg', "wb")
    outF.write(f)
    outF.close()
    print(f'Put {i} monkeys in the box', end="\r")
    i += 1