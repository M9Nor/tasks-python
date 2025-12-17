items = []
for i in range(5):
    item = input("Enter item:")
    items.append(item)

target = input("Enter target to Searche: ")

if target in items:
    print("Found")
else:
    print("Not Found")
    #only commint