class Guitar():
    def __init__(self, wood):
        self.wood = wood



acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)

baritone = Guitar("Alder")
print(baritone.wood)

print(acoustic)
print(baritone)

a = [1, 2, 3]
b = [1, 2, 3]

class Musical():
    def __init__(self, name):
        self.name = name
        
        
rent = Musical("Rent")
mormon = Musical("Book of Mormon")
chicago = Musical("Chicago")

#Declare a Skyscraper class that accepts name and year parameters. 

# In the initialization process for an object, assign the name parameter to a name attribute 
# and the year parameter to a year attribute.

# Instantiate a Skyscraper object with the name “Empire State Building”  and the year 1931. 
# Assign it to a “empire" variable.

# Instantiate a Skyscraper object with the name “One World Trade Center” and the year 2014. 
class Skyscraper():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
empire = Skyscraper("Empire State Building", 1931)
wtc = Skyscraper("One World Trade Center", 2014)

# Assign it to a “wtc" variable.

