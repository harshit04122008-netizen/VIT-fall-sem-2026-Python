L = input().split()
#input for the list of numbers

i = 0
#intializing the index variable to 0

L_2 =  []
#creating an empty list to store the peaks

while i<(len(L)-1):     
    #loop through the list
    
    if i<(len(L)-2):    
        #sepearting because the last two elements of the list will not  have  a next element to compare with

        a = int(L[i])
        #first number to compare with the next two numbers

        b = int(L[i+1])
        #second number to compare with the first and third numbers

        c = int(L[i+2])
        #third number to compare with the first and second numbers

        if b>a and b>c:    
             #to check if the second number is greater than the first and third numbers

            L_2.append(b)
            #adding the second number to the list of peaks if it is greater than the first and third numbers

    elif i<len(L): 
        #for the last two elements of the list, we will only compare with the next element

        a = int(L[i])
        #first number to compare with the next number

        b = int(L[i+1])
        #second number to compare with the first number

        if b>a:
            #to check if the second number is greater than the first number

            L_2.append(b)
            #adding the second number to the list of peaks if it is greater than the first number
    i = i + 1
        #incrementing the index variable to move to the next element in the list

print("Peaks:",L_2)
#printing the list of peaks