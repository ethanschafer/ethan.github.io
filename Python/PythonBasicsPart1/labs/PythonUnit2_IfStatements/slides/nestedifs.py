print "Nested ifs example"
grade = 97
if grade >= 70:
    print "Passing"
    if grade >= 90:
        print "A"
    elif grade >= 80:
        print "B"
    elif grade >= 75:
        print "C"
    else:
        print "D"
else:
    print "Failing"
