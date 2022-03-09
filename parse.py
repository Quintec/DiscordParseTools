import sys

fn = sys.argv[1]

msgs = []
with open(fn, 'r', encoding='latin-1') as f:
	dat = f.readlines()
i = 0
while i < len(dat):
	line = dat[i]
	if line[0] == '[' and ('AM' in line or 'PM' in line):
		msg = ''
		i += 1
		while len(dat[i].strip()) > 0:
			msg += dat[i]
			i += 1
		if len(msg) > 0 and msg[0] not in ['!', '<', '>'] and (len(msg) < 5 or msg[:5] != 'sh!rs'):
			toks = msg.split(' ')
			seen = []
			nore = ''
			cu = line.split('] ')[1].strip()
			for tok in toks:
				if tok in seen or 'http' in tok:
					continue
				tok = tok.replace('~', '')
				seen.append(toks)
				nore += tok + ' '
			if len(nore) > 0 and 'owo' not in cu:
				msgs.append(nore.strip())
				#print('added', nore.strip())
	i += 1
with open('parsed-' + fn + '.txt', 'w', encoding='latin-1') as f:
	f.write('\n\n<|endoftext|>\n\n'.join(msgs))