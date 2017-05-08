import re
def order(sentence):
    """
    Sort a given string. Each word in the String contains a single number. 
    This number is the position the word should have in the result.
    
    Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
    
    If the input String is empty, return an empty String. 
    
    The words in the input String will only contain valid consecutive numbers.
    
    For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
    """
    words = sentence.split()
    if len(words) <= 1:
        return sentence
    else:
        sorted_words = range(len(words))
        for w in words:
            sorted_words[int(re.search(r'\d', w).group()) - 1] = w
        return " ".join(sorted_words)

print(order("is2 Thi1s T4est 3a"))