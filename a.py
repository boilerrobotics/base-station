
with open("output.txt","r") as f:
    lines = f.readlines()

time = []

for line in lines:
   print(line)
   ind = line.index("time=")
   time.append(float(line[ind+5:len(line)-3]))

print(max(time))