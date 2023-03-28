#sentence.py
#this program asks the user to enter a sentence
#and outputs the number of words in the sentence
#and the average word length

def main():
    print("This program gives the number of words in a sentence")
    print("and the average word length. \n")

    myString = input("Please enter your sentence: ")

    num = len(myString.split())

    print("The number of words in the sentence is: " + str(num))

    words = myString.split()
    average = sum(len(word) for word in words) / len(words)
    
    print("The average word length is: ", average)
    
main()
        
