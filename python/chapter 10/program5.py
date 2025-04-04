# write a class train which has  mathods to book a tickit ,get status (no of seats) and get faere information
# of the train running under indian raliways

from random import randint
class train:
   
   def __init__(self, trainNo):
       self.trainNo = trainNo
           
    def greatbook(self, fro, to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print(f"train no: {self.trinNo} is running on time")
    
    def getFare(self, fro ,to):
        print(f"tickit is fare in train no: {self.trainNo} from {fro} to {to} is
        {randit(222,5555)}")
        
        
t = train(12349)
t.book("lahore","layyah") 
t.getstatus("pandi", "layyah")
t.getFare("karachi", "layyah")       