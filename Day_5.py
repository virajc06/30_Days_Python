# Excercise 5

from statistics import median


lst=[]

lstt=[1,2,3,4,5,6]

print(len(lstt))

print(lstt[0])
n=len(lstt)
print(lstt[n/2])
print(lstt[-1])

list=["Raj",20,6.4,"Python","Pune"]

listt=["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

print(listt)

print(len(listt))

nn=len(listt)
print(listt[0])
print(listt[nn//2])
print(listt[-1])

listt.append("Tesla")

print(listt)

listt.append("TCS")

print(nn//2,"Wipro")

print(listt[0].upper())

listt.append("#;")

does_exist="Accenture" in listt
print(does_exist)

listt.sort()
print(listt)

listt.sort(reverse=True)
print(listt)

listt[:3]
listt[5:]
listt[2:6]

listt.remove(list[0])
print(listt)

listt.remove(list[3])
print(listt)

listt.remove(list[nn])
print(listt)

listt.clear()
print(listt)

del listt

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


# Excercise Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)

print(median(ages))

print(sum(ages) / len(ages))

print(max(ages) - min(ages))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries)

nnn=len(countries)
print(countries[nnn//2])

# 2,3







