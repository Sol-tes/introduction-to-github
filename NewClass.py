class MyRouter(object):
    "This is a class that"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)


new_router1 = MyNewRouter("new1", "1800", "11111", "12.2", "10")

print(new_router1.print_router("adafsfds"))
print(new_router1.print_new_router("fdgdgfd"))