def stringComparison():

    line1 = raw_input("Enter the first line. ")
    type(line1)

    line2 = raw_input("Enter the second line. ")
    type(line2)

    if line1 == line2 :
        print(line1 + ' is the same as ' + line2 + '. They match.')
    else:
        print(line1 + ' is not the same as ' + line2 + '. They do not match.')

if __name__ == "__main__":
    stringComparison()
