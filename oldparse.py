import sys

user = sys.argv[1]
fn = sys.argv[2]

msgs = []
with open(fn, 'r') as f:
	dat = f.readlines()
i = 0
while i < len(dat):
	line = dat[i]
	if line[0] == '[' and ('AM' in line or 'PM' in line):
		cu = line.split('] ')[1].strip()
		if cu == user:
			msg = ''
			i += 1
			while len(dat[i].strip()) > 0:
				msg += dat[i]
				i += 1
			msgs.append(msg)
	i += 1
with open('parsed-' + user.replace('#', '') + fn + '.txt', 'w') as f:
	f.write('\n<|endoftext|>\n\n'.join(msgs))