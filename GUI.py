from tkinter import filedialog as fdlg
from PIL import ImageTk
import PIL
from tkinter import *
from tkinter import messagebox as mbx
from Image_Detection import *
import tensorflow as tf
from keras_preprocessing import image
from keras.datasets import cifar10

#Declaring various different fonts used in the GUI
LARGEFONT = ("Brush Script MT", 30)
BUTTONFONT = ("COPPERPLATE", 12)
RESULTFONT = ("COPPERPLATE", 18)

count = 0
cnt = 0
indices1 = 0
indices2 = 0
maxs = 0
cnts = 0
g = 0
counts = 0
classes = []
file_name = ''
accuracy = 0
res = ''
p = ''
x1 = ''

#Loading the previously created model
model = tf.keras.models.load_model('CNN_ImageProcessing_Manab.h5')

#Creating different classes for different frames to mimic the page switching mechanism
class tkinterApp(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='grey')
        self.bg1 = ImageTk.PhotoImage(file="Background.png")
        l2 = Label(self, image=self.bg1)
        l2.place(anchor='center', relx=0.5, rely=0.5)

        l1 = Label(self, text='OBJECT RECOGNITION SYSTEMS', font=LARGEFONT, bg='grey')
        l1.place(anchor='center', relx=0.5, rely=0.1)

        b1 = Button(self, text='Choose Files', command=lambda: controller.show_frame(Page1), font=BUTTONFONT,
                    bg='grey', activebackground='grey', width=12)
        b1.place(anchor='e', relx=0.3, rely=0.9)

        b2 = Button(self, text='Live Feed', command=live_feed, font=BUTTONFONT, bg='grey', activebackground='grey',
                    width=10)
        b2.place(anchor='e', relx=0.9, rely=0.9)


class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='grey')

        l1 = Label(self, text='OBJECT RECOGNITION SYSTEMS', font=LARGEFONT, bg='grey')
        l1.place(anchor='center', relx=0.5, rely=0.1)

        c1 = Canvas(self, height=300, width=300, bg='grey', bd=20)
        c1.place(anchor='center', relx=0.5, rely=0.5)

        l2 = Label(self, text='INSERT YOUR IMAGE HERE', font=BUTTONFONT, bg='grey')
        l2.place(anchor='center', relx=0.5, rely=0.5)

        def files():
            global count, file_name
            file_name = fdlg.askopenfilename(title='Open a file')
            if not str(file_name).endswith('.png'):
                mbx.showerror('Error', 'Wrong file type or no file found. Only ".png" files allowed.')
            else:
                count += 1
                image2 = PIL.ImageTk.Image.open(file_name)
                image2 = image2.resize((300, 300), PIL.ImageTk.Image.ANTIALIAS)
                self.bg2 = ImageTk.PhotoImage(image2)
                l3 = Label(self, image=self.bg2)
                l3.place(anchor='center', relx=0.5, rely=0.5)

        def Page2_Proceed():
            global count
            if count == 1:
                count = 0
                c2 = Canvas(self, height=300, width=300, bg='grey', bd=20)
                c2.place(anchor='center', relx=0.5, rely=0.5)
                l4 = Label(self, text='INSERT YOUR IMAGE HERE', font=BUTTONFONT, bg='grey')
                l4.place(anchor='center', relx=0.5, rely=0.5)
                controller.show_frame(Page2)
            else:
                mbx.showerror("Error", "Please select a file before proceeding ahead.")

        def Startpage_Proceed():
            global count
            count = 0
            c3 = Canvas(self, height=300, width=300, bg='grey', bd=20)
            c3.place(anchor='center', relx=0.5, rely=0.5)
            l5 = Label(self, text='INSERT YOUR IMAGE HERE', font=BUTTONFONT, bg='grey')
            l5.place(anchor='center', relx=0.5, rely=0.5)
            controller.show_frame(StartPage)

        b1 = Button(self, text='File Explorer', command=files, font=BUTTONFONT,
                    bg='grey', activebackground='grey', width=12)
        b1.place(anchor='e', relx=0.3, rely=0.9)

        b2 = Button(self, text='Back', command=Startpage_Proceed, font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=10)
        b2.place(anchor='e', relx=0.88, rely=0.9)

        b3 = Button(self, text='Proceed', command=Page2_Proceed, font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=10)
        b3.place(anchor='e', relx=0.59, rely=0.9)


class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='grey')

        global cnt, file_name

        l1 = Label(self, text='OBJECT RECOGNITION SYSTEMS', font=LARGEFONT, bg='grey')
        l1.place(anchor='center', relx=0.5, rely=0.1)

        c1 = Canvas(self, height=300, width=400, bg='grey', bd=20, highlightcolor='grey')
        c1.place(anchor='center', relx=0.5, rely=0.5)

        def test():
            global accuracy, indices1, indices2, maxs, classes, g, res, cnt, counts, x1, p
            cnt = 1

            '''
            #If the code below has errors in resizing the image, this is a backup code for the same, performs the same actions as below.
            
            im = PIL.ImageTk.Image.open("Bicycle_Testing.png")
            # the input image is required to be in the shape of dataset, i.e (32,32,3)
            results = {0: 'aeroplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse',
                       8: 'ship', 9: 'truck'}
            im = im.resize((32, 32))
            im = np.expand_dims(im, axis=0)
            im = np.array(im)
            predictions = (model.predict([im])[0] > 0.5).astype("int32")
            prds = results[predictions]
            '''
            '''
            def Filename_Create(x):
                global counts, x1
                x = file_name
                for i in range(len(x)):
                    if x[i] == '/':
                        counts += 1
                        x = x[i:]
                        Filename_Create(x)
                    else:
                        x1 = x
                        print(x1, file=f)
                        return x1

            p = Filename_Create(file_name)
            f = open('test.txt', 'w')
            print(file_name, file=f)
            '''
            global file_name
            # Give the link of the image here to test
            test_image1 = image.load_img(file_name, target_size=(32, 32))
            test_image = image.img_to_array(test_image1)
            test_image = np.expand_dims(test_image, axis=0)
            result = model.predict(test_image)

            if result[0][0] == max(result[0]):
                accuracy = int(result[0][0] * 100)
                res = '   Aeroplane :\n'
            elif result[0][1] == max(result[0]):
                accuracy = int(result[0][1] * 100)
                res = '   Automobile :\n'
            elif result[0][2] == max(result[0]):
                accuracy = int(result[0][2] * 100)
                res = 'Bird :\n'
            elif result[0][3] == max(result[0]):
                accuracy = int(result[0][3] * 100)
                res = 'Cat :\n'
            elif result[0][4] == max(result[0]):
                accuracy = int(result[0][4] * 100)
                res = 'Deer :\n'
            elif result[0][5] == max(result[0]):
                accuracy = int(result[0][5] * 100)
                res = 'Dog :\n'
            elif result[0][6] == max(result[0]):
                accuracy = int(result[0][6] * 100)
                res = 'Frog :\n'
            elif result[0][7] == max(result[0]):
                accuracy = int(result[0][7] * 100)
                res = 'Horse :\n'
            elif result[0][8] == max(result[0]):
                accuracy = int(result[0][8] * 100)
                res = 'Ship :\n'
            elif result[0][9] == max(result[0]):
                accuracy = int(result[0][9] * 100)
                res = 'Truck :\n'
            else:
                res = 'Error!!'

            image3 = PIL.ImageTk.Image.open(file_name)
            image3 = image3.resize((400, 300), PIL.ImageTk.Image.ANTIALIAS)
            self.bg3 = ImageTk.PhotoImage(image3)
            l3 = Label(self, image=self.bg3)
            l3.place(anchor='center', relx=0.5, rely=0.5)

            l4 = Label(self, text=res + str(accuracy)+'%', font=RESULTFONT, bg='grey')
            l4.place(anchor='center', relx=0.5, rely=0.9)

            '''
            l5 = Label(self, text=str(accuracy) + '%', font=RESULTFONT, bg='grey')
            l5.place(anchor='center', relx=0.6, rely=0.9)
            '''

        def page1_proceed():
            c2 = Canvas(self, height=10, width=170, bg='grey', bd=20)
            c2.place(anchor='center', relx=0.5, rely=0.9)
            f2 = Frame(self, height=100, width=240, bg='grey')
            f2.place(anchor='center', relx=0.5, rely=0.9)
            controller.show_frame(Page1)

        b1 = Button(self, text='Results', command=test, font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=12)
        b1.place(anchor='e', relx=0.3, rely=0.9)

        b2 = Button(self, text='Back', command=page1_proceed, font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=10)
        b2.place(anchor='e', relx=0.88, rely=0.9)


root = tkinterApp()
root.geometry('600x600')
root.title("Object Recognition Systems")
root.mainloop()
