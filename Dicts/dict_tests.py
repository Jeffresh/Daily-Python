funcion = {'Computable': ["suma","multipicación","potencia","factorial"], 'No computable':{'nombre':["resta",'division']}}

# CHALLENGE!
#Use a dictionary comprehension to count the length of each word in a sentence.

sentence = "All that is gold does not glitter,Not all those who wander are lost"


#For all the numbers 1-1000, use a nested list/dictionary comprehension to
#find the highest single digit any of the numbers is divisible by.



if __name__ == '__main__':
    result = {word: len(word) for word in sentence.split()}

    print(result)

    result = {number:max([divisor for divisor in range(1, 10) if number % divisor == 0]) for number in range(1, 1001)}

    print(result)
