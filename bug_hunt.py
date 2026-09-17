count = 1
total = 0

while count <= 5: # BUG: syntax error there was no full colon at the end and there was logic error 5 was not included
    total = total + count
    count = count + 1

print("Sum of 1 to 5 is: " + str(total)) # BUG: we can only concatenate str to str