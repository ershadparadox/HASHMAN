
try:

	import os
	import sys
	import hashlib
	from colorama import Fore

	# ===========================

	bold = "\033[1m"
	endbold = "\033[0m"

	g = Fore.GREEN
	r = Fore.RED
	w = Fore.WHITE
	y = Fore.YELLOW
	b = Fore.BLUE
	c = Fore.CYAN
	m = Fore.MAGENTA

	# ===========================

	os.system("clear")


	print(f"""{y}

#####################################################################################################	
#	 ___  ___  ________  ________  ___  ___          _____ ______   ________  ________          #
#	|\  \|\  \|\   __  \|\   ____\|\  \|\  \        |\   _ \  _   \|\   __  \|\   ___  \        #                               
#	\ \  \\ \  \ \  \|\  \ \  \___|\ \  \\\   \       \ \  \\\__\  \  \ \  \|\  \ \  \\ \   \       #
#	 \ \   __  \ \   __  \ \_____  \ \   __  \       \ \  \\|__| \   \ \   __  \ \  \\ \   \      #
#	  \ \  \ \  \ \  \ \  \|____|\  \ \  \ \  \       \ \  \    \ \  \ \  \ \  \ \  \\ \   \     #
#	   \ \__\ \__\ \__\ \__\____\_\  \ \__\ \__\       \ \__\    \ \__\ \__\ \__\ \__\\ \__ \    #
#	    \|__|\|__|\|__|\|__|\_________\|__|\|__|        \|__|     \|__|\|__|\|__|\|__| \|__|    #
#			       \|_________|                                                         #
#####################################################################################################	

										{b}Author : {g}Paradox
							  			{b}Version : {g}1.0
										{b}Github : {g}ershadparadox

{w}۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞۞
	""")


	print(f"""

 + - - - - - - +
|		|
| md5		|
| sha1	    	|
| sha224	|
| sha256	|
| sha384	|
| sha512	|
| blake2b	|
| blake2s	|
| sha3-224	|
| sha3-256	|
| sha3-384	|
| sha3-512	|
| 		|		
 + - - - - - - +

		""")

	while True :


		input_text = input(f" {b}[*]{r} HASH MAN {y}(Enter the text){w}: ")


		print()

		

		input_hash = input(f" {b}[*]{r} HASH MAN {y}(Enter the hash type){w}: ")

		print()

		if input_hash == "md5":
			md5 = hashlib.md5(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+md5.hexdigest())
			print()
		elif input_hash == "sha1":
			sha1 = hashlib.sha1(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha1.hexdigest())
			print()
		elif input_hash == "sha224":
			sha224 = hashlib.sha224(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha224.hexdigest())
			print()
		elif input_hash == "sha256":
			sha256 = hashlib.sha256(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha256.hexdigest())
			print()
		elif input_hash == "sha384":
			sha384 = hashlib.sha384(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha384.hexdigest())
			print()
		elif input_hash == "sha512":
			sha512 = hashlib.sha512(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha512.hexdigest())
			print()
		elif input_hash == "blake2b":
			blake2b = hashlib.blake2b(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+blake2b.hexdigest())
			print()
		elif input_hash == "blake2s":
			blake2s = hashlib.blake2s(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+blake2s.hexdigest())
			print()
		elif input_hash == "sha3-224":
			sha3_224 = hashlib.sha3_224(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha3_224.hexdigest())
			print()
		elif input_hash == "sha3-256":
			sha3_256 = hashlib.sha3_256(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha3_256.hexdigest())
			print()
		elif input_hash == "sha3-384":
			sha3_384 = hashlib.sha3_384(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha3_384.hexdigest())
			print()
		elif input_hash == "sha3-512":
			sha3_512 = hashlib.sha3_512(input_text.encode())
			print(f" {m}[{r}+{m}] {g}"+sha3_512.hexdigest())
			print()
		else:
			print(f"{r}	Error")
			print()
except:
        print()
        print(f"{g}	Beyyyyyyyyyyyyyy")
        print()
        sys.exit()