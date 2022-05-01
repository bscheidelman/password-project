import random

def remake_data(input_data):
    my_file = open(input_data, 'r')

    #read text file into list
    data = my_file.read()
    new_data = []
    temp = ""
    for i in data:
        if i == "\n":
            new_data.append(temp)
            temp = ""
        else:
            temp += i
    return new_data

names = ["Andrew","Bill", "Charles", "Dillard", "Elly", "Frank", "Gus", "Harry", "Ingrid", "Jacky", "Kent", "Larry", "Moe", "Noel", "Oliver", "Patrick", "Quentin", "Ricky", "Steve", "Tommy", "Uriel", "Vinny", "Wilson", "Xavier", "Yosef", "Zach"]

adjli = remake_data("english-adjectives.txt")
for val in adjli:
    if len(adjli) < 6:
        adjli.remove(val)
        
adjs = {}
alphabet = []
inital_val = ord("a")
end_val = ord("z")
while inital_val <= end_val:
    adjs[(chr(inital_val))] = []
    inital_val += 1

for key in adjs:
    let = key[0]
    for val in adjli:
        if val[0] == let:
            adjs[key].append(val)

nums = ["11", "27", "21", "07", "5"]
passli = []

for name in names:
    coreCoef = []
    for val in adjs[name[0].lower()]:
        num = 0
        for oval in adjs[name[0].lower()]:
            for let in range(3):
                if val[let] == oval[let]:
                    num += 8
                    if val.count(val[let]) > 1:
                        num -= 4
                elif oval.__contains__(val[let]):
                    num += 3
                    if val.count(val[let]) > 1:
                        num -= 1.5
        num = num/len(adjs[name[0].lower()])
        coreCoef.append(num)
    maxval = max(coreCoef)
    finaladj = adjs[name[0].lower()][coreCoef.index(maxval)]
    temp = str(finaladj) + str(name) + str(nums[random.randint(0, len(nums)-1)]) + "!"
    passli.append(temp)

filename = "password.txt"
password = str(passli[random.randint(0,len(passli)-1)])

f = open(filename, "w")
f.write(password)
f.close()

print(f'Your Password is {password}')
print(f'It is saved in the file {filename}')
