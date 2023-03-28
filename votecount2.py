#PA8 counting votes from two candidates

def main():
    x = str(input("Give the name of the first candidate: "))
    y = str(input("Give the name of the second candidate: "))
    total1 = 0
    tolat2 = 0
    
    vote = str(input("Add votes for which candidate?: "))
    if vote == 'John':
        total1 = 0
        x1 = int(input('How many votes to add?(or negative to quit): '))
        while x1 > 0:
            total1 = total1 + x1
            vote = str(input("Add votes for which candidate?: "))
            x1 = int(input('How many votes to add?(or negative to quit): '))
    elif vote == 'Mary':
        total2 = 0
        x2 = int(input('How many votes to add?(or negative to quit): '))
        while x2 > 0:
            total2 = total2 + x2
            vote = str(input("Add votes for which candidate?: "))
            x2 = int(input('How many votes to add?(or negative to quit): '))
    else:
        print("\nInvalid candidate name.")
        exit()
        
    print("Total votes:", 'John', total1)
    print("Total votes:", 'Mary', total2)

    diff = abs(total1 - total2)
    
    if (total1 > total2):
        print("John is the winner by {} votes!".formate(diff))
    elif (total1 < total2):
        print("Mary is the winner by {} votes!".format(diff))
    else:
        print("It is a draw!")

main()
        
    
  
