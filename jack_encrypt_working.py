import sys
import numpy as np

def encrypt(inString, inPassword):
	prime = 257
	n = len(inString)
	p = inString
	t = inPassword
	#p = [ord(i) for i in inString]
	#t = [ord(i) for i in inPassword]
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
	prime = 257
	n = len(inString)
	c = inString
	t = inPassword
	#c = [ord(i) for i in inString]
	#t = [ord(i) for i in inPassword]
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


def genMatrix(size):
	matrix = np.empty((size,size))
	for i in range(0, size):
		for j in range(0, size):
			val = 0
			if i == j:
				val = 1
			elif i > j:
				if i % 2 == 0:
					if j % 2 == 0:
						val = 0
					else:
						val = 0
				else:
					if j % 2 == 0:
						val = 0
					else:
						val = 0
			else:
				val = 0
			matrix[i][j] = val
	#print matrix
	return matrix


def enc(plaintext, password):
	ct = []
	matrix = genMatrix(len(plaintext))
	plaintext = np.matmul(plaintext, matrix)

	ct = encrypt(plaintext, password)

	inverse = np.linalg.inv(matrix)
	ct = np.matmul(ct, matrix)

	return ct


def dec(ciphertext, password):
	pt = []
	matrix = genMatrix(len(ciphertext))
	ciphertext = np.matmul(ciphertext, matrix)

	pt = decrypt(ciphertext, password)

	inverse = np.linalg.inv(matrix)
	pt = np.matmul(pt, matrix)

	return pt



def main():
	'''
	#Will take in bytes from a file.
	pt_d = [1,2,3,4,5,6,7,8,8,9,10]
	passw_d = [1,2,3,1,2,3]


	#Reading in a file seems like its going to take longer than I have. :(

	print pt_d
	a = enc(pt_d, passw_d)
	print a
	b = dec(a, passw_d)
	print b
	'''

	f = open('file', 'r')
	a = np.fromfile(f, dtype=np.uint8)

	
	pt_d = a
	passw_d = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


	#Reading in a file seems like its going to take longer than I have. :(

	#print pt_d
	a = enc(pt_d, passw_d)
	print a
	b = dec(a, passw_d)
	#print b






	sys.exit()
	with open('file', 'rb') as f:
		array = []
		while True:
			a = f.read(1)
			if a:
				array.append(a)
			else:
				f.close()
				print array
				break




main()


sys.exit()


pt_a = "abcdefg\n"
passw_a = "1234"

pt_a = [ord(i) for i in pt_a]
passw_a = [ord(i) for i in passw_a]


print pt_a
a = encrypt(pt_a, passw_a)
print a
c = decrypt(a,passw_a)
print c
d = [chr(i) for i in c]
print d
#print [chr(i) for i in decrypt(enc, "PASSWORD")]