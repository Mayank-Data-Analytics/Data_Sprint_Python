#Dictionaries
band = {
    "vocals":"plant",
    'guitar':"page"
}

band2 = dict(vocals="plant", guitar="page")

print(band)
print(band2)
print(type(band))
print(len(band))

#access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/value pairs as tuples
print(band.items())

#verify a key exits
print('guitar' in band)
print("triangle" in band)

#change values
band["vocals"] = 'coverdale'
band.update({"bass":"JPH"})

print(band)

#remove items
print(band.pop("bass"))
print(band)

band["drums"] = "bonham"
print(band)

print(band.popitem()) #tuple
print(band)

#delete and clear
band["drums"] = "bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#copy dictionaries

band2 = band.copy()
band2['drums'] = 'dave'
print("good copy!")
print(band)
print(band2)

#or use the dict() dictionaries function
band3 = dict(band)
print("good copy!")
print(band3)

#nested dictionaries
member1 = {
    "name":"plant",
    "instrument":"vocals"
}
member2 = {
    "name":"page",
    "instrument":"guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

#sets

nums = {1, 2,3,4}

nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates allowed
nums = {1,2,2,3}
print(nums)

#true is a dupe of 1, false is a dupe of zero
nums = {1, True, 2, False, 3,4,0}
print(nums)

#add a new element to a set
nums.add(10)
print(nums)

#add elements from one set to another
morenums = {5,6,7}
nums.update(morenums)
print(nums)

#merge two sets two create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

#keep only the duplicates
one = {1,2,3}
two = {2,3,6}

one.intersection_update(two)
print(one)

#keep everything except the duplicates
one = {1,2,3}
two = {2,3,6}

one.symmetric_difference_update(two)
print(one)
