firstName= "Praneel"  # input("whats your name? ")
lastName = "Yarlagadda"

fullName = firstName + " " + lastName
score1 = 34 # int(input("score1: "))
score2 = 56 # int(input("score2: "))

print("My Name is: " + fullName + ", not done yet,....")
print("Result: " + str(score2-score1) + ", end of program....")
finalScore=score2 + score1
print("My Name: %s, my score: %i" % (fullName, finalScore))
print("My Name: {} my score: {}" .format(finalScore, fullName))
print("My Name: {first}, my score: {second}".format(second=fullName, first=finalScore))
print(f"My Name: {fullName}, my score: {finalScore}") # This is the best way so use it like this

# 1. plain format, passing multiple values
# 2. string concatenate : sting join
# 3. using % format
# 4. using format()
# 5. using format() with key-value
# 6. using f-string
# 7. using %s means it's a string %s = string
# 8. using %i means it's an integer %i = integer