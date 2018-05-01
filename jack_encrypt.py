


def encrypt(inString, inPassword):
	prime = 127
	n = len(inString)
	p = [ord(i) for i in inString]
	t = [ord(i) for i in inPassword]
	r = 0


	l = [None] * (n)
	#Remember to decrement by one to be zero aligned for the array
	for i in range(len(t)):
		#Changed this to be the size of the inString instead of the length of the password.

		if r == 0:
			#print "before l: " + str(l)
			l[1] = (p[1] + t[i]) % prime
			l[2] = (p[2] + p[1] * l[1]) % prime 
			l[3] = (p[3] + p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					l[j] = (p[j] + p[1] * l[j-2]) % prime
				else:
					l[j] = (p[j] + p[j-2] * l[1]) % prime
			r = 1
			#print "after l: " + str(l)
		else:
			#print "before p: " + str(p)
			p[1] = (l[1] + t[i]) % prime
			p[2] = (l[2] - p[1] * l[1]) % prime
			p[3] = (l[3] - p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					p[j] = (l[j] - p[1] * l[j-2]) % prime
				else:
					p[j] = (l[j] - p[j-2] * l[1]) % prime
			r = 0
	if r == 0:
		return p
	return l


def decrypt(inString, inPassword):
	prime = 127
	n = len(inString)
	c = [ord(i) for i in inString]
	t = [ord(i) for i in inPassword]
	r = 0
	l = [None] * (n)
	p = [None] * (n)

	if len(t) % 2 == 0:
		r = 0
		p = c
	else:
		r = 1
		l = c

	#Remember to decrement by one to be zero aligned for the array
	for i in range(len(t)-1, -1, -1):
		#Changed this to be the size of the inString instead of the length of the password.

		if r == 0:
			#print "before l: " + str(l)
			l[1] = (p[1] - t[i]) % prime
			l[2] = (p[2] + p[1] * l[1]) % prime 
			l[3] = (p[3] + p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					l[j] = (p[j] + p[1] * l[j-2]) % prime
				else:
					l[j] = (p[j] + p[j-2] * l[1]) % prime
			r = 1
			#print "after l: " + str(l)
		else:
			#print "before p: " + str(p)
			p[1] = (l[1] - t[i]) % prime
			p[2] = (l[2] - p[1] * l[1]) % prime
			p[3] = (l[3] - p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					p[j] = (l[j] - p[1] * l[j-2]) % prime
				else:
					p[j] = (l[j] - p[j-2] * l[1]) % prime
			r = 0
	if r == 0:
		return p
	return p



a = encrypt("abcdefg\n", "PASSWORD")
print a
b =  [chr(i) for i in a]
c = decrypt(b,"PASSWORD")
print c
d = [chr(i) for i in c]
print d
#print [chr(i) for i in decrypt(enc, "PASSWORD")]


