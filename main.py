# WHAT IS DONE :
#   Syntax and Input / Output

# WHAT NEED TO BE DONE :
#   Algorithm to find if P/Q is possible
#   Append answer to variable "answer"


#inputs
f = open("A-small-practice.in") #File to open for test :


numberOfCases = int(f.readline()) #Number of test cases
maxGenerations = 40 #Max number of generations for Vida

# Loop through each one
for i in range(numberOfCases):
    P, Q = f.readline().split("/") #Get P and Q
    P = int(P) # cast them into int
    Q = int(Q) # cast them into int
    answer = "Case #" + str(i) + ": " #create answer format
    answerFound = False #boolean to see if answer was found
    #print ("P : " + str(P) + "     Q : " + str(Q)) #Test To see if P and Q are read correctly
    
    
    # WHERE I LEFT AT <-------------------------------------- ALEXIS
    #Find an algorithm to see if P/Q is possible :
    
    
    
    #If not possible
    if(answerFound == False) :
        answer += "impossible"
    
    
    
    
    #Print answer to current P Q
    print (answer)