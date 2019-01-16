# read file
def read_file(filename):
	record = []
	with open(filename, 'r', encoding = 'utf-8-sig') as r:
		for line in r:
			record.append(line.strip())
	return record
#拆行加字
def trans(chat):
	
	Terry_wordcont = 0
	terry_sticker = 0
	terry_video = 0
	Jack_wordcont = 0
	jack_sticker = 0
	jack_video = 0
	name = None
	for line in chat:
		new = line.split(' ')
		time = new[0]
		name = new[1]
		if name == '莊友淳(Terry)':
			if new[2] == '貼圖':
				terry_sticker += 1
			elif new[2] == '影片':
				terry_video += 1
			else:
				for m in new[2:]:
					Terry_wordcont += len(m)
		elif name == 'Jack':
			if new[3] == '貼圖':
				jack_sticker += 1
			elif new[3] == '影片':
				jack_video += 1
			else:
				for m in new[3:]:
					Jack_wordcont += len(m)
	print('Jack word cont: ', Jack_wordcont)
	print('Jack sticker cont: ', jack_sticker)
	print('jack video cont: ', jack_video)
	print('Terry word cont:', Terry_wordcont)
	print('Terry sticker cont:', terry_sticker)
	print('terry video cont:', terry_video)
	#print(new)
	return new
	


def write_file(filename, chat):
	with open(filename, 'w', encoding = 'utf-8') as w:
		for line_1 in chat:
			w.write(line_1 + '\n')
	
	

def main():
	chat = read_file('[LINE]Terry.txt')
	chat = trans(chat)
	#write_file('outfile.txt', chat)
	#print(chat)
main()


