from tkinter import *

# Day of the Week Calculator


class Dayoftheweek(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("425x625")
        self.master.title("Day of the Week Calculator")
        self.grid()

        self.title = Label(self, text="Day of the Week", fg="sea green", font=('Algerian',20))
        self.title.grid(row=1, column=1)
        self.title2 = self.title = Label(self, text="Calculator", fg="sea green", font=('Algerian',20))
        self.title2.grid(row=1, column=2) 

#Lists
        self.month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
        self.day_list = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
        self.doomsday_list = (0,3,28,14,4,9,6,11,8,5,10,7,12)
        self.century_list = (5,3,2,0)
        self.month_day_list = (31,29,31,30,31,30,31,31,30,31,30,31)

#Month
        self.month_title = Label(self, text='Month', fg="steel blue", font=('Baskerville Old Face',20,'bold'))
        self.month_title.grid(column=1, row=4)

        self.month_text_var = StringVar()
        
        self.month = Menubutton(self, relief=SUNKEN, textvariable = self.month_text_var, width=19, bg='white')
        self.month.grid(column=2, row=4)

        self.month_var = StringVar()

        self.month.menu = Menu(self.month, tearoff=0)
        self.month['menu'] = self.month.menu

        for m in self.month_list:
            self.month.menu.add_radiobutton(label=m,variable=self.month_var, value=self.month_list.index(m)+1, command=self.month_change)

#Day
        self.day_title = Label(self, text='Day', fg="steel blue", font=('Baskerville Old Face',20,'bold'))
        self.day_title.grid(column=1, row=5)

        self.day = Entry(self, justify=CENTER)
        self.day.grid(column=2, row=5)

#Year
        self.year_title = Label(self, text='Year', fg="steel blue", font=('Baskerville Old Face',20,'bold'))
        self.year_title.grid(column=1, row=6)

        self.year = Entry(self, justify=CENTER)
        self.year.grid(column=2, row=6)
#Submit
        self.button_submit = Button(self, relief=RAISED, text='Submit', command=self.submit_click, fg="firebrick3", font=('Baskerville Old Face',16,'bold'))
        self.button_submit.grid(column=2)

#lines
        self.lines = Label(self, text='='*27, fg="sea green", font=('Baskerville Old Face',20,'bold'))
        self.lines.grid(row=0,columnspan=3)
        self.lines1 = Label(self, text='='*27, fg="sea green", font=('Baskerville Old Face',20,'bold'))
        self.lines1.grid(row=3,columnspan=3)
        self.lines2 = Label(self, text='='*27, fg="sea green", font=('Baskerville Old Face',20,'bold'))
        self.lines2.grid(columnspan=3)
#Answer
        self.answer_var = StringVar()
        self.answer = Label(self, textvariable = self.answer_var, fg="steel blue", font=('Baskerville Old Face',20,'bold'))
        self.answer.grid(column=1, columnspan=2)

        self.cal_var = StringVar()
        self.cal = Label(self, textvariable = self.cal_var, fg="firebrick3", font=('Baskerville Old Face',14,'bold'))
        self.cal.grid(column=1, columnspan=2)

        self.lines3 = Label(self, text='='*27, fg="sea green", font=('Baskerville Old Face',20,'bold'))
        self.lines3.grid(columnspan=3)
#Interesting Dates
        color = "black"
        self.int_title = Label(self, text="Some interesting dates to consider", fg=color, font=('Baskerville Old Face',14,'bold underline'))
        self.int_title.grid(column=1, columnspan=2)
        self.int_1 = Label(self, text="September 2, 1752", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_1.grid(column=1, columnspan=2)
        self.int_2 = Label(self, text="September 8, 1752", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_2.grid(column=1, columnspan=2)
        self.int_3 = Label(self, text="September 14, 1752", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_3.grid(column=1, columnspan=2)
        self.int_4 = Label(self, text="February 29, 1700", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_4.grid(column=1, columnspan=2)
        self.int_5 = Label(self, text="February 29, 1800", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_5.grid(column=1, columnspan=2)
        self.int_6 = Label(self, text="Negative years (BC)", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_6.grid(column=1, columnspan=2)
        self.int_7 = Label(self, text="June 10, 5000", fg=color, font=('Baskerville Old Face',12,'bold'))
        self.int_7.grid(column=1, columnspan=2)
        

    def month_change(self):
        self.month_text_var.set(self.month_list[eval(self.month_var.get())-1])

        self.day_text_var = StringVar()
        self.month_day = Menubutton(self, relief=SUNKEN, textvariable = self.day_text_var, width=19, bg='white')
        self.month_day.grid(column=2, row=5)

        self.day_var = StringVar()

        self.month_day.menu = Menu(self.month_day, tearoff=0)
        self.month_day['menu'] = self.month_day.menu

        for d in range(1,self.month_day_list[eval(self.month_var.get())-1]+1):
            self.month_day.menu.add_radiobutton(label=d,variable=self.day_var, value=d, command=self.day_change)
        
    def day_change(self):
        self.day_text_var.set(self.day_var.get())
        

    def submit_click(self):
        try:
            a = eval(self.month_var.get())      #1-12 corresponding to month
            b = eval(self.day_var.get())        #1-31 corresponding to day
            c = eval(self.year.get())           #year
        except Exception:
            self.answer_var.set("")
            self.cal_var.set("Please provide a full date")
            
    # Leap year
        else:
            j = self.doomsday_list[a]

            if c % 4 == 0:
                if c < 1752 or (c % 100 != 0 or c % 400 == 0):
                    if a == 1 or a == 2:
                        j += 1

    # Deviation from doomsday
            d = (b - j) % 7           
    # Century code

            if 1752 < c < 3000 or (c == 1752 and (a > 9 or (a == 9 and b >= 14))):
                e = self.century_list[((c // 100)-2)%4]
                self.cal_var.set("Gregorian Calendar")
            elif c >= 3000:
                e = self.century_list[((c // 100)-2)%4]
                self.cal_var.set("Gregorian Calendar?")
            else:
                e = (-(c // 100))%7
                self.cal_var.set("Julian Calendar")
    # Others
            f = (c % 100) // 12
            g = (c % 100) % 12
            h = g // 4
            i = (d+e+f+g+h)%7


            if c == 1752 and a == 9 and 2 < b < 14:
                self.answer_var.set("No such day")
                self.cal_var.set("Really, look it up!")
            elif -753 <= c < -46:
                self.answer_var.set("Out of range")
                self.cal_var.set("Roman Calendar")
            elif c < -753:
                self.answer_var.set("Out of range")
                self.cal_var.set("Stars and Shadows")
            elif c >= 5000:
                self.answer_var.set("Angelicaday")
                self.cal_var.set("The Future Calendar")
            elif c % 4 != 0 or (c > 1752 and (c % 100 == 0 and c % 400 != 0)):
                if a == 2 and b == 29:
                    self.answer_var.set("Try March 1st")
                    self.cal_var.set("Not a Leap Year")
                else:
                    self.answer_var.set(self.day_list[i])
            else:
                self.answer_var.set(self.day_list[i])
    
        


frame01 = Dayoftheweek()
frame01.mainloop()
