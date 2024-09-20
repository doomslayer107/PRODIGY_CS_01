from tkinter import *
def GUI():
    
    master = Tk()
    #master.geometry("700x600")
    
    #title
    master.wm_title("Caesar cipher")
    master.configure( background="grey14" )
    
    #askquestion
    text_label = Label(master, text="Let's Cipher",fg="Red", bg="grey14")
    text_label.pack(side=TOP)
    #textbox
    
    text_field = Text(master,bg="Grey75",fg="Red")
    text_field.pack(side=TOP)
    
    #shiftques
    key_label = Label(master, text="SHIFT BY:-",fg="Red",bg="grey14")
    key_label.pack(side=TOP)
    #shiftslider
    key_slider = Scale(master, from_=1, to=25, orient=HORIZONTAL,length=500, fg="red",bg="thistle4")
    key_slider.pack(side=TOP)
    
    #logic

    alpha=[chr(i) for i in range(97,123)]
    alpha_upper=[chr(i) for i in range(65,91)]
    
    def set_temp():
        return(text_field.get("1.0","end-1c"),key_slider.get())
    
    def allow_to_paste(string):
        master.clipboard_clear()
        master.clipboard_append(string)
        
    def cipher():
        inf,shift=set_temp()
        ciphered=list()
        deciphered=list()
        cipher_lower=dict(zip(alpha,[chr(ord(i)+shift) if ord(i)+shift<=122 else chr(97+((ord(i)+shift)-123))  for i in alpha]))
        cipher_upper=dict(zip(alpha_upper,[chr(ord(i)+shift) if ord(i)+shift<=90 else chr(65+((ord(i)+shift)-91))  for i in [x.upper() for x in alpha]]))
        r=append(inf,ciphered,cipher_upper,cipher_lower)
        result.set(r)
        allow_to_paste(r)
        
    def append(info,c,cu,cl):
        for i in info:
            if i in alpha_upper:
                c.append(cu[i])
            elif i in alpha:
                c.append(cl[i])
            else:
                c.append(i)
        return("".join(c))
    
    def decipher():
        inf,shift=set_temp()
        ciphered=list()
        deciphered=list()
        decipher_lower=dict(zip(inf,[chr(ord(i)-shift) if ord(i)-shift>=97 else chr(123-(97-((ord(i)-shift))))  for i in inf]))
        decipher_upper=dict(zip([b for b in inf],[chr(ord(i)-shift) if ord(i)-shift>=65 else chr(91-(65-((ord(i)-shift))))  for i in [y.upper() for y in inf]]))
        r=append(inf,deciphered,decipher_upper,decipher_lower)
        result.set(r)
        allow_to_paste(r)

    #encrypt/decrypt buttons
    b = Button(master, text="ENCRYPT", command=cipher, fg="Black",bg="Green")
    c = Button(master, text="DECRYPT", command=decipher, fg="black",bg="Red")
   
  

    #output box_default text
    result = StringVar()
    result.set("Ciphered/Deciphered text")
    #output box
    result_label = Entry(master, textvariable=result ,bg="White", width=150, fg="red")
    result_label.pack(side=TOP)
    
    b.pack(side=TOP)
    c.pack(side=TOP)

    master.mainloop()
    
#calling the gui func
if __name__ == "__main__":
    GUI()
