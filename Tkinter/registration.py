from tkinter import *
from tkinter import messagebox
from PIL import ImageTk   # pip3 install pillow

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Page")  # For Title of the page
        self.root.geometry("1350x700+0+0")    # Resolution of the page , top, bottom
        self.root.config(bg="white")

        # ===BackGround Image===
        self.bg = ImageTk.PhotoImage(file="D:/Downloads/DL_Lab/back.png")
        bg = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===Register Frame===
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=20, width=700, height=550)

        title = Label(frame1, text="Register Here", font=("times new roman", 20, "bold"), bg="white", fg="green").place(x=270, y=15)

        # --------Name
        f_name = Label(frame1, text="Name", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=60)
        self.txt_fname = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_fname.place(x=220, y=60, width=250)
        
        # --------Roll Number
        roll = Label(frame1, text="Roll Number", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
        self.txt_roll = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_roll.place(x=220, y=100, width=250)

        # --------Year of Study
        yos = Label(frame1, text="Year of Study", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=140)
        self.yos = StringVar()
        year = ['Select', 'Ist', 'IInd', 'IIIrd', 'IVth']
        self.yos.set('Select year')
        self.drop = OptionMenu(frame1, self.yos, *year)
        self.drop.place(x=220, y=140, width=250)

        # --------Branch
        branch = Label(frame1, text="Branch of Study", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
        self.bos = StringVar()
        branch = ["Select", "Civil", "CSE", "CSE-AI&ML", "ECE", "EEE", "IT", "Mech"]
        self.bos.set('Select branch')
        self.drop1 = OptionMenu(frame1, self.bos, *branch)
        self.drop1.place(x=220, y=180, width=250)

        # -------Contact
        contact = Label(frame1, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
        self.txt_contact = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=220, y=220, width=250)

        # -------Email
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
        self.txt_email = Entry(frame1, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=220, y=260, width=250)

        # -------Gender
        gender = Label(frame1, text="Gender", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=300)
        self.var = IntVar()
        self.male = Radiobutton(frame1, text="Male", variable=self.var, value=1, font=("times new roman", 15))
        self.female = Radiobutton(frame1, text="Female", variable=self.var, value=2, font=("times new roman", 15))
        self.other = Radiobutton(frame1, text="Other", variable=self.var, value=3, font=("times new roman", 15))
        dic1 = {"0":"None","1":"Male","2":"Female","3":"Other"}
        self.gen = dic1[str(self.var.get())]
        self.male.place(x=220,y=300)
        self.female.place(x=320,y=300)
        self.other.place(x=440,y=300)

        # ---------Password
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=340)
        self.txt_password = Entry(frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=220, y=340, width=250)

        # --------Confirm Password
        cpassword = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=380)
        self.txt_cpassword = Entry(frame1, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_cpassword.place(x=220, y=380, width=250)

        # Register Button with Image
        self.btn_img = ImageTk.PhotoImage(file="D:/Downloads/DL_Lab/register.png")
        btn_register = Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=420)

    def register_data(self):

        if self.txt_fname.get() == "" or self.yos.get() == "" or self.bos.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.var.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror("Error !", "All Fields are Required !", parent=self.root)
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error !", "Password Didn't Match !", parent=self.root)
        else:
            name = self.txt_fname.get()
            roll = self.txt_roll.get()
            yos = self.yos.get()
            branch = self.bos.get()
            contact = self.txt_contact.get()
            email = self.txt_email.get()
            dic1 = {"0":"None","1":"Male","2":"Female"}
            gender = dic1[str(self.var.get())]
            email = self.txt_email.get()
            st = "Details entered are :\n\nName :"+name+"\n\nRoll Number : "+roll+"\n\nYear : "+yos+"\n\nBranch : "+branch+"\n\nContact No. : "+contact+"\n\nEmail : "+email+"\n\nGender : "+gender
            self.msgbx = messagebox.showinfo("Registration Successful",st)


root = Tk()
obj = Register(root)
root.mainloop()