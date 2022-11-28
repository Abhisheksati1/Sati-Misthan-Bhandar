from tkinter import *
from tkinter import ttk

def Bill():
    T2.delete("1.0",END)
    sum=0
    a="Sir/Madam "+T1.get()
    a+="\n \n"
    a+="\t ---BILL-- \n"
    a+="*"*50
    a+="\n"
    L=Lb1.curselection()
    L2=Lb2.curselection()
    for i in L:
        a+="\t"+Lb1.get(i)
        p=Lb1.get(i).index('.')
        sum=sum+int(Lb1.get(i)[p+1:])
        a+="\n"
    for j in L2:
        a+="\t"+Lb2.get(j)
        p=Lb2.get(j).index('.')
        sum=sum+int(Lb2.get(j)[p+1:])
        a+="\n"
    try:
        a+="\t"+r.get()
        p=r.get().index('.')
        sum=sum+int(r.get()[p+1:])
    except:
        pass
    a+="\n"
    if s.get()==2:
        a+="\t Paking Charges Rs.10"
        sum=sum+10
        a+="\n"
    if t.get()==1:
        a+="\n \t Add on Rs.30"
        sum=sum+30
    a+="\n"+"*"*50
    a+="\n"+"\t Total Rs."+str(sum)+"\n"
    a+="*"*50
    a+="\n \t GST(s+c)12% Rs 97.2 \n \t service Tax 08% Rs 64.8 \n"
    a+="*"*50+"\n"
    sum=sum+97.2+64.8
    a+="\t Net Payable Amount Rs. "+str(sum)+"\n"
    a+="*"*50+"\n"
    a+="Thanks Visit Again"
    T2.insert(END,a)
def Exit():
    exit()
def Clear():
    Lb1.selection_clear(0,END)
    Lb2.selection_clear(0,END)
    T1.delete(0,END)
    T2.delete("1.0",END)
    #Cb1.selection_clear(0,END)
    t.set(0)
    
root=Tk()


root.title("SATI MISTHAN BHANDAR")
root.geometry("1000x500")

r=StringVar()
s=IntVar()
s.set(1)
t=IntVar()

L1=Label(root,text="SATI MISTHAN BHANDAR",font=('Arial',20),bg='Yellow',fg='Red')
L2=Label(root,text="Customer Name",font=('Arial',15))
L3=Label(root,text="Snacks",font=('Arial',15))
L4=Label(root,text="Sweets",font=('Arial',15))
L5=Label(root,text="Drinks",font=('Arial',15))
L1.grid(row=0,column=1)
L2.grid(row=1,column=0)
L3.grid(row=2,column=0)
L4.grid(row=2,column=1)
L5.grid(row=2,column=2)

T1=Entry(root,width=25)
T1.grid(row=1,column=1)

Lb1=Listbox(root,selectmode=MULTIPLE,exportselection=0)
Lb2=Listbox(root,selectmode=MULTIPLE,exportselection=0)
Lb1.insert(1, "Dosa Rs.150")
Lb1.insert(2, "Pizza Rs.450")
Lb1.insert(3, "Burger Rs.290")
Lb1.insert(4, "Samosa Rs.90")
Lb1.insert(5, "Tikki Rs.80")
Lb1.insert(6, "Pasta Rs.180")
Lb2.insert(1, "Rabri Rs.150")
Lb2.insert(2, "Gulab Jamun Rs.450")
Lb2.insert(3, "Ras Gulla Rs.290")
Lb2.insert(4, "Laddu Rs.90")
Lb2.insert(5, "Barfi Rs.80")
Lb2.insert(6, "Halwa Rs.180")
Lb1.grid(row=3,column=0)
Lb2.grid(row=3,column=1)

Cb1=ttk.Combobox(root,textvariable=r)
Cb1['values']=('Coffie Rs.90','Tea Rs.50','Shake Rs.120','Soups Rs.110')
Cb1.grid(row=3,column=2)

Rb1=Radiobutton(root,text="Dine Here",variable=s,value=1)
Rb2=Radiobutton(root,text="Pack",variable=s,value=2)
Rb1.grid(row=4,column=0)
Rb2.grid(row=4,column=1)

Cb1=Checkbutton(root,text="Add Ons",variable=t)
Cb1.grid(row=5,column=0)

B1=Button(root,text="Bill",width=20,command=Bill)
B2=Button(root,text="Clear",width=20,command=Clear)
B3=Button(root,text="Exit",width=20,command=Exit)
B1.grid(row=6,column=0)
B2.grid(row=6,column=1)
B3.grid(row=6,column=2)

T2=Text(root,width=50,height=25,bg='Black',fg='White',font=('Arial',10))
T2.grid(row=0,column=3,rowspan=8)
root.mainloop()

