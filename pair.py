import sys

fn = sys.argv[1]

with open(fn, 'r', encoding='latin-1') as f:
	dat = f.read()
msgs = dat.split('\n\n<|endoftext|>\n\n')
filt = []
for i in range(len(msgs) - 1):
	msg1 = msgs[i]
	msg2 = msgs[i + 1]
	if len(msg1) + len(msg2) == 0:
		continue
	filt.append('[1]: ' + msg1.strip() + '\n[2]: ' + msg2.strip())
with open(fn + 'paired.txt', 'w', encoding='latin-1') as f:
	f.write('\n\n<|endoftext|>\n\n'.join(filt))