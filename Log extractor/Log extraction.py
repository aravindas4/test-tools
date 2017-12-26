from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import zipfile,os,re
from tkinter.messagebox import showinfo
import shutil
class MyFrame(Frame): #Inhering the Frame class. The container for browse button and label
    def __init__(self):  #constructor
        Frame.__init__(self)
        #print(self.master)
        self.master.title("Main Frame") #Title for the frame. self.matrer is equivalent to MyFrame.Frame call
        #self.title('Example')
        self.master.rowconfigure(1, weight=1)
        #self.rowconfigure(1,weight=1)
        self.master.columnconfigure(1, weight=1)
        '''Setting the x and y coorinates'''
        #self.columnconfigure(1,weight=1)
        self.grid(sticky=W+E+N+S)
        
        roms=open('omsorder 3_1.txt','w') #resultant file creation
        roms.close()
        roms=open('cca REG PEND Accounts.txt','w') #resultant file creation
        roms.close() #closing the file
        self.label=ttk.Label(text='Please select a zipped log file',font=('Verdana,14'))  # creating the label
        self.label.grid(row=1, column=0, sticky=W)
        self.button = ttk.Button(self, text="Browse", command=self.load_file, width=10)
        '''creating the browse button
        when the button is clicked the method defined in the command is called, every time.'''
        self.button.grid(row=1, column=1, sticky=W)
        

    def co_extra(self,fn):
        f1=open('./Files/'+fn,'r') #open the received file in File folder in read mode
        str=f1.read() #Read entire file content
        f1.close()
        #print(str)
        r=re.compile(r'OMSOrderId:\s*(\d*)\t') #Compile the regular expression (Regex)
    
        rl=[]
        rl=r.findall(str) #Find all data in the read data through Regex into a list
        rs='\n_'.join(rl)
        rl=rs.split('_')
        roms=open('omsorder 3_1.txt','a') #Open a file in append mode
        roms.writelines(rl)#Write the found data to a file
        roms.write('\n')
        roms.close()
        print(fn,sep=' ') #Print the filename just processed
        print(len(rl))#Print the data count found in the file
        return len(rl) #Return the data count
    def cca(self,fn):
        f1=open('./Files/'+fn,'r')
        str=f1.read()
        f1.close()
        #print(str)
        r=re.compile(r'The account:\s*(\d*).*')
    
        rl=[]
        rl=r.findall(str)
        rs='\n_'.join(rl)
        rl=rs.split('_')
        roms=open('cca REG PEND Accounts.txt','a')
        roms.writelines(rl)
        roms.write('\n')
        roms.close()
        print(fn,sep=' ')
        print(len(rl))
        return len(rl)
        
    def load_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        #method to browse the desired files
        
        #print(fname)
        if fname:
            try:
                print("""here it comes: self.settings["template"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        '''
        Checking whether successfully able to browse and find the file.
        If successful, prints the message
        otherwise in the popup displays the error that unable to read the file'''
        
        zf=zipfile.ZipFile(fname) # obtaining a reference to zipped file
        zf.extractall('./Files/') #Extarcting the zipped file
        zf.close()
        print('Extracting done...')
        counter1=0    # counter for one of the data

        for f in os.listdir(path='./Files/'):  #for each content in the extarcted File folder
            if f.startswith('createorder_3.1_updated_'): #If the content begins with the name
                counter1 +=self.co_extra(f) #calling a method and get the data count and add up

        counter2=0   #counter for another data

        for f in os.listdir(path='./Files/'): #for each content in the extarcted File folder
            if f.startswith('createcustomeraccount'):#If the content begins with the name
                counter2 +=self.cca(f)#calling a method
        
        print('The oms order count:'+str(counter1)) #Print the total data count
        print('The cc accounts count:'+str(counter2))    
        showinfo(title='Final Message',message='DONE!!!')
        shutil.rmtree('./Files')#deleting the extarcted File folder
        self.master.destroy() #destroying the Parent frame
        try:
            self.destroy()#Destroying the Main frame
        except:
            pass
        return
        #exit()
        
if __name__ == "__main__":
    MyFrame().mainloop()  #continue the execution until we explicitly come out
