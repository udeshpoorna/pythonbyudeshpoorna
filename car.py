car = ""
engine = False
while car!="quit":
    car = input(">").lower()
    if car == "help":
        print ('''
start - to start the car
stop - to stop the car
quit - to quit''')
    elif car == "start":

        if engine is True:
         print("the car is already started")
        else:
            print("the car is started")
            engine = True

    elif car == "stop":
        if engine is False:
         print("the car is not yet started")
        else:
         print("tha car is stopped")
         engine = False
    else :
        break

