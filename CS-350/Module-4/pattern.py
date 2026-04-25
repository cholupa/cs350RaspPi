#a small module for a new bit patterns 
#Adafruit Basic LCD screen
# to be used in conjunction with the adafruit_character_lcd package
row0 = 0b11111
row1 = 0b01110
row2 = 0b00100
row3 = 0b00100
row4 = 0b011110
row5 = 0b11111
row6 = 0b11011
row7 = 0b10101

pattern = [
    row0, #row0
    row1, #row1
    row2, #row2
    row3, #row3
    row4, #row4
    row5, #row5
    row6, #row6
    row7, #row7
]

def shift(bit,dir,value):
    new_bit = 0
    match(dir):
        case "left":
            pass
        case "right":
            pass
    return new_bit
