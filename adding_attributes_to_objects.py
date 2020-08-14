class Subject():
    def __init__(self):
        print(f"A new object is being created! The object is {self}")
#consistent interface

mathematics = Subject()
chemistry = Subject()

mathematics.school = "Havard"
mathematics.score = 99
mathematics.year = 1990

chemistry.nickname = "Light"

print(mathematics.year)
print(chemistry.nickname)
