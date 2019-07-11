import pronouncing

def linesInput():

    line1 = raw_input("Enter the first line. ")
    type(line1)

    line2 = raw_input("Enter the second line. ")
    type(line2)

    return line1, line2;


def simpleEndRhymeComparison(lines):
    L1 = list(lines[0])
    L2 = list(lines[1])

    #Get length of sentences
    lengths = (len(lines[0]),len(lines[1]))

    #assign last two consonants for comparison
    lastTwo1 = (L1[lengths[0]-2], L1[lengths[0]-1])
    lastTwo2 = (L2[lengths[0]-2], L2[lengths[0]-1])

# Print for debugging purposes
    # print(lastTwo1)
    # print(lastTwo2)

    #Compare the last two
    if lastTwo1 == lastTwo2:
        print('This is a perfect rhyme. Yay!')
    else:
        print('This is not a perfect rhyme, please try again. Remember, a perfect rhyme in this program means the last two characters match.')
        stringComparison()


def phoneticEndRhymeComparison(lines):

    output = [pronouncing.rhymes(lines[0]),pronouncing.rhymes(lines[1])]
    outputD = {0: pronouncing.rhymes(lines[0]), 1: pronouncing.rhymes(lines[1])}

    # print(outputD)
    # if outputD[0] != outputD[1]:
    #     print('This has passed the complex rhyme test.')
    # else:
    #     print(outputD[0], " ", outputD[1])

    # set(output[0]).intersection(output[1])
    # set([5])

    test_list1 = output[0]
    test_list2 = output[1]

    test_list1 = [str(r) for r in test_list1]
    test_list2 = [str(r) for r in test_list2]
    
    # printing lists
    print ("The first list is : " + str(test_list1))
    print ("The second list is : " + str(test_list2))

    # sorting both the lists
    test_list1.sort()
    test_list2.sort()

    # using == to check if
    # lists are equal
    if test_list1 == test_list2:
        print ("The lists are identical")
    else :
        print ("The lists are not identical")

if __name__ == "__main__":

    lines = linesInput()
    phoneticEndRhymeComparison(lines)
    # output1 = pronouncing.rhymes(lines[0])
    # output2 = pronouncing.rhymes(lines[0])
    #
    # print(output1)
    # print(output2)



    phoneticEndRhymeComparison(lines)
