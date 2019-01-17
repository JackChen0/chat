

gogogo = []
new = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		gogogo.append(line.strip())

for line in gogogo:
	new = line.split(' ')
	time = new[0][:5]
	name = new[0][5:]
	print(time)
	print(name)
