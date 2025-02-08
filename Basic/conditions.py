""" not , in , not in, is, is not, or, and  """

a=20
boss=True
name ="Riyadh"


if a > 10 or a > 15:
    print("a 10 er boro")
elif a > 50 and a > 100:
    print("a 50 er boro abong a 100")
else:
    print("a 10 er boro na")


if boss is True:
    print("You are my boss")
else:
    print("You are not my boss")


if boss is not True:
    print("Sorry you are not my boss")
else:
    print("Welcome my boss")


if name == "Riyadh":
    print("Name is Riyadh")
else:
    print("Name is not Riyadh")
