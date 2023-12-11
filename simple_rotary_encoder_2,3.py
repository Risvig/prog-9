from rotary_encoder import RotaryEncoder
from machine import Pin

print("Rotary encoder test program\n")
testing = True
rot = RotaryEncoder()

while testing:
    res = rot.re_full_step()
    rot.counter += res
    if res == 1:
        print("Right/CW:", rot.counter)
    elif res == -1:
        print("Left/CCW:", rot.counter)