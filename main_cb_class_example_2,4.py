from machine import Pin
from cb_handler_class import CallbackHandlerExample

rotary_encoder_pushbutton = Pin (14, Pin. IN) # instans af pin klassen til encoder knap

cb_handler = CallbackHandlerExample (rotary_encoder_pushbutton) # instans af callback eksempel klassen

def test_callback_1(): # callback funktion 1 som passeres til objektets metode som argument print("cb1 called")
    print("cb1 called")

def test_callback_2(): # callback funktion 2 som passeres til objektets metode som argument print("cb2 called")
    print("cb2 called")


cb_handler.add_menu("test1", test_callback_1) # metodekald der tilfjøjer tekst og callback funktion til objektets liste cb_handler.add_menu("test1", test_callback_2) # metodekald der tilfjøjer tekst og callback funktion til objektets liste
cb_handler.add_menu("test1", test_callback_2) # metodekald der tilfjøjer tekst og callback funktion til objektets liste cb_handler.add_menu("test1", test_callback_2) # metodekald der tilfjøjer tekst og callback funktion til objektets liste
cb_handler.run()