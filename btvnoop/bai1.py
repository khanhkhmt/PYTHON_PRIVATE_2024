class Manufacturer :
    def __init__(self , identity : int , location : str): 
        self.identity : int = identity 
        self.location : str = location 
    def describe (self) :
        print ("Identity: " , self.identity , ' - ' , 'Location: ' , self.location)
class Device (Manufacturer) :
    def __init__(self , name : str , price : float, identity, location):
        super().__init__(identity, location)
        self.name : str = name 
        self.price : float = price
    def describe(self):
        print('Name: ' , self.name , '-' , 'Price: ' , self.price)
        super().describe()
        
device1 = Device(name="mouse", price=2.5, identity=9725, location="Vietnam")
device1.describe()
device2 = Device(name="monitor", price=12.5, identity=11, location="Germany")
device2.describe()