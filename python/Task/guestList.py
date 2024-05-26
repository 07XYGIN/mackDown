guests = [
    "Alice Johnson",
    "Bob Smith",
    "Catherine Lee",
    "David Martinez",
    "Ella Brown",
    "Frank Williams",
    "Grace Wilson",
    "Henry Clark",
    "Isabella Thompson",
    "Jack Davis"
]

for i in guests:
    print(i + 'Will we have dinner together later?')

newGuests = guests.pop(1)

print(newGuests + "Can't come to the appointment")
guests.insert(1,'Jock')

for i in guests:
    print(i + 'Will we have dinner together later?')

print('I found a bigger dining table')
guests.insert(0,'a')
guests.insert(4,'b')
guests.append('c')
for i in guests:
    print(i + 'Will we have dinner together later?')
print('I can only invite two people')
while guests:  
    guests.pop()
    if len(guests) == 2:
        break
del guests[0]
del guests[0]
print(guests)
