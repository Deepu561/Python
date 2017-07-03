string = input("Enter a long String :\n")

result = string.split()
result_1 = result[::-1]
result_1 = " ".join(result_1)
print(result_1)

#Reverse Word Order with function

def reverse_word(string):
    return " ".join(string.split()[::-1])

string = input("Enter a long String\n")
print("Reversed String is\n",reverse_word(string))
