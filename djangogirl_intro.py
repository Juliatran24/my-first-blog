volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")

def hi2():
    print('Hi there!')
    print('How are you?')

hi2()
def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hi('O')

def hi3(name):
    print('Hi ' + name + '!')

def hi4(name):
    print('Next girl')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for n in girls:
	hi3(n)
	#print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi4(name)
    
for i in range(1, 6):
    print(i)