# tuple
Data1 = (7, False, "Apple", True, 7, 98.6)

# set
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

# list
Data3 = ["A", 7, -1, 3.14, True, 7]

# dict
Data4 = {"name": "Joe",
        "age": 26,
        "active": True,
        "hourly_wage": 14.75}


# DATA SET 1
def dataOneTaskOne(Data1):
    return len(Data1)
print(dataOneTaskOne(Data1))

def dataOneTaskTwo(Data1):
    return Data1[3]
print(dataOneTaskTwo(Data1))

def dataOneTaskThree(Data1):
    return Data1.count(7)
print(dataOneTaskThree(Data1))


# DATA SET 2
def dataTwoTaskOne(Data2):
    return Data2.pop()
print(dataTwoTaskOne(Data2))

def dataTwoTaskTwo(Data2):
    return Data2.add('Alpha')
dataTwoTaskTwo(Data2)

def dataTwoTaskThree(Data2):
    return Data2
print(dataTwoTaskThree(Data2))


# DATA SET 3
def dataThreeTaskOne(Data3):
    return list(reversed(Data3))
print(dataThreeTaskOne(Data3))

def dataThreeTaskTwo(Data3):
    Data3.insert(1, 'B')
    return Data3
print(dataThreeTaskTwo(Data3))

def dataThreeTaskThree(Data3):
    Data3.pop()
    return Data3
print(dataThreeTaskThree(Data3))


# DATA SET 4
def dataFourTaskOne(Data4):
    Data4.update({"active": False})
    return Data4
print(dataFourTaskOne(Data4))

def dataFourTaskTwo(Data4):
    Data4["address"] = "123 West Main Street"
    return Data4
print(dataFourTaskTwo(Data4))

def dataFourTaskThree(Data4):
    weeklySalary = (Data4["hourly_wage"] * 40)
    return weeklySalary
print(dataFourTaskThree(Data4))

def dataFourTaskFour(Data4):
    return Data4
print(dataFourTaskFour(Data4))