from tkinter import *
from tkinter.ttk import *
from PyPDF2 import PdfFileMerger
import tkinter.filedialog
from tkinter import filedialog
import os 
import zipfile

root = Tk()
root.geometry('700x600')
root.title("PDF Merger 1.0")

class Process:

    def open_file(self):

        self.files = tkinter.filedialog.askopenfilenames(parent = root, title = 'Choose files', filetypes = [("PDF file", ".pdf"), ("ZIP file", ".zip")])

        for item in root.tk.splitlist(self.files):

            if item.endswith('.zip'):

                zip = zipfile.ZipFile(item)

                for zipitem in zip.namelist():
                    neededfile = zip.open(zipitem)
                    content = neededfile.read()

                    filename = item.rsplit('/', 1)[1]

                    createfolderpath = os.path.dirname(item) + '/'+ filename + 'ZipExtractedHere'

                    if os.path.exists(createfolderpath) == False:

                        os.mkdir(createfolderpath)

                    ziplocation = createfolderpath + '/' + zipitem

                    neededfile = open(ziplocation, 'wb')

                    neededfile.write(content)

                    neededfile.close()

                    ListBox.insert(END, ziplocation)

                    print(ziplocation)

                

            else:

                 ListBox.insert(END, item)

 

        NumberOfFiles = ListBox.size()

        OutputLabel.config(text = "Total " + str(NumberOfFiles) + " files selected")

 

        self.AsList = ListBox.get(0, tkinter.END)

        

 

 

    def merger_pdf(self):

        SaveAs = filedialog.asksaveasfilename(filetypes = [("PDF file", ".pdf")])

        pathpdfoutput = SaveAs + ".pdf"

        if SaveAs != "":

            

            if os.path.exists(pathpdfoutput) == True:

                OutputLabel.config(text = "This file name exists in chosen folder ,please change the file name and save it again")

 

            if os.path.exists(pathpdfoutput) == False:
                print("Please wait...")
                pdfOutput = open(SaveAs + '.pdf', 'wb')
                merger = PdfFileMerger(strict=False)

                for x in root.tk.splitlist(self.AsList):           
                   if x.endswith('.pdf'):
                        merger.append(x)

                   if x.endswith('.tiff'):
                       print(".tiff file detected and excluded from list")

                merger.write(pdfOutput)

                pdfOutput.close()

                OutputLabel.config(text = "Files merged successfully -> " + pathpdfoutput)

        else: 

             OutputLabel.config(text = "Process Cancelled by User, please try once again")

 

    def seperator(self):
        ListBox.insert(END, 'blank.pdf')

        NumberOfFiles = ListBox.size()

        OutputLabel.config(text = "Total " + str(NumberOfFiles) + " files selected")

        self.AsList = ListBox.get(0, tkinter.END)

 

    def remove_selected(self):
        selected = ListBox.curselection()

        for index in selected[::-1]:
            ListBox.delete(index)

 

        NumberOfFiles = ListBox.size()

        OutputLabel.config(text = "Total " + str(NumberOfFiles) + " files selected")

    

        self.AsList = ListBox.get(0, tkinter.END)

 

    def clean_listbox(self):
       ListBox.delete(0, tkinter.END)

       self.AsList = ListBox.get(0, tkinter.END)

       NumberOfFiles = ListBox.size()

       OutputLabel.config(text = "Total " + str(NumberOfFiles) + " files selected")

 

p = Process()

btnBrowseFiles = Button(root, text = 'Browse File Directory', command = lambda: p.open_file())

btnBrowseFiles.pack(side = TOP, pady = 10)

 

btnMergeFiles = Button(root, text = 'Click to Merge the Files', command = lambda: p.merger_pdf())

btnMergeFiles.pack(side = TOP, pady = 10)

 

OutputLabel = Label(root, text = "")

OutputLabel.pack(pady = 20)

 

ListBox = Listbox(root)

ListBox.pack(pady = 20)

ListBox.config(width = 85, height = 10)




btnCleanListBox = Button(root, text = 'Clean List', command = lambda: p.clean_listbox())

btnCleanListBox.pack(side = LEFT, pady = 30)

btnCleanListBox.place(relx = 0.30, rely=0.6)

 

SeperatorButton = Button(root, text = 'Add Seperator Page', command = lambda: p.seperator())

SeperatorButton.pack(side = LEFT, pady = 30)

SeperatorButton.place(relx = 0.42 ,rely=0.6)

 

btnCleanOne = Button(root, text = 'Remove Selected PDF', command = lambda: p.remove_selected())

btnCleanOne.pack(side = LEFT, pady = 30)

btnCleanOne.place(relx = 0.59, rely=0.6)

 

SignatureLable = tkinter.Label(root, text = "Developed by Huseyn Mammadli (hm10869)")

SignatureLable.place(x = 450, y = 575)

 

mainloop()