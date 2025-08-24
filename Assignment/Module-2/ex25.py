x = 25

print("X :",x)

def val():
    global x        # Important 
    x += 10
    print("X :",x)

val()