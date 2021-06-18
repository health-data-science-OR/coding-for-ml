#######################################################################
# Example:  Illustrates how to use, format and manipulate strings
# Author:   T.Monks
######################################################################


#print a string to console
print("foo")

#access a specific letter
print("Spam"[0])     #access the first character in string
print("Spam"[2])     #access the third character in string


mystr = "Spam"
print(mystr[-1])    #alternative count from end to access the last character 
print(mystr[-4])    #alternative count from end to access the first character 

#string slicing (substrings)

print(mystr[:2]) #this will print the first two chars. Same as writing mystr[0:2]

print(mystr[1:4]) #print chars 1 to 4 i.e. pam

print(mystr[-2:]) #last two chars i.e. am
print(mystr[-3:]) #last three chars i.e. pam

print(mystr[1:]) #print string starting from char pos 1 i.e pam
print(mystr[2:]) #print string starting from char pos 2 i.e. am

mystr = "123456789"
print(mystr[1:8:2]) #starting from index 1 return every other char up to index 8  = "2468"
print(mystr[0:8:2]) #1357

#concatenation
myvar1 = "foo"
myvar2 = "bar"

print(myvar1 + myvar2)

#string case
print(myvar1.lower())
print("LoWeRCAse".lower())
print(myvar1.upper())

#string length
print(len(myvar1))

#convert numeric values to strings
my_num= 2
print("my daughter is " + str(my_num))

#advanced formatting of output
language = "python"
skill = "productivity"

print("%s increases your programming %s" %(language, skill))

#modern alternative output formatting using string.format
print("{} increases your programming {}".format(language, skill))

#use an optional index to easily rearrange the order of output.
print("{0} increases your programming {1}".format(language, skill))
print("{1} increases your programming {0}".format(language, skill))

#reuse the same variable multiple times
print("{0} increases {0} your {0} programming {1}".format(language, skill))

#formatting output to n decimal places
print("{:.2f}".format(0.123456789))
print("{:.3f}".format(0.123456789))

#if you need {} in your output - double up.
print("{{}}".format("double"))

#splitting strings

sentence = "we are the knights who say ni!"
print(sentence.split())     #default is to split by space.

sentence = "we|are|the|knights|who|say|ni!"
print(sentence.split("|"))
print(sentence.split("|", 1))       #the 2nd parameter limits the number of splits
print(sentence.split("|", 2))

#the reverse of split is the join command 
split_data = ["we", "are", "the", "knights", "that", "say", "ni!"]
sentence = " ".join(split_data)     #join words with " " as between each word.
print(sentence)

sentence = "-".join(split_data)     #join words with ", " as between each word.
print(sentence)


#Strings are iterable
mystr = "123456789"
for c in mystr:
    print(c)