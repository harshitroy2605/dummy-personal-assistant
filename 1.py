import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time

while True:
	r=sr.Recognizer()

	with sr.Microphone() as source:
		print("speak something.....")
		audio=r.listen(source)
		try:
			text=r.recognize_google(audio)
			if text=="stop":
				break
			else:
				window=Tk()
				window.geometry("700x600")
				try:
					app_id="enter your app id here"
					client=wolframalpha.Client(app_id)
					answer=next(res.results).text

					label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font='times 15 bold')
					label1.pack()
					window.after(5000,lambda: window.destroy())
					mainloop()
				except:
					answer=wikipedia.summary()
					label1=Label(window,justify=LEFT,compound=CENTER,padx=10,text=answer,font='times 15 bold')
					label1.pack()
					window.after(500000,lambda: window.destroy())
					mainloop()
		except:
			answer="sorry we cannt hear you"
			print(answer)
