from ham_scale import *
from tkinter import *

def Layout():
    layout = Tk()
    layout.title('FOODY SCALE 1.0')
    layout.minsize(500,500)
    layout.maxsize(500,500)
    panel_title = PanedWindow(layout,bd=4, relief="raised",bg="white")
    panel_title.place(x=0,width=500,height=60)
    panel_content = PanedWindow(layout,bd=4, relief="raised", bg="white")
    panel_content.place(x=0,y=60,width=500,height=440)
    panel_vertical_left = PanedWindow(panel_content,bd=4, relief="raised", bg="white")
    panel_vertical_left.place(x=100,y=0,width=100,height=440)
    panel_vertical_right = PanedWindow(panel_content, bd=4, relief="raised", bg="white")
    panel_vertical_right.place(x=100,y=0,width=400,height=440)
    panel_weight = PanedWindow(panel_vertical_right,bd=4, relief="raised", bg="white")
    panel_weight.place(x=0,y=0,width=400,height=220)
    panel_console = PanedWindow(panel_vertical_right,bd=4, relief="raised", bg="white")
    panel_console.place(x=0,y=220,width=400,height=220)
    x0=Label(layout, text="FOODY SCALE", font='Times 20')
    x1 = Label(panel_weight, text="Calories: ", font='Times 15')
    x1.place(x=0, y=0)
    x2 = Label(panel_weight, text="Protein: ", font='Times 15')
    x2.place(x=0, y=33)
    x3 = Label(panel_weight, text="Fat: ", font='Times 15')
    x3.place(x=0, y=66)
    x4 = Label(panel_weight, text="Satfat: ", font='Times 15')
    x4.place(x=0, y=99)
    x5 = Label(panel_weight, text="Fiber: ", font='Times 15')
    x5.place(x=0, y=132)
    x6 = Label(panel_weight, text="Carb: ", font='Times 15')
    x6.place(x=0, y=165)
    y1 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y1.place(x=90, y=0, width=290)
    y2 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y2.place(x=90, y=33, width=290)
    y3 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y3.place(x=90, y=66, width=290)
    y4 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y4.place(x=90, y=99, width=290)
    y5 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y5.place(x=90, y=132, width=290)
    y6 = Entry(panel_weight, width=10, font=('Time New Roman', 15))
    y6.place(x=90, y=165, width=290)

    # def checkvalue():
    #     if y1.get()=="":
    #         z1=0
    #     else:
    #         z1 = getdouble(y1.get())
    #     if y2.get()=="":
    #         z2=0
    #     else:
    #         z2 = getdouble(y2.get())
    #     if y3.get()=="":
    #         z3=0
    #     else:
    #         z3 = getdouble(y3.get())
    #     if y4.get()=="":
    #         z4=0
    #     else:
    #         z4 = getdouble(y4.get())
    #     if y5.get()=="":
    #         z5=0
    #     else:
    #         z5 = getdouble(y5.get())
    #     if y6.get()=="":
    #         z6=0
    #     else:
    #         z6 = getdouble(y6.get())
    #     model= scale(z1,z2,z3,z4,z5,z6)
    #     try:
    #        print(model.Obj)
    #        layout.after(1000, checkvalue)
    #     except:
    #        layout.geometry("40x400")
    #        layout.after(1, checkvalue)
    # global condition
    # layout.after(1,checkvalue)

    newwindow = Toplevel(layout)
    newwindow.title("Answer")
    newwindow.geometry("400x400")
    newwindow.maxsize(400, 400)
    newwindow.minsize(400, 400)
    newwindow.withdraw()
    console2 = Label(newwindow, text="", font='Times 15')
    console2.place(x=0, y=0)

    # check = 0
    # def tinhtoan():
    #     if check==0:
    #         tinhtoan1()
    #     else:
    #         tinhtoan2()

    def tinhtoan1():
        newwindow.geometry("400x400")
        for i in newwindow.winfo_children():
            i.destroy()
        newwindow.deiconify()
        if y1.get()=="":
            z1=0
        else:
            z1 = getdouble(y1.get())
        if y2.get()=="":
            z2=0
        else:
            z2 = getdouble(y2.get())
        if y3.get()=="":
            z3=0
        else:
            z3 = getdouble(y3.get())
        if y4.get()=="":
            z4=0
        else:
            z4 = getdouble(y4.get())
        if y5.get()=="":
            z5=0
        else:
            z5 = getdouble(y5.get())
        if y6.get()=="":
            z6=0
        else:
            z6 = getdouble(y6.get())
        model = scale(z1, z2, z3, z4, z5, z6)
        try:
            data = pd.read_csv("./nutrients_csvfile.csv")
            data1 = data.iloc[:, 0].values
            data2 = data.iloc[:, 2].values
            pos = 0
            sum = 0
            for i in range(0,335):
                weight_food = round(model.x[i+1]()*float(data2[i]),2)
                sum += weight_food
                if (weight_food > 0.0):
                    print(data1[i],': ' + str(weight_food))
                    string =str(data1[i]) + ': ' + str(weight_food) + ' gram'
                    console = Label(newwindow, text= string, font='Times 15')
                    console.place(x=0, y=pos)
                    pos+=30
            string='Sum of weight: '+ str(round(sum,2)) + ' gram'
            console = Label(newwindow, text=string, font='Times 15')
            console.place(x=0, y=pos)
        except:
            for i in newwindow.winfo_children():
                i.destroy()
            console2 = Label(newwindow, text="YOUR VALUES IS NOT WORTHY!", font='Times 15',fg='#f00')
            console2.place(x=0, y=0)

    def tinhtoan2():
        newwindow.geometry("400x400")
        for i in newwindow.winfo_children():
            i.destroy()
        newwindow.deiconify()
        if y1.get() == "":
            z1 = 0
        else:
            z1 = getdouble(y1.get())
        if y2.get() == "":
            z2 = 0
        else:
            z2 = getdouble(y2.get())
        if y3.get() == "":
            z3 = 0
        else:
            z3 = getdouble(y3.get())
        if y4.get() == "":
            z4 = 0
        else:
            z4 = getdouble(y4.get())
        if y5.get() == "":
            z5 = 0
        else:
            z5 = getdouble(y5.get())
        if y6.get() == "":
            z6 = 0
        else:
            z6 = getdouble(y6.get())
        model = scaleprice(z1, z2, z3, z4, z5, z6)
        try:
            data = pd.read_csv("./nutrients_csvfile.csv")
            data1 = data.iloc[:, 0].values
            data2 = data.iloc[:, 9].values
            pos = 0
            sum = 0
            for i in range(0, 335):
                price_food = round(model.x[i + 1]() * float(data2[i]), 2)
                sum += price_food
                if (price_food> 0.0):
                    print(data1[i], ': ' + str(price_food))
                    string = str(data1[i]) + ': ' + str(price_food) + ' $'
                    console = Label(newwindow, text=string, font='Times 15')
                    console.place(x=0, y=pos)
                    pos += 30
            string = 'Sum of price: ' + str(round(sum, 2)) + ' $'
            console = Label(newwindow, text=string, font='Times 15')
            console.place(x=0, y=pos)
        except:
            for i in newwindow.winfo_children():
                i.destroy()
            console2 = Label(newwindow, text="YOUR VALUES IS NOT WORTHY!", font='Times 15', fg='#f00')
            console2.place(x=0, y=0)

    def tinhtoan3():
        newwindow.geometry("400x400")
        for i in newwindow.winfo_children():
            i.destroy()
        newwindow.deiconify()
        if y1.get() == "":
            z1 = 0
        else:
            z1 = getdouble(y1.get())
        if y2.get() == "":
            z2 = 0
        else:
            z2 = getdouble(y2.get())
        if y3.get() == "":
            z3 = 0
        else:
            z3 = getdouble(y3.get())
        if y4.get() == "":
            z4 = 0
        else:
            z4 = getdouble(y4.get())
        if y5.get() == "":
            z5 = 0
        else:
            z5 = getdouble(y5.get())
        if y6.get() == "":
            z6 = 0
        else:
            z6 = getdouble(y6.get())
        model = scaleprice(z1, z2, z3, z4, z5, z6)
        try:
            data = pd.read_csv("./nutrients_csvfile.csv")
            data0 = data.iloc[:, 2:10].values
            data1 = data.iloc[:, 0].values
            data2 = data.iloc[:, 9].values
            pos1 = 0
            pos2 = 0
            sum = 0
            for i in range(0, 335):
                price_food = round(model.x[i + 1]() * float(data2[i]), 2)
                sum += price_food
                #pos1=0
                if (price_food > 0.0):
                    #for j in range(0,8):
                    print(data1[i], ': ' + str(price_food))
                    string = str(data1[i]) + ': ' + str(price_food) + ' $'
                    console = Label(newwindow, text=string, font='Times 15')
                    console.place(x=pos1, y=pos2)
                    pos2 += 30
                    #pos1+=30
            string = 'Sum of price: ' + str(round(sum, 2)) + ' $'
            console = Label(newwindow, text=string, font='Times 15')
            console.place(x=0, y=pos2)
        except:
            for i in newwindow.winfo_children():
                i.destroy()
            console2 = Label(newwindow, text="YOUR VALUES IS NOT WORTHY!", font='Times 15', fg='#f00')
            console2.place(x=0, y=0)


    But1=Button(panel_vertical_left,text='',width=10, height=1,background='gray')
    But1.place(x=0,y=0)

    # def change1():
    #         But2.configure(bg="gray", fg="white")
    #         But3.configure(bg="white", fg="black")
    #         check==0
    # def change2():
    #         But3.configure(bg="gray", fg="white")
    #         But2.configure(bg="white", fg="black")
    #         check==1

    But2 = Button(panel_console, text='WEIGHT', width=10, height=1,bg="gray", fg="white", command=tinhtoan1)
    But2.place(x=80,y=20)
    But3 = Button(panel_console, text='PRICE', width=10, height=1,bg="gray", fg="white", command=tinhtoan3)
    But3.place(x=220, y=20)

    panel_vertical_left.add(But1)
    panel_title.add(x0)
    panel_content.add(panel_vertical_left)
    panel_content.add(panel_vertical_right)
    return layout

if __name__ == '__main__':
    roof = Layout()
    roof.mainloop()

