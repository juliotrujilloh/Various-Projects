#How NOT to give instructions to a programmer...lol

you_see_avocados = True
bring = 0

def wife_said_go_to_supermarket_to_get_milk():
    global bring
    if you_see_avocados:
        bring +=2
    return bring

def hubby_went_to_supermarket_to_get_milk():
    global brought
    milk = 0
    brought = bring + milk


wife_said_go_to_supermarket_to_get_milk()
hubby_went_to_supermarket_to_get_milk()

print("Hubby brought", brought,"Milk cartons")
