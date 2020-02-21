devices=[]
file=open("ComeTogether.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
