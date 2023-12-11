#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = (str.split(), str.split()[5:7], [str.split()[0]])
print(' '.join(str[1] + str[2]))
