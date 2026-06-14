print("Welcome to AI and programming basics quiz")
print("This quiz is to test your fundamentals in AI and programming")
print("All the best!!")
score = 0
r = "That's right"
w = "Wrong answer"

# question one
print("1. What is the full meaning of AI?")
ans = input("")
if ans == "artificial intelligence":
  print(r)
  score += 1
else:
  print(w)

# question two
print("2. What is python mainly used for?")
ans = input("")
if ans == "programming":
  print(r)
  score += 1
else:
  print(w)

# question three
print("3.What is a variable in programming?")
ans = input("")
if ans == "a container used to store data":
  print(r)
  score += 1
else:
  print(w)

# question four
print("4. What is algorithm?")
ans = input("")
if ans == "a step by step procedure to solve a problem":
  print(r)
  score += 1
else:
  print(w)

# question five
print("5. What is debugging?")
ans = input("")
if ans == "finding and fixing errors in a program":
  print(r)
  score += 1
else:
  print(w)

# question six
print("6. What is machine learning?" )
ans = input("")
if ans == "a branch of AI that allows computers to learn from data":
  print(r)
  score += 1
else:
  print(w)

# question seven
print("7. What is the difference between AI and traditional programming?" )
ans = input("")
if ans == "AI learns from data whilst traditional programming follows explicit instruction":
  print(r)
  score += 1
else:
  print(w)

#question eight
print("8. What is data in AI?")
ans = input("")
if ans == "information used to train the AI":
  print(r)
  score += 1
else:
  print(w)

# question nine
print("What is a model in AI?")
ans = input("")
if ans == "A trained system that makes predictions or decisions":
  print(r)
  score += 1
else:
  print(w)

# question ten
print("What is supervised learning in AI?")
ans = input("")
if ans == "Learning with labelled data":
  print(r)
  score += 1
else:
  print(w)

# scoring 
print("At the end of the quiz, you scored " + str(score) + "/10")
print("Your final grade is : ")
if score >= 8:
  print ("A")
  print("Excellent")
elif score >= 5:
  print("B")
  print("Good")
else:
  print("C")
  print("Keep learning")
