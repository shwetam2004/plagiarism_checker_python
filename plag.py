import re
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def cosineSimilarity():
    try:
        universalSetOfUniqueWords = []
        matchPercentage = 0

        ####################################################################################################

        inputQuery = entry_query.get()
        lowercaseQuery = inputQuery.lower()

        queryWordList = re.sub("[^\w]", " ", lowercaseQuery).split()  # Replace punctuation by space and split

        for word in queryWordList:
            if word not in universalSetOfUniqueWords:
                universalSetOfUniqueWords.append(word)

        ####################################################################################################

        fd = open("database1.txt", "r")
        database1 = fd.read().lower()

        databaseWordList = re.sub("[^\w]", " ", database1).split()  # Replace punctuation by space and split

        for word in databaseWordList:
            if word not in universalSetOfUniqueWords:
                universalSetOfUniqueWords.append(word)

        ####################################################################################################

        queryTF = []
        databaseTF = []

        for word in universalSetOfUniqueWords:
            queryTfCounter = 0
            databaseTfCounter = 0

            for word2 in queryWordList:
                if word == word2:
                    queryTfCounter += 1
            queryTF.append(queryTfCounter)

            for word2 in databaseWordList:
                if word == word2:
                    databaseTfCounter += 1
            databaseTF.append(databaseTfCounter)

        dotProduct = 0
        for i in range(len(queryTF)):
            dotProduct += queryTF[i] * databaseTF[i]

        queryVectorMagnitude = 0
        for i in range(len(queryTF)):
            queryVectorMagnitude += queryTF[i] ** 2
        queryVectorMagnitude = math.sqrt(queryVectorMagnitude)

        databaseVectorMagnitude = 0
        for i in range(len(databaseTF)):
            databaseVectorMagnitude += databaseTF[i] ** 2
        databaseVectorMagnitude = math.sqrt(databaseVectorMagnitude)

        matchPercentage = (float)(dotProduct / (queryVectorMagnitude * databaseVectorMagnitude)) * 100

        output = "Input query text matches %0.02f%% with database." % matchPercentage

        messagebox.showinfo("Result", output)
    except Exception as e:
        output = "Please Enter Valid Data"
        messagebox.showerror("Error", output)

def loadPage():
    entry_query.delete(0, tk.END)
    entry_query.insert(0, "")

# Create the main window
app = tk.Tk()
app.title("Plagiarism Checker")
app.geometry("920x670+290+85")
app.configure(bg="#0f1a2b")
app.resizable(False, False)

# Create a frame for the widgets
frame = tk.Frame(app, bg="#0f1a2b")
frame.pack(pady=30)

# Create widgets with some styling
label_query = tk.Label(frame, text="Enter your query:", font=("Hello valentica", 20), bg="sky blue")
entry_query = tk.Entry(frame, font=("Helvetica", 20))
Button_calc = PhotoImage(file="plag_check.png")
btn_calculate = tk.Button(frame, image=Button_calc, command=cosineSimilarity)
Button_clear = PhotoImage(file="clear_btn.png")
btn_clear = tk.Button(frame, image=Button_clear, command=loadPage)

# Place widgets on the window
label_query.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_query.grid(row=0, column=1, padx=10, pady=10)
btn_calculate.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)
btn_clear.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)

# Start the Tkinter main loop
app.mainloop()
