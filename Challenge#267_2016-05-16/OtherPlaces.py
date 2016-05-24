import sys, re

def otherPlaces(number, size=100):
	final = ""
	prefixes = ["th", "st", "nd", "rd", "th", "th", "th", "th", "th", "th"]
	for i in range(1,int(size)+1):
		if i == int(number):
			print "hi"
			continue
		singlesDigit = i%10
		tensDigit = i/10%10
		if tensDigit == 0:
			final += "%d" % i + prefixes[i%10] + ", "
		else:
			final += str(i) + "th, "
	return final



if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "What place is your dog?"
	if len(sys.argv) > 1:
		number = sys.argv[1]
		size = 100
	if len(sys.argv) > 2:
		number = sys.argv[1]
		size = sys.argv[2]
	print(otherPlaces(number,size))

	