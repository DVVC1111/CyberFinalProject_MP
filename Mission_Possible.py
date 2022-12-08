from tkinter import *
import tkinter.filedialog
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import  os

#GUI::Start          ----------------------->

class Mission_Possible:
    output_image_size = 0
             
    #Main Screen
    def main(self, root):
        root.title('Mission Possible')
        root.geometry('800x1000')
        root.resizable(width =True, height=True)
        root.config(bg = '#f0f0f0')
        frame = Frame(root)
        frame.grid()
        
        title = Label(frame,text='Mission Possible')
        title.config(font=('Helvetica',50, 'bold'))
        title.grid(pady=100)
        title.grid(row=1)
        
        subhead = Label(frame,text='Pick your weapon, Agent!')
        subhead.config(font=('Helvetica',30, 'bold'))
        subhead.grid(pady=30)
        
        subhead.grid(row=2)

        encode = Button(frame,text="Encode",command= lambda :self.encode_frame1(frame), padx=14 )
        encode.config(font=('Helvetica',18), bg='#FFFFFF')
        encode.grid(pady=12)
        encode.grid(row=3)
        
        decode = Button(frame, text="Decode",command=lambda :self.decode_frame1(frame), padx=14)
        decode.config(font=('Helvetica',18), bg='#FFFFFF')
        decode.grid(pady=12)
      
        decode.grid(row=4)

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)


    #Return to last frame
    def back(self,frame):
        frame.destroy()
        self.main(root)

    
    #Encode: Main Screen
    def encode_frame1(self,frame):
        encode_frame = Frame(root)
        encode_frame.grid()
        
        encode_frame1_title= Label(encode_frame,text='Select your material, Agent!')
        encode_frame1_title.config(font=('Helvetica',25, 'bold'))
        encode_frame1_title.grid(pady=100)
        encode_frame1_title.grid(row=1)
        

        button_encode_select = Button(encode_frame,text='Select',command=lambda : self.encode_frame2(encode_frame),padx=14,bg = '#FFFFFF' )
        button_encode_select.config(font=('Helvetica',18),bg='#FFFFFF')
        button_encode_select.grid(pady=12)
        button_encode_select.grid(row=2)
        
        button_encode_cancel = Button(encode_frame, text='Cancel', command=lambda : Mission_Possible.back(self,encode_frame),padx=14,bg = '#FFFFFF' )
        button_encode_cancel.config(font=('Helvetica',18),bg='#FFFFFF')
        button_encode_cancel.grid(pady=12)
        button_encode_cancel.grid(row=3)
        
        frame.destroy()
    
    #Encode: Encode Screen    
    def encode_frame2(self,frame):
        encode_frame_2= Frame(root)
        encode_frame_2.grid()
        
        input_file = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        
        if not input_file:
            messagebox.showerror("Error","Select a proper material, Agent! ")
        else:
            my_img = Image.open(input_file)
            new_image = my_img.resize((300,200))
            img = ImageTk.PhotoImage(new_image)
            
            encode_frame2_title= Label(encode_frame_2,text='Material Selected')
            encode_frame2_title.config(font=('Helvetica',25,'bold'))
            encode_frame2_title.grid(row=1)
            encode_frame2_title.grid(pady=10)
            
            board = Label(encode_frame_2, image=img)
            board.image = img
            self.output_image_size = os.stat(input_file)
            self.o_image_w, self.o_image_h = my_img.size
            board.grid(row=2)
            
            encode_frame2_subhead = Label(encode_frame_2, text='Insert your poison!')
            encode_frame2_subhead.config(font=('Helvetica',18,'bold'))
            encode_frame2_subhead.grid(row=3)
            encode_frame2_subhead.grid(pady=12)
            
            text_input = Text(encode_frame_2, width=50, height=10)
            text_input.config(font=('Helvetica',10), highlightbackground = "blue", highlightcolor= "blue")
            text_input.grid(row=4)
            
            encode_frame2_encode = Button(encode_frame_2, text='Encode', command=lambda : [self.encode_input(text_input,my_img),Mission_Possible.back(self,encode_frame_2)],padx=14,bg = '#FFFFFF')
            encode_frame2_encode.config(font=('Helvetica',18), bg='#FFFFFF')
            encode_frame2_encode.grid(row=5)
            encode_frame2_encode.grid(pady=15)
            
            encode_frame2_cancel = Button(encode_frame_2, text='Cancel', command=lambda : Mission_Possible.back(self,encode_frame_2),padx=14,bg = '#FFFFFF')
            encode_frame2_cancel.config(font=('Helvetica',18), bg='#FFFFFF')
            encode_frame2_cancel.grid(row=6)
            encode_frame2_cancel.grid(pady=15)
            
            data = text_input.get("1.0", "end-1c")
            frame.destroy()
        

    #Decode: Main Screen
    def decode_frame1(self,frame):
        decode_frame = Frame(root)
        decode_frame.grid()
        
        decode_frame1_title = Label(decode_frame, text='Pick your mystery, Agent!')
        decode_frame1_title.config(font=('Helvetica',25,'bold'))
        decode_frame1_title.grid(row=1)
        decode_frame1_title.grid(pady=80)
    
        
        button_decode_select = Button(decode_frame, text='Select', command=lambda :self.decode_frame2(decode_frame),padx=14,bg = '#FFFFFF' )
        button_decode_select.config(font=('Helvetica',18),bg='#FFFFFF')
        button_decode_select.grid(pady=12)
        button_decode_select.grid(row=2)
        
        button_decode_cancel = Button(decode_frame, text='Cancel', command=lambda : Mission_Possible.back(self,decode_frame),padx=14,bg = '#FFFFFF' )
        button_decode_cancel.config(font=('Helvetica',18),bg='#FFFFFF')
        button_decode_cancel.grid(pady=12)
        button_decode_cancel.grid(row=3)
        
        frame.destroy()

    #Decode: Decode Screen
    def decode_frame2(self,frame):
        decode_frame_2 = Frame(root)
        myfiles = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        
        if not myfiles:
            messagebox.showerror("Error","You have selected nothing! ")
        else:
            my_img = Image.open(myfiles, 'r')
            my_image = my_img.resize((300, 200))
            img = ImageTk.PhotoImage(my_image)
            label4= Label(decode_frame_2,text='Selected Image :')
            label4.config(font=('Helvetica',14,'bold'))
            label4.grid()
            board = Label(decode_frame_2, image=img)
            board.image = img
            board.grid()
            hidden_data = self.decode(my_img)
            
            label2 = Label(decode_frame_2, text='Hidden data is :')
            label2.config(font=('Helvetica',14,'bold'))
            label2.grid(pady=10)
            
            text_a = Text(decode_frame_2, width=50, height=10)
            text_a.insert(INSERT, hidden_data)
            text_a.configure(state='disabled')
            text_a.config(font=('Helvetica',20,'bold'), padx=20)
            text_a.grid()
            
            button_back = Button(decode_frame_2, text='Cancel', command= lambda :self.frame_3(decode_frame_2))
            button_back.config(font=('Helvetica',14),bg='#FFFFFF')
            button_back.grid(pady=15)
            button_back.grid()
            decode_frame_2.grid(row=1)
            frame.destroy()
            
#GUI::END ----------------------->

# Algorithm ------------------->

    #Decode Algorithm
    def decode(self, image):
            image_data = iter(image.getdata())
            data = ''

            while (True):
                pixels = [value for value in image_data.__next__()[:3] +
                            image_data.__next__()[:3] +
                            image_data.__next__()[:3]]
                binary_str = ''
                for i in pixels[:8]:
                    if i % 2 == 0:
                        binary_str += '0'
                    else:
                        binary_str += '1'

                data += chr(int(binary_str, 2))
                if pixels[-1] % 2 != 0:
                    return data
    
    #Encode Algorithm
    def generate_data(self,data):
        new_data = []
        for i in data:
            new_data.append(format(ord(i), '08b'))
        return new_data

    def modify_pixel(self,pixel, data):
        dataList = self.generate_data(data)
        dataLen = len(dataList)
        imgData = iter(pixel)
        
        for i in range(dataLen):
            pixel = [value for value in imgData.__next__()[:3] +
                    imgData.__next__()[:3] +
                    imgData.__next__()[:3]]
            
            for j in range(0, 8):
                if (dataList[i][j] == '0') and (pixel[j] % 2 != 0):
                    if (pixel[j] % 2 != 0):
                        pixel[j] -= 1

                elif (dataList[i][j] == '1') and (pixel[j] % 2 == 0):
                    pixel[j] -= 1
            
            if (i == dataLen - 1):
                if (pixel[-1] % 2 == 0):
                    pixel[-1] -= 1
            else:
                if (pixel[-1] % 2 != 0):
                    pixel[-1] -= 1

            pixel = tuple(pixel)
            yield pixel[0:3]
            yield pixel[3:6]
            yield pixel[6:9]

    def encode_data(self,newImg, data):
        w = newImg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modify_pixel(newImg.getdata(), data):

            # Putting modified pixels in the new image
            newImg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1


    def encode_input(self,textInput,myImg):
        data = textInput.get("1.0", "end-1c")
        if (len(data) == 0):
            messagebox.showinfo("Alert","Kindly enter text in TextBox")
        else:
            newImg = myImg.copy()
            self.encode_data(newImg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myImg.filename))[0]
            newImg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newImg.size
            messagebox.showinfo("Success","Encoding Successful\nMission Begin!")

    def frame_3(self,frame):
        frame.destroy()
        self.main(root)
    

#Algorithm ----------------------->

#GUI loop
root = Tk()
o = Mission_Possible()
o.main(root)
root.mainloop()

