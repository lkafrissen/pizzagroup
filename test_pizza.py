"""
Test for pizza program
"""

import pizza as pi
import random as ra
def test_add():
    toppings=pi.Toppings()
    temp_top=[]
    for i in range(0,10):
        new_top=ra.choice(toppings.toppings)
        if new_top not in temp_top:
            temp_top.append(new_top)
            toppings.selected.set(new_top)
            toppings.add_button.invoke()
    shown_top=toppings.toppings_wid.get("1.0", pi.tk.END).split("\n")
    shown_top=[element for element in shown_top if element !=""]
    assert toppings.your_toppings==temp_top
    assert shown_top==toppings.your_toppings
    

def test_remove():
    toppings=pi.Toppings()
    temp_top=toppings.toppings
    for element in temp_top:
        toppings.selected.set(element)
        toppings.add_button.invoke()
    for i in range(0,10):
        new_top=ra.choice(toppings.toppings)
        if new_top in temp_top:
            temp_top.remove(new_top)
            toppings.selected.set(new_top)
            toppings.remove_button.invoke()
    shown_top=toppings.toppings_wid.get("1.0", pi.tk.END).split("\n")
    shown_top=[element for element in shown_top if element !=""]
    assert toppings.your_toppings==temp_top
    assert shown_top==toppings.your_toppings
    