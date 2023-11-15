#We are building a chatbot as a number guesser. 
#You need to write a number guesser class to guess a number in a range of your choosing and can give the user three hints. 
#You must implement the required properties for the class to have a random number in the range you want
#and five properties to use as hints(parity, factors, multiples, larger, smaller). 
#There should be private methods in the class to calculate those properties when an object is created.

#Create an object of the class.

#The chatbot greets the user and tells them they have guessed a number, 
#that they have 4 (you are free to change the number) guesses to make, and waits for the user's input.
#If the user guessed right, the chatbot congratulates them and exits.
#If the user guessed wrong, the chatbot subtracts the number of guesses by 1, asks them to guess again, and reminds them they can request up to 3 hints by typing "hint" in the terminal.
#If the user guesses right at any point, the chatbot congratulates them and exits.
#If the user requests a hint, the chatbot will randomly choose between the five hints divided into three categories:
#Factors, multiples
#Larger, Smaller
#Parity
#If the hint is "a", the chatbot will choose either to display factors or multiples, taking into consideration that if one of them isn't applicable, it'll choose the other(If both aren't, what could that mean?).
#The factors is a list of all numbers that the chatbot guessed number is divisible by, and the chatbot will choose one of them randomly.
#The multiples are multiples of the chatbot's guessed number, and the chatbot will choose one of them randomly.
#If the hint is "b", the chatbot will choose either to display a larger number or a smaller number than the chatbot guessed number, taking into consideration that if one of them isn't applicable, it'll choose the other.
#The larger or smaller number must be in the range of the guesses (if the number is between 1 and 10, then smaller or larger must be in that range as well).
#If the hint is "c", the chatbot will write whether the number is even or odd.
#If the user runs out of hints, the chatbot will only take guesses from the user and display an apology if they request a hint.
#If the user runs out of guesses, the chatbot tells them the number and exits.
#The chatbot must always remind the user after every guess or hint of how many guesses and hints are remaining.
#Milestones
#Implement the Gueser class
#Build the class to guess a number and get its properties.
#Implement the chatbot to interact with the user
#Display the information the user is looking for.
import random

class Number_guesser:
    
    
    
    def __init__(self, num_hints = 3 ,num_guesses = 4 ):
        self.comp_result = int(random.randint(1, 10))
        self.num_hints = num_hints
        self.num_guesses = num_guesses
      
        self.input_num = int(input("Hello! guess a number between 1 to 10 , you have 4 guesses to make:"))
        
        if self.comp_result == self.input_num:
            return print("you won")
            
        while (self.input_num != self.comp_result) and self.num_guesses>1:
            print("wrong! here are 3 hints ")
            self.give_hints()
            self.input_num  = int(input("Hello! guess a number again:"))
            self.num_guesses -=1

            if self.comp_result == self.input_num:
                return print("you won")
            if self.num_guesses<=1:
                return print("you lost")
            
        
    def give_hints(self):
        self.hint_list =[self.__get_parity(),self.__get_factors(),self.__get_multiples(),self.__get_larger(),self.__get_smaller()]
        hints = random.sample(self.hint_list, k=3)
        for hint in hints:
            print(hint)
    
    
    
    def __get_comp_result(self):
        return self.comp_result
    
    #parity
    
    def __get_parity(self):
        if self.comp_result%2 == 0:
            return "number is even"
        else:
            return "number is odd"
        
    #factors
    def __get_factors(self):
        factors=[]
        for i in range(1,self.comp_result+4):
            if self.comp_result%i==0:
                factors.append(i)
        return factors
        
    #multiples
    def __get_multiples(self):
        random_num = 0
        multiples = []
        count = 1
        
        while count <=5:
            random_num = random.randint(2, 10)
            multiples.append(random_num*self.comp_result)
            count +=1
            random_num += random_num
        return multiples
        
        
    #larger
    def __get_larger(self):
        if self.comp_result > self.input_num :
            return "Number is larger than selected number"
        else:
            self.__get_smaller()
        
    
    #smaller
    def __get_smaller(self):
        if self.comp_result < self.input_num :
            return "Number is smaller than selected number"
        else:
            self.__get_larger()
        


   


guess1 = Number_guesser()

