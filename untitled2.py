from tkinter import*

root = Tk()
root.title("Sales Generator")
root.geometry("400x400")

months = Label(root)
months.place(relx="0.5", rely="0.4", anchor=CENTER)
profits = Label(root)
profits.place(relx="0.5", rely="0.5", anchor=CENTER)
max_profit = Label(root)
max_profit.place(relx="0.5", rely="0.6", anchor=CENTER)
min_profit = Label(root)
min_profit.place(relx="0.5", rely="0.7")

months["text"] = "Months:" + str(monthss)

profits["text"] = "profits:" + str(profitss)

monthss = ("January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profitss = (566655, 61000, 7081, 111111, 321000, 234567, 898989, 76543, 99999, 454545, 12345, 10000)

def maximumprofit():
    max_profit = max(profitss)
    max_profit_index = profitss.index(max_profit)
    max_profit_month = monthss[max_profit_index]
    
def minimumprofit():
    min_profit = min(profitss)
    min_profit_index = profitss.index(min_profit)
    min_profit_month = monthss[min_profit_index]

btn1 = Button(root, text="Get Maxiumum profit", command=maximumprofit)
btn1.place(relx="0.5", rely="0.2", anchor="CENTER")

btn2 = Button(root, text="Get Minimum profit", command=minimumprofit)

root.mainloop()