from tkinter import filedialog as fdlg
from PIL import ImageTk
import PIL
from tkinter import *
from tkinter import messagebox as mbx
from Image_Detection import *
import tensorflow as tf
from keras_preprocessing import image
import keras

LARGEFONT = ("Brush Script MT", 30)
BUTTONFONT = ("COPPERPLATE", 12)
RESULTFONT = ("COPPERPLATE", 18)
count = 0
file_name = ''
accuracy = ''
cnts = 0

from keras.datasets import cifar100

# loading in the data
(X_train, y_train), (X_test, y_test) = cifar100.load_data()

model = tf.keras.models.load_model('CNN_ImageProcessing_Manab.h5')


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
        self.bg1 = PhotoImage(file="Background.png")
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
                image2 = PIL.Image.open(file_name)
                image2 = image2.resize((300, 300), PIL.Image.ANTIALIAS)
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

        l1 = Label(self, text='OBJECT RECOGNITION SYSTEMS', font=LARGEFONT, bg='grey')
        l1.place(anchor='center', relx=0.5, rely=0.1)

        c1 = Canvas(self, height=300, width=400, bg='grey', bd=20,  highlightcolor='green')
        c1.place(anchor='center', relx=0.5, rely=0.5)

        cnt = 0

        def test():
            global file_name, accuracy
            nonlocal cnt
            cnt = 1
            '''
            im = PIL.Image.open("Testing_Car.png")
            # the input image is required to be in the shape of dataset, i.e (32,32,3)
            results = {0: 'aeroplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse',
                       8: 'ship',
                       9: 'truck'}

            im = im.resize((32, 32))
            im = np.expand_dims(im, axis=0)
            im = np.array(im)
            predictions = (model.predict([im])[0] > 0.5).astype("int32")
            prds = results[predictions]
            '''
            # Give the link of the image here to test
            test_image1 = image.load_img('Face_Testing.png', target_size=(32, 32))
            test_image = image.img_to_array(test_image1)
            test_image = np.expand_dims(test_image, axis=0)
            result = model.predict(test_image)
            #prds = result
            if 1 >= result[0][0] >= 0.8:
                prds = "Aeroplane:"
                accuracy = str(result[0][0]*100)+'%'
            elif 1 >= result[0][1] >= 0.8:
                prds = 'Automobile:'
                accuracy = str(result[0][1] * 100)+'%'
            elif 1 >= result[0][2] >= 0.8:
                prds = 'Bird:'
                accuracy = str(result[0][2] * 100)+'%'
            elif 1 >= result[0][3] >= 0.8:
                prds = 'Cat:'
                accuracy = str(result[0][3] * 100)+'%'
            elif 1 >= result[0][4] >= 0.8:
                prds = 'Deer:'
                accuracy = str(result[0][4] * 100)+'%'
            elif 1 >= result[0][5] >= 0.8:
                prds = 'Dog:'
                accuracy = str(result[0][5] * 100)+'%'
            elif 1 >= result[0][6] >= 0.8:
                prds = 'Frog:'
                accuracy = str(result[0][6] * 100)+'%'
            elif 1 >= result[0][7] >= 0.8:
                prds = 'Horse:'
                accuracy = str(result[0][7] * 100)+'%'
            elif 1 >= result[0][8] >= 0.8:
                prds = 'Ship:'
                accuracy = str(result[0][8] * 100)+'%'
            elif 1 >= result[0][9] >= 0.8:
                prds = 'Truck:'
                accuracy = str(result[0][9] * 100)+'%'
            else:
                prds = 'Error'

            l4 = Label(self, text=prds, font=RESULTFONT, bg='grey', width='11')
            l4.place(anchor='center', relx=0.5, rely=0.2)

            '''
            l5 = Label(self, text=accuracy, font=RESULTFONT, bg='grey', width='11')
            l5.place(anchor='center', relx=0.7, rely=0.2)
            '''

            image3 = PIL.Image.open('Face_Testing.png')
            image3 = image3.resize((400, 300), PIL.Image.ANTIALIAS)
            self.bg3 = ImageTk.PhotoImage(image3)
            l3 = Label(self, image=self.bg3)
            l3.place(anchor='center', relx=0.5, rely=0.5)

        b1 = Button(self, text='Results', command=test, font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=12)
        b1.place(anchor='e', relx=0.3, rely=0.9)

        if cnt == 1:
            cnt = 0
            c2 = Canvas(self, height=300, width=400, bg='grey', bd=20)
            c2.place(anchor='center', relx=0.5, rely=0.5)

        b2 = Button(self, text='Back', command=lambda: controller.show_frame(Page1), font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=10)
        b2.place(anchor='e', relx=0.88, rely=0.9)


root = tkinterApp()
root.geometry('600x600')
root.title("Object Recognition Systems")
root.mainloop()
