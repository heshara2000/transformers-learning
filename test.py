###find simillr word

# def common_letters():
#     str1 = input("Enter first string: ")
#     str2 = input("Enter second string: ")

#     s1 = set(str1)
#     s2 = set(str2)
#     common = s1 & s2
#     print(common)
# common_letters()



###count the frequency of the words

def count_word_frequency():
    str = input("enter the the string: ")
    words = str.split()
    frequency = {}
    for i in words:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print(frequency)
count_word_frequency()