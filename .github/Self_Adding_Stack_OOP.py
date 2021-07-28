class Stack:
    def __init__(self):
        self.__stack_list =[]
    
    def push(self, val):
        self.__stack_list.append(val)
    
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

class Adding_Stack(Stack):
    def __init__(self):
        Stack.__init__(self) #This is made to activate the class within the subclass to get access to the Superclass private data.
        self.__sum = 0
    
    def get_sum(self):
        return self.__sum
        
    def push(self, val):
        self.__sum += val #it gets the information from inputted in object (below).
        Stack.push(self,val) #push from Stack gets executed as well.
    
    def pop(self):
        val = Stack.pop(self) #It gets feeded from the information within the list self.__stack.
        self.__sum-= val #In the Superclass, pop returns val, which is the one we use.
        return val
        
        

stack_object = Stack() #This is made to compare the usage of just the class

#stack_object.push(3)
#stack_object.push(5)
#stack_object.push(1)

#print(stack_object.pop())
#print(stack_object.pop())
#print(stack_object.pop())

stack_object_2 = Adding_Stack() #variable assigned for the Subclass

#stack_object_2.push(3)
#stack_object_2.push(5)
#stack_object_2.push(1)


#print(stack_object_2.get_sum()) #we obtain the sum of the stack

#print(stack_object_2.pop())
#print(stack_object_2.pop())
#print(stack_object_2.pop())

for i in range(5):
    stack_object_2.push(i)
    
print(stack_object_2.get_sum()) #This is left outside of the iteration
    
for i in range(5):
    print(stack_object_2.pop())





