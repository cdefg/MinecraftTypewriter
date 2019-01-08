import os

os.chdir("./chars")
letterlist = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

for letter in letterlist:
	print(letter)
	pf = os.popen("toilet "+ letter, "r")
	pixList = pf.read()
	with open(letter, "w") as f:
		f.write(pixList)
	f.close()
	pf.close()

