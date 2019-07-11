import pronouncing
from collections import Counter

def stringComparison():

    text = "april is the cruelest month breeding lilacs out of the dead"
    count = Counter()
    words = text.split()
    for word in words:
       pronunciation_list = pronouncing.phones_for_word(word)
       if len(pronunciation_list) > 0:
         count.update(pronunciation_list[0].split(" "))

    output = count.most_common(5)
    print(output)

    line1 = raw_input("Enter the first line. ")
    type(line1)

    line2 = raw_input("Enter the second line. ")
    type(line2)

    if line1 == line2 :
        print(line1 + ' is the same as ' + line2 + '. They match.')
    else:
        print(line1 + ' is not the same as ' + line2 + '. They do not match.')

    return line1, line2;


def simpleEndRhymeComparison(lines):
    L1 = list(lines[0])
    L2 = list(lines[1])

    #Get length of sentences
    lengths = (len(lines[0]),len(lines[1]))

    #print last two consonants for comparison
    lastTwo1 = (L1[lengths[0]-2], L1[lengths[0]-1])
    lastTwo2 = (L2[lengths[0]-2], L2[lengths[0]-1])

    #Compare the last two
    if lastTwo1 == lastTwo2:
        print('This is a perfect rhyme. Yay!')
    else:
        print('This is not a perfect rhyme, please try again. Remember, a perfect rhyme in this program means the last two characters match.')
        stringComparison()

if __name__ == "__main__":
    pronouncing.rhymes("climbing")
    lines = stringComparison()
    print(lines)

    simpleEndRhymeComparison(lines)