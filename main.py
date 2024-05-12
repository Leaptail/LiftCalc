import lift_func

#line1 syntax error use exit() in terminal
#input in python is always received as string

commandlist = ["test", "lift", "quit"]

userinputted = []

while(True):
    validinput = True
    userinputted = input('What can I help you with today? \n').split()

    if len(userinputted) == 1 and userinputted[0].lower() in commandlist:
        break

    if len(userinputted) == 1 and userinputted[0].lower() in "help":
        
        print("\n\nHere are the commands:")

        for item in commandlist:
            print(item)




#     templist = userinputted.pop(0)

#     for item in templist:
#         if not lift_func.is_number(templist):
#             validinput = False

#     if validinput:
#         break
if userinputted[0].lower() in 'quit':
    exit()

if userinputted[0].lower() in 'test':
    lift_func.test()

if userinputted[0].lower() in 'lift':
    while(True):
        liftvalidinput = True
        liftinputted = input('Input the 4 numbers: liftcoeff, density, velocity, wingarea \n').split()
        
        for item in liftinputted:
            if not lift_func.is_number(item):
                liftvalidinput = False
        
        if len(liftinputted) != 4:
            liftvalidinput = False

        if liftvalidinput:
            break
    
    lift = 0
    lift = lift_func.liftcalc(float(liftinputted[0]), float(liftinputted[1]), float(liftinputted[2]), float(liftinputted[3]))
    print("The Lift is:", lift)

