from machine import Pin

led1 = Pin(26, Pin.OUT)

def isr_handler_function(pin_obj):
    print("pressed")
    led1.value(not led1.value())
    
rotary_pushbutton = Pin(14, Pin.IN)
print(rotary_pushbutton.value())
rotary_pushbutton.irq(isr_handler_function, trigger=Pin.IRQ_FALLING)