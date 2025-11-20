print("+++++example of list+++++")
vehicleList=["motorcycle", "car", "jetplane"]
print(vehicleList)
print(type(vehicleList))
print(vehicleList[0])
print(vehicleList[1])
print(vehicleList[2])

print("+++++example of list+++++")
vehicleList[1]="truck"
print(vehicleList)
print(vehicleList[0])
print(vehicleList[1])
print(vehicleList[2])

print("+++++example of tuple+++++")
gearTuple=("helmet", "glove", "vest")
print(gearTuple)
print(type(gearTuple))
print(gearTuple[0])
print(gearTuple[1])
print(gearTuple[2])

# gearTuple[1]="knee pad"

print("+++++example of dictionary+++++")
equipmentDictionary={
    "control":"electric steering",
    "brake":"disc",
    "safety":"airbags"
}
print(equipmentDictionary)
print(type(equipmentDictionary))
print(equipmentDictionary["control"])
print(equipmentDictionary["brake"])
print(equipmentDictionary["safety"])