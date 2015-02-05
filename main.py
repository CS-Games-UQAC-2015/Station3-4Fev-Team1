# WHAT IS DONE :
#   Syntax and Input / Output
#   Algorithm to find if P/Q is possible
#    P/Q is possible if u can do: (numérateur/dénumérateur) * 40 = entier. Sinon, impossible


# WHAT NEED TO BE DONE :
#   Append answer to variable "answer"



#inputs
f = open("A-small-practice.in")#File to open for test :


numberOfCases = int(f.readline())#Number of test cases
maxGenerations = 40 #Max number of generations for Vida

# Loop through each one
for i in range(numberOfCases):
    P, Q = f.readline().split("/")#Get P and Q, vérify is there is a /, arrive pas toujours
    P = int(P) # cast them into int
    Q = int(Q) # cast them into int
    answer = "Case #" + str(i) + ": "#create answer format
    answerFound = False#boolean to see if answer was found
    #print ("P : " + str(P) + "     Q : " + str(Q)) #Test To see if P and Q are read correctly
    
    
    # WHERE I LEFT AT <-------------------------------------- ALEXIS
    #Find an algorithm to see if P/Q is possible :
    Z = (P + Q) * 40
    isInt = isinstance(Z, int)  #Johnny: isInt is false if its impossible (not a int), and true if it is

    
    
    #If not possible
    if isInt == False :
        answer += "impossible"
        print (answer)


    ############################################################################
    ## ALEXIS TES RENDU LAAA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    ############################################################################

    #if possible
    else:
        #Algo:if its possible
        # j'ai pas le temps de le programmer mais je suis un génie d'avoir pensé à ca (johnny)
        # 1 Faire myVar = P/Q , nombreGen = 0
        #2 TANT QUE myVar != 1
        #3      myVar *= 2
        #4      nombreGen += 1
        #5      if myVar == 1:
        #6          answe += str(nombreGen)

        #Print answer to current P Q
        print (answer)