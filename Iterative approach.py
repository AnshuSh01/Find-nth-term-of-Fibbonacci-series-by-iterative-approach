def Fibbo(index):
    #For Iterative Approch We have to Declare the New node which store the value of previous node
    
    previous=0
    current=1 
    
    for i in range(1,index): 
         
        preprevious=previous
        previous=current
        
        current=previous+preprevious
         
    return current
         
if __name__ == '__main__':
    EnterInput=int(input("enter the nth term at which u want to know the value of that particular index no.\n"))
    print(f"The value at Index {EnterInput} is ",Fibbo(EnterInput))
