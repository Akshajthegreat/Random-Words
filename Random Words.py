from tkinter import*
import random

root=Tk()
root.title("Random_Words")
root.geometry("500x500")

label=Label(root)
def random_word():
    list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    random_no1=random.randint(1,26)
    random_no2=random.randint(1,26)
    random_no3=random.randint(1,26)
    random_no4=random.randint(1,26)
    random_no5=random.randint(1,26)
    random_word1=list[random_no1]
    random_word2=list[random_no2]
    random_word3=list[random_no3]
    random_word4=list[random_no4]
    random_word5=list[random_no5]
    label["text"]=random_word1+random_word2+random_word3+random_word4+random_word5
btn=Button(root,text="generate",command=random_word)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
