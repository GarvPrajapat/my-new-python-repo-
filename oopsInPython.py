class Car:
    __carCount : int = 0 
    def __init__(self ,brand: str , model: str):
        self.__brand : str = brand
        self.__model : str = model
        Car.__carCount +=1
    
    def getInfo(self) -> None:
        print(f"the brand of car is: {self.__brand}")
        print(f"the model of car is: {self.__model}")
        
    @property
    def Brand(self) -> str:
        return self.__brand
    
    @property
    def Model(self) -> str:
        return self.__model

    def fuelType(self) -> None:
        print("the vehicle use Petrol")

    @staticmethod
    def getCarCount() -> int:
        return Car.__carCount

class ElectricCar(Car):
    def __init__(self, brand , model ,batterySize : int):
        super().__init__(brand,model)
        self.batterySize : int = batterySize
    
    def getInfo(self) -> None:
        super().getInfo()
        print(f"the size of batter is {self.batterySize}")
        

    @property
    def Brand(self) -> str:
        return super().Brand
    
    @property
    def Model(self) -> str:
        return super().Model

    def fuelType(self) -> None:
        print("the vehicle use battery")
    
# ALL car instence/ object of car & and electric car class
lambo : Car = Car("lambo" , "sian")
nano : Car = Car("tata" , "Nano")
tesla : ElectricCar = ElectricCar("tesla" , "SUV", 89)
# ALL car instence/ object of car & and electric car class ends here 

print(isinstance(tesla , Car))