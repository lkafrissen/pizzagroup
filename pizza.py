"""
Rabecka Moffit
CS 162

Work with other people in the class (shared folder, email,
telephone, telepathy, IP over Avian Carriers, or whatever) to:
implement your assigned component(s), but do not worry too much if
it does not end up properly interacting with each other as we will
expand on this in the next project,
Create a basic GUI that displays the attributes of your component
(it does not need to be an interactive GUI yet, just set some text
on a label or textbox as the program starts up,
Note: I recommend using tkinter as it is built in to Python, but
we could experiment with other GUI frameworks or libraries as well
Include in a README file the perceived contribution of your fellow
teammates
Attempt to implement the tests that your team came up with as PyTest
tests (and more as you think of them), but if you need to rely on
simpler functions that act as tests instead of PyTest, that is okay too,
Be ready to discuss how things go with your team when we next meet.
"""


import tkinter as tk

class Toppings():
    
    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Order")

        self.window=tk.Frame(self.root, width=500, height=600)
        self.window.pack()
        self.window.configure(bg='light slate gray')

        self.toppings=["pepperoni", "canadian bacon", "bacon", "sausage",
                  "linguica", "ground beef", "taco meat", "chicken",
                  "mushrooms", "green peppers", "black olives", "white onions",
                  "red onions", "jalapenos", "pineapple", "marinated onions",
                  "kalamata olives", "peppercinis", "spinach", "tomatoes",
                  "garlic"]
        self.toppings.sort()
        self.selected=tk.StringVar(self.root)
        self.selected.set("Create a Pizza")

        self.your_toppings=[]
        
        self.toppings_wid=tk.Text(self.root, height=10, width=20)
        self.toppings_wid.place(x=150, y=250)

        self.title=tk.Label(self.root, text="Add or remove the toppings you \
want on your pizza")
        self.title.pack()
        self.title.place(x=75, y=0)

        self.create_button=tk.OptionMenu(self.root, self.selected, *self.toppings)
        self.create_button.place(x=180, y=50)

        self.add_button=tk.Button(self.root, text="Add Topping", command=self.add_toppings)
        self.add_button.place(x=75, y=150)

        self.remove_button=tk.Button(self.root, text="Remove Topping", command=self.delete_button)
        self.remove_button.place(x=300, y=150)


        self.quit_button=tk.Button(self.root, text="Click here to close", command=self.close)
        self.quit_button.place(x=180, y=550)
        
    def add_toppings(self):
        toppings_chosen=self.selected.get()
        self.your_toppings.append(toppings_chosen)
        insert=toppings_chosen+ "\n"
        self.toppings_wid.insert(tk.END, insert)
        return self.your_toppings

    def delete_button(self):
        toppings_removed=self.selected.get()
        self.your_toppings.remove(toppings_removed)
        self.toppings_wid.delete("1.0", tk.END)
        for element in self.your_toppings:
            insert= element + "\n"
            self.toppings_wid.insert(tk.END, insert)
        return self.your_toppings
    
    def close(self):
        self.root.destroy()
        
def main():
    calling=Toppings()
    
if __name__=="__main__":
    main()