class Mother:
    def __str__(self):
        return "I am mother"
class Daughter(Mother):
    def __str__(self):
        return "I am dotch"

a = Mother()
b = Daughter()
print(a)
print(b)