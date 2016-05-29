import sys

def resistance(f):
	nodes = f.next().split()
	
	resistances = {}
	for line in f:
		l = line.split()
		if (l[0], l[1]) in resistances:
			resistances[(l[0], l[1])].append(int(l[2]))
		else: 
			resistances[(l[0], l[1])] = [int(l[2])]

	rTotal = 0
	for r in resistances:
		if len(resistances[r]) > 1:
			t = 0
			for i in resistances[r]:
				t += 1.0/i
			rTotal += 1.0/t
		else:
			rTotal += resistances[r][0]

	return rTotal






if __name__ == "__main__":
	f = open(sys.argv[1],'r')
	print "Total resistance is " + str(resistance(f))
