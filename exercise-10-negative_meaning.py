"""
To improve your defining function skills and string operations ability.

        Define a function to take a word and return negative meaning.
Given a word, return a new word where "not " has been added to the front. However, if the word already begins with "not", return the string unchanged.

        For example:

        Test                                    Result
        print(not_string('sugar'))              not sugar

        print(not_string('x'))                  not x

        print(not_string('not bad'))            not bad
"""
# Solution
def not_string(word):
    word = str(word)
    if word.startswith("not") == True:
        print(word)
    else:
        print('not', word)  
