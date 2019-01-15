# read file
def read_file(filename):
	record = []
	with open(filename, 'r', encoding = 'utf-8-sig') as r:
		for line in r:
			record.append(line.strip())
	return record
#拆行加字
def trans(chat):
	new = []
	person = None
	for line in chat:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ':' + line)
	return new
	


def write_file(filename, chat):
	with open(filename, 'w', encoding = 'utf-8') as w:
		for line_1 in chat:
			w.write(line_1 + '\n')
	
	

def main():
	chat = read_file('input.txt')
	chat = trans(chat)
	write_file('outfile.txt', chat)
	print(chat)
main()


