from tkinter import filedialog as fdlg
from PIL import ImageTk
import PIL.Image
from tkinter import *
#from CNN import *
from tkinter import messagebox as mbx
from Image_Detection import *
import tensorflow as tf
import keras

LARGEFONT = ("Brush Script MT", 30)
BUTTONFONT = ("COPPERPLATE", 12)
count = 0


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
            global count
            file_name = fdlg.askopenfilename(title='Open a file')
            if not str(file_name).endswith('.png'):
                mbx.showerror('Error', 'Wrong file type or no file found. Only ".png" files allowed.')
            else:
                count += 1
                image = PIL.Image.open(file_name)
                image = image.resize((300, 300), PIL.Image.ANTIALIAS)
                self.bg2 = ImageTk.PhotoImage(image)
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
                    bg='grey', activebackground='grey',width=12)
        b1.place(anchor='e', relx=0.3, rely=0.9)

        b2 = Button(self, text='Back', command=Startpage_Proceed, font=BUTTONFONT, bg='grey',
                    activebackground='grey',width=10)
        b2.place(anchor='e', relx=0.88, rely=0.9)

        b3 = Button(self, text='Proceed', command=Page2_Proceed, font=BUTTONFONT, bg='grey',
                    activebackground='grey',width=10)
        b3.place(anchor='e', relx=0.59, rely=0.9)


class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.configure(bg='grey')

        l1 = Label(self, text='OBJECT RECOGNITION SYSTEMS', font=LARGEFONT, bg='grey')
        l1.place(anchor='center', relx=0.5, rely=0.1)

        c1 = Canvas(self, height=300, width=300, bg='grey', bd=20)
        c1.place(anchor='center', relx=0.5, rely=0.5)

        b1 = Button(self, text='Back', command=lambda: controller.show_frame(Page1), font=BUTTONFONT, bg='grey',
                    activebackground='grey', width=10)
        b1.place(anchor='e', relx=0.88, rely=0.9)


root = tkinterApp()
root.geometry('600x600')
root.title("Object Recognition Systems")
root.mainloop()


'''
sunflower_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/592px-Red_sunflower.jpg"
sunflower_path = tf.keras.utils.get_file('Red_sunflower', origin=sunflower_url)

img = keras.preprocessing.image.load_img(
    sunflower_path, target_size=(32, 32)
)
img_array = keras.preprocessing.image.img_to_array(img)
img_array = tf.expand_dims(img_array, 0) # Create a batch

predictions = model.predict(img_array)
score = tf.nn.softmax(predictions[0])

print(
    "This image most likely belongs to {} with a {:.2f} percent confidence."
    .format([np.argmax(score)], 100 * np.max(score)))
'''