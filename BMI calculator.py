"""
BMI App
Email:  atenajos@gmail.com


"""

from tkinter import*
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import simpledialog as sd
import time

import csv


class Application(Frame):  # code creates the class under Tkinter to make the gui
    def __init__(self, master):
        super(Application, self).__init__(master)
        root.withdraw()
        self.name = sd.askstring('Name', 'Enter your name')
        root.deiconify()
        self.grid()
        self.create_cascade()
        val_cmd = (self.master.register(self.callback))
        self.file_name = None

        Label(self, text='ENTER YOUR WEIGHT', bg="turquoise").grid(row=0, columnspan=6, pady=15)

        Label(self, text='Stones', bg="turquoise").grid(row=1, column=0, sticky=SE)
        self.user_stones = StringVar()
        self.entry_stones = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                                  textvariable=self.user_stones, justify='center', width=10)
        self.entry_stones.grid(row=1, column=1, ipady=5)

        Label(self, text='Pounds', bg="turquoise").grid(row=1, column=2, sticky=SE)
        self.user_pounds = StringVar()
        self.entry_pounds = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                                  textvariable=self.user_pounds, justify='center', width=10)
        self.entry_pounds.grid(row=1, column=3, ipady=5)

        Label(self, text='or KGs', bg="turquoise").grid(row=1, column=4, sticky=SE)
        self.user_kg = StringVar()
        self.entry_kg = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                              textvariable=self.user_kg, justify='center', width=10)
        self.entry_kg.grid(row=1, column=5, ipady=5)

        Label(self, text='ENTER YOUR HEIGHT', bg="turquoise").grid(row=2, columnspan=6, pady=15)

        Label(self, text='Feet', bg="turquoise").grid(row=3, column=0, sticky=SE)
        self.user_feet = StringVar()
        self.entry_feet = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                                textvariable=self.user_feet, justify='center', width=10)
        self.entry_feet.grid(row=3, column=1, ipady=5)

        Label(self, text='Inches', bg="turquoise").grid(row=3, column=2, sticky=SE)
        self.user_inches = StringVar()
        self.entry_inches = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                                  textvariable=self.user_inches, justify='center', width=10)
        self.entry_inches.grid(row=3, column=3, ipady=5)

        Label(self, text='or CM', bg="turquoise").grid(row=3, column=4, sticky=SE)
        self.user_cm = StringVar()
        self.entry_cm = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                              textvariable=self.user_cm, justify='center', width=10)
        self.entry_cm.grid(row=3, column=5, ipady=5)

        self.button_bmi = Button(self, text='Calculate Yor BMI Now', command=self.bmi_calculator,
                                 bg='green', fg='white')
        self.button_bmi.grid(row=4, columnspan=6, pady=15, ipady=6)
        self.bmi = StringVar()
        self.entry_bmi = Entry(self, validate='all', validatecommand=(val_cmd, '%P'), bd=4, fg='green',
                               textvariable=self.bmi, justify='center', width=12)
        self.entry_bmi.grid(row=5, columnspan=6, pady=12, ipady=8)

        self.reset_button = Button(self, text='Reset', command=self.reset)
        self.reset_button.grid(row=7, columnspan=6, pady=10)

        Label(self, bg="turquoise", text='Type in your weight either in stones,'
              'pounds or kilograms and\n''your height either in feet,'
              'inches or meters.').grid(row=8, columnspan=6)

        self.pack(side=TOP, padx=25)

    def callback(self, entry):  # restrict the values in the Entry widget to numbers only
        if str.isdigit(entry) or entry == "":
            return True
        else:
            return False

    def bmi_calculator(self):  # Retrieves all necessary information to calculate BMI
        if self.user_stones.get() and self.user_pounds.get():
            stones = int(self.user_stones.get()) * 6.35029318
            pounds = float(self.user_pounds.get()) * 0.45359237
            kg = stones + pounds
            self.user_kg.set(round(kg))
            feet = int(self.user_feet.get())
            inches = float(self.user_inches.get())
            inches += feet * 12
            cm = round(inches * 2.54)
            self.user_cm.set(cm)

            display_bmi = float(self.entry_kg.get()) / (int(self.entry_cm.get()) / 100) ** 2
            self.bmi.set(round(display_bmi, 2))

        else:
            display_kg = self.user_kg.get()
            display_stones = float(display_kg) / 6.35029318
            self.user_stones.set(int(display_stones))
            display_pound = (display_stones % 14) * 14
            self.user_pounds.set(round(display_pound, 4))
            display_cm = self.user_cm.get()
            display_feet = (int(display_cm) * 0.393700787) // 12
            self.user_feet.set(int(display_feet))
            display_inches = (int(display_cm) * 0.393700787) % 12
            self.user_inches.set(round(display_inches, 4))

            display_bmi = float(self.entry_kg.get()) / (int(self.entry_cm.get()) / 100) ** 2
            self.bmi.set(round(display_bmi, 2))

        if display_bmi < 18.5:  # Conditions to find out BMI category
            mb.showwarning('Body Mass Index', 'You are underweight!')
        if 18.5 <= display_bmi <= 24.99:
            mb.showinfo('Body Mass Index', 'This is the normal BMI range, great!')
        if 25 <= display_bmi <= 29.99:
            mb.showwarning('Body Mass Index', 'This is considered overweight')
        if display_bmi >= 30:
            mb.showwarning('Body Mass Index', 'This is considered obese, you should try to lose weight.')
        return

    def reset(self):   # Defining reset method
        self.user_stones.set('')
        self.user_pounds.set('')
        self.user_kg.set('')
        self.user_feet.set('')
        self.user_inches.set('')
        self.user_cm.set('')
        self.bmi.set('')

    def open_file(self):  # Defining save method
        self.file_name = fd.askopenfilename(filetypes=[('Csv files (*.csv)', ''), ("All Files", '')])

    def save_as(self):  # Defining save as method
        self.file_name = fd.asksaveasfilename(defaultextension='.csv',
                                              filetypes=[('Csv files (*.csv)', ''), ("All Files", '')])
        self.write_to_file()

    def save(self):     # Defining save method
        if self.file_name is None or self.file_name == '':
            self.save_as()
        else:
            self.write_to_file()

    def write_to_file(self):  # Defining write to file method
        current_time = time.strftime("%m/%d/%Y")
        with open(file=self.file_name, mode='w', newline='\n') as f:
            title_name = ['Date', 'Name', 'Weight(kg)', 'Height(cm)', 'Weight(st)',
                          'Weight(lbs)', 'Height(feet)', 'Height(in)', 'BMI']
            writer = csv.DictWriter(f, fieldnames=title_name)

            writer.writeheader()
            writer.writerow({'Date': current_time, 'Name': self.name.title(), 'Weight(kg)': self.entry_kg.get(),
                             'Height(cm)': self.entry_cm.get(), 'Weight(st)': self.entry_stones.get(),
                             'Weight(lbs)': self.entry_pounds.get(), 'Height(feet)': self.entry_feet.get(),
                             'Height(in)': self.entry_inches.get(), 'BMI': self.entry_bmi.get()})

    def create_cascade(self):
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)
        # File menu,for options, open file, save, save as, exit
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Options", menu=file_menu)
        file_menu.add_command(label='Open File...', command=self.open_file)
        file_menu.add_command(label='Save', command=self.save)
        file_menu.add_command(label='Save As...', command=self.save_as)
        file_menu.add_command(label='Exit', command=root.destroy)
        self.pack(side=TOP)


if __name__ == "__main__":  # Entry point
    root = Tk()
    root.title('Body Mass Index')  # Sets title
    root.geometry('400x410+483+190')  # Sets size
    root.configure(background="turquoise")
    app = Application(root)
    app.configure(background="turquoise")
    root.mainloop()
