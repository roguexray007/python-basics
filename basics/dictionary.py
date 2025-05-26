myDict = {
    "sekiro": 10
}

myDict["elden ring"] = 100

print(myDict)



myDict.pop("elden ring")

print(myDict)



myDict["nioh"] = 200
myDict["nioh2"] = 300

print(myDict)



print("loop dictionary")

for mykey, myvalue in myDict.items():
    print(mykey, myvalue)




