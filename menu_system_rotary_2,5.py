from time import sleep
from rotary_encoder import RotaryEncoder

rot = RotaryEncoder()
line = 1
highlight = 1
shift = 0
list_length = 0
total_lines = 4

def show_menu(menu):
    """ Shows the menu in the shell """
    global line, highlight, shift, list_length
    item = 1  # item får 1 som startværdi
    line = 1  # linje får 1 som startværdi
    list_length = len(menu)  # antal items i listen
    
    # sørg for at de rigtige 4 items vælges
    short_list = menu[shift: shift + total_lines]
    
    # for hvert element i den korte liste
    for item in short_list:
        if highlight == line:  # hvis den nuværende linje og highlight er ens
            print(item.upper(), line - 1)  # sætter highlighted menu tekst i upper case
        else:  # ellers printes menu tekst bare normalt i lowercase
            print(item, line - 1)
        line += 1

# Get the list of menu items and display the menu
menu_items = ["menu1", "menu2", "menu3", "menu4"]
show_menu(menu_items)  # printer menuen i shell 1 gang før loop

while True:  # uendeligt while loop startes
    res = rot.re_full_step()  # gem returværdi fra metodekaldet i variablen res
    if res == -1:  # når rotary encoder drejes mod venstre
        if highlight > 1:  # hvis highlight er større end 1
            highlight -= 1  # dekrementer highlight med 1
        else:  # sørger for at der skiftes en linje op hvis vi er nået til første item
            if shift > 0:  # hvis shift er større end 0
                shift -= 1  # dekrementer shift med 1
            show_menu(menu_items)  # vis menu i shell med ny highlight

    elif res == 1:  # når rotary encoder drejes mod højre
        if highlight < total_lines:
            highlight += 1
        else:  # sørger for at der skiftes en linje ned hvis vi er nået til sidste item
            if shift + total_lines < list_length:
                shift += 1
                
            show_menu(menu_items)  # vis menu i shell med ny highlight

