set_countries = {"Col", "Mex", "Arg"}
size = len(set_countries)
print(size)

print("Col" in set_countries)
print("Pe" in set_countries)

#Add
set_countries.add("Pe")
print(set_countries)
set_countries.add("Pe")
print(set_countries)

#Update
set_countries.update({"Bol", "Ecua", "Bol"})
print(set_countries)

#Remove
set_countries.remove("Col")
print(set_countries)
#set_countries.remove("Col")
set_countries.discard("Col")
print(set_countries)
set_countries.clear()
print(set_countries)