import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import os
import functions as sc

root = tk.Tk()
frame = tk.Frame(root)

frameBot = tk.Frame(root)	
frameBot.pack( side = "bottom")

frameMid= tk.Frame(root)	
frameMid.pack( side = "bottom")

frameTop = tk.Frame(root)	
frameTop.pack( side = "top")

fichier1 = tk.Button(frameTop, text="Fichier 1", fg="red",command=sc.ask_file1)
fichier1.pack( side = "left")


fichier2 = tk.Button(frameTop, text="Fichier 2", fg="brown",command=sc.ask_file2)
fichier2.pack( side = "left" )

fichier3 = tk.Button(frameTop, text="Fichier 3", fg="blue",command=sc.ask_file3)
fichier3.pack( side = "left" )



def visualise():

	
	
	sc.join_files()		
	sc.kmeans_apply()

	path = "resultat.png"
	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img = ImageTk.PhotoImage(Image.open(path))

	#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	panel = tk.Label(frameMid, image = img)

	#The Pack geometry manager packs widgets in rows or columns.
	panel.pack(side = "bottom", fill = "both", expand = "yes")

	return


def report():

	sc.create_reporte(sc.ds,sc.labels)
	
	return

visualiser = tk.Button(frameBot, text="Visualiser", fg="black",command=visualise)
visualiser.pack( side = "left")

rapport = tk.Button(frameBot, text="Rapport", fg="black",command=report)
rapport.pack( side = "right")

root.mainloop()


