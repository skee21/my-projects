import wikipedia 


Search = input("Enter the subject of search: ")
summ =  wikipedia.summary(Search)


print("here are the details::::::::::::::::::::::")

print(summ)


input("Press any key to continue")
