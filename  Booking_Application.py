# Booking Application 
def singleton(arg):
    l=[]
    def inner():
        if len(l)==0:
            obj=arg()
            l.append(obj)
        return l[0]
    return inner
@singleton
class arm():
    def __init__(self):
        self.maxtick=150
    def booking(self):
        print(f"Avialiable Tickets are:{self.maxtick}")
        count=int(input("Enter the Tickets to book"))
        if 0<count<=self.maxtick:
            self.maxtick-=count
            print("Booking Sucessfull")
            print(f"aviable tickets are {self.maxtick}")
        else:
            print("Invalid Count of Tickets")
@singleton
class Robot():
    def __init__(self):
        self.maxtick=200
    def booking(self):
        print(f"Avialiable tickets are {self.maxtick}")
        count=int(input("Enter the tickets to book movie"))
        if 0<count<=self.maxtick:
            self.maxtick-=count
            print("Booking Sucesfully done")
            print(f"aviable tickets are {self.maxtick}")
        else:
            print("invalid tickets")
@singleton
class mercel():
    def __init__(self):
        self.maxtick=150
    def booking(self):
        print(f"Avialiable Tickets are:{self.maxtick}")
        count=int(input("Enter the Tickets to book"))
        if 0<count<=self.maxtick:
            self.maxtick-=count
            print("Booking Sucessfull")
            print(f"aviable tickets are {self.maxtick}")
        else:
            print("Invalid Count of Tickets")
def BookMyShow():
    ch=int(input("Select The movie to book the show \n 1. ARM \n 2. Robot \n 3. Mercel \n"))
    if ch==1:
        obj=arm()
        obj.booking()
    elif ch==2:
        obj=Robot()
        obj.booking()
    elif ch==3:
        obj=mercel()
        obj.booking()
    else:
        print("Booking UnSucessfull")

def Paytm():
    ch=
obj=BookMyShow()
obj=BookMyShow()
obj=BookMyShow()

