import csv
from datetime import datetime
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox


class Pizza():
    def get_description(self):
        pass
    def get_cost(self):
        pass
   
class ClassicPizza(Pizza):
    def get_description(self):
        return "Classic pizza"
    def get_cost(self):
        return 80

class MargheritaPizza(Pizza):
    def get_description(self):
        return "Margherita pizza"
    def get_cost(self):
        return 120
    
class TurkPizza(Pizza):
    def get_description(self):
        return "Turk pizza"
    def get_cost(self):
        return 150

class PlainPizza(Pizza):
    def get_description(self):
        return "Plain pizza"
    def get_cost(self):
        return 100


class SauceDecorator:
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return f"{self.pizza.get_description()} with {self.get_sauce()} toppings"

    def get_cost(self):
        return self.pizza.get_cost() + self.get_sauce_cost()

    def get_sauce(self):
        pass

    def get_sauce_cost(self):
        pass

class Olives(SauceDecorator):
    def get_sauce(self):
        return "olives"

    def get_sauce_cost(self):
        return 10

class Mushrooms(SauceDecorator):
    def get_sauce(self):
        return "mushrooms"

    def get_sauce_cost(self):
        return 12

class GoatCheese(SauceDecorator):
    def get_sauce(self):
        return "goat cheese"

    def get_sauce_cost(self):
        return 18

class Meat(SauceDecorator):
    def get_sauce(self):
        return "meat"

    def get_sauce_cost(self):
        return 25

class Onions(SauceDecorator):
    def get_sauce(self):
        return "onions"

    def get_sauce_cost(self):
        return 11

class Corn(SauceDecorator):
    def get_sauce(self):
        return "corn"

    def get_sauce_cost(self):
        return 7
    
baseTypes = ['Classic Pizza', 'Margherita Pizza', 'Turk Pizza','Plain Pizza']
sauces = ['Olives', 'Mushrooms', 'Goat Cheese', 'Meat', 'Onions', 'Corn']


def run_order():
    baseType = combo1.get()
    sauce = combo2.get()

    my_pizza = None
    if baseType == baseTypes[0]:
        my_pizza = ClassicPizza()
    elif baseType == baseTypes[1]:
        my_pizza = MargheritaPizza()
    elif baseType == baseTypes[2]:
        my_pizza = TurkPizza()
    elif baseType == baseTypes[3]:
        my_pizza = PlainPizza()

    if sauce == sauces[0]:
        
        my_pizza = Olives(my_pizza)
    elif sauce == sauces[1]:
        my_pizza = Mushrooms(my_pizza)
    elif sauce == sauces[2]:
        my_pizza = GoatCheese(my_pizza)
    elif sauce == sauces[3]:
        my_pizza = Meat(my_pizza)
    elif sauce == sauces[4]:
        my_pizza = Onions(my_pizza)
    elif sauce == sauces[5]:
        my_pizza = Corn(my_pizza)

    
    #Orders_Database.csv
    time_stamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(my_pizza.get_description())
    print(my_pizza.get_cost())
    print(time_stamp)
    messagebox.showinfo('Your Pizza Order', f"{my_pizza.get_description()} has been ordered \n\nPrice: ₺{my_pizza.get_cost()}")

    #store order information in csv
    with open('Orders_Database.csv', 'a', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow([my_pizza.get_description(), my_pizza.get_cost(), time_stamp]) 
        csvfile.close()
    

#root window 
win = Tk()
win.title('Pizza Order System')
win.resizable(False, False) 
window_height = 200
window_width = 300
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#pizza base image
pizza_frame = Frame(win, width=300, height=200)
pizza_frame.pack()
pizza_frame.place(anchor='center', relx=0.5, rely=0.5)
pizza_image = ImageTk.PhotoImage(Image.open('pizzabase.png').resize((300,200)))
pizza_label = Label(pizza_frame, image=pizza_image, anchor='center', width=300, height=200).pack()

#choose pizza base label
pizza_label = Label(win, text='Choose Pizza Base')
pizza_label.pack(padx=(10,10), pady=(10,10))
#pizza base combo box
combo1 = ttk.Combobox(values=baseTypes)
combo1.set(baseTypes[0])
combo1.pack()

#chose sauce label
sauce_label = Label(win, text='Choose Pizza Sauce')
sauce_label.pack(padx=(10,10), pady=(10,10))
#sauce combobox
combo2 = ttk.Combobox(values=sauces)
combo2.set(sauces[0])
combo2.pack()

button = Button(win , text = "Order", command=run_order).pack(pady=(10,10))

win.mainloop()