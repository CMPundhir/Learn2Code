# Dicttionary
# Key value pair
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

myLife = {
	"Name": "CMPundhir",
	"Age": 12,
	"Address": "Ghar pr",
	"Water": "3-4 litre",
	"Students": ["Harshil", "Pranshu"],
	"Fav": ["Panchayat", "End Game"],
	"PrivateJet": False,
	"Helicopter": True,
	"Scooty": True,
	"OS": ["MAC", "WINDOWS", "ANDROID"]
}

# check object type
print(type(myLife))

# getting value of a key
print(myLife["Students"])

# change value of a key
myLife["Age"] = 15
print(myLife["Age"])

# create or add new key
myLife["Car"] = False
print(myLife["Car"])

# remove a key
myLife.pop("Car")

# remove last item in dict
myLife.popitem()

# printing whole dictionary
print(myLife)

print("------******-------")
# loop a dict
for item in myLife:
	print(item, ":", myLife[item])
print("------******-------")

print("All keys")
# loop a dict getting keys
for key in myLife.keys():
	print(key, end=",")
print("\n------******-------")

print("All values")
# loop a dict getting values
for v in myLife.values():
	print(v, end=",")
print("\n------******-------")

print("All Key and value pairs")
# loop a dict getting values
for k, v in myLife.items():
	print(k, ":", v)
print("\n------******-------")


# clear dict
myLife.clear()

# printing whole dictionary
print(myLife)