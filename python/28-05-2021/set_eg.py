# Set
# set is a collection of unordered items.
# set contains uniques elements
# set is mutable or Unchangeable
# set is unindexed
# set items can be added but can't be changed


jwellery_set = {"Rings", "braclet"}
print(type(jwellery_set))
print(jwellery_set)
print(len(jwellery_set))

for x in jwellery_set:
	print(x)


list_keys = ["name", "class", "subjects"]
keySet = set(list_keys)
print(type(list_keys), list_keys)
print(type(keySet), keySet)