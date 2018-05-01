import sys
import numpy as np

#Encrypt - central map
def encrypt(inString, inPassword):
	#127 didn't work when I switched to using bytes
	prime = 257
	n = len(inString)
	p = inString
	t = inPassword
	#p = [ord(i) for i in inString]
	#t = [ord(i) for i in inPassword]
	r = 0


	l = [None] * (n)
	for i in range(len(t)):
		if r == 0:
			l[1] = (p[1] + t[i]) % prime
			l[2] = (p[2] + p[1] * l[1]) % prime 
			l[3] = (p[3] + p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					l[j] = (p[j] + p[1] * l[j-2]) % prime
				else:
					l[j] = (p[j] + p[j-2] * l[1]) % prime
			r = 1
		else:
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

#Decrypt - central map
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

	for i in range(len(t)-1, -1, -1):
		if r == 0:
			l[1] = (p[1] - t[i]) % prime
			l[2] = (p[2] + p[1] * l[1]) % prime 
			l[3] = (p[3] + p[1] * l[2]) % prime
			for j in range(4, n):
				if j % 4 == 3 or j % 4 == 2:
					l[j] = (p[j] + p[1] * l[j-2]) % prime
				else:
					l[j] = (p[j] + p[j-2] * l[1]) % prime
			r = 1
		else:
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
	f = open('file', 'r')
	a = np.fromfile(f, dtype=np.uint8)

	
	pt_d = a
	passw_d = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


	#Reading in a file seems like its going to take longer than I have. :(

	#print pt_d
	a = enc(pt_d, passw_d)
	print a
	
	#To switch to decrypt use this with the file input
	b = dec(a, passw_d)
	#print b


main()
