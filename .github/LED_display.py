dic = {1:"  #  #  #  #  #", 2:"###  #####  ###", 
       3:"###  ####  ####", 4:"# ## ####  #  #",
       5:"####  ###  ####", 6:"####  #### ####",
       7:"###  #  #  #  #", 8:"#### ##### ####",
       9:"#### ####  ####", 0:"#### ## ## ####"}

def ask_number():
    global number
    number = input("Type a number, no negatives allowed: ")
    
    #coded the exception of negatives or any other symbol in the typing area
    while number.isdigit() == False:
        number = input("Just positive numbers allowed man! Now type: ")
    else:
         return number
    
def create_led():
    global ledlist
    #iterate the number(as string)
    ledlist= []
    for x in number:
        ledlist.append(dic[int(x)])  #convert it to integer to be able to search for it in dictionary and added to list.
    return ledlist

def display_led():
    #print("\n".join(ledlist)) #used as reference to know what i was doing
    #print(ledlist) #same thing
    count = 0                                   #Used a counter to iterate on all the elements from ledlist
    list = []                                   #Created lists to cut the parts of the number
    list_2 = []                                 #Since all the numbers are 5 lines equal, I used 5 lists
    list_3 = []   
    list_4 = []
    list_5 = []

    for element in ledlist:
        list.append(ledlist[count][0:3])        #So, we iterate trough ledlist and cut the parts of it
        list_2.append(ledlist[count][3:6])      #then each part is added to other list individualy
        list_3.append(ledlist[count][6:9])
        list_4.append(ledlist[count][9:12])
        list_5.append(ledlist[count][12:16])
        count+=1
        continue
    

    print(" ".join(list))                       #Then, the display is made line by line on any numbers of typed numbers
    print(" ".join(list_2))                     #Used join method to remove the elements of the list and print them
    print(" ".join(list_3))
    print(" ".join(list_4))
    print(" ".join(list_5))

ask_number()                                    #The functions get executed
create_led()
display_led()
