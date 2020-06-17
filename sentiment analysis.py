
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    """Returns a string without any punctuations"""
    t = ''
    for ch in s:
        if ch not in punctuation_chars:
            t += ch
    return t


def get_pos(st):
    """Returns the number of positive words in a string"""
    temp = strip_punctuation(st)
    c = 0
    for word in temp.lower().split():
        if word in positive_words:
            c += 1
    return c


def get_neg(st):
    """Returns the number of negative words in a string"""
    temp = strip_punctuation(st)
    c = 0
    for word in temp.lower().split():
        if word in negative_words:
            c += 1
    return c


# lists of words to use
## list of positive words
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


## list of negative words
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# opening file containing twitter data and copying lines to a list pt

with open("project_twitter_data.csv") as ptd:
    pt = ptd.readlines()
    pt.pop(0)
# creating file containing results and appending results to it
rd = open("resulting_data.csv", "w")
rd.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score" + "\n")
for lines in pt:
    templst = lines.strip().split(',')
    tempstr = strip_punctuation(templst[0])
    pos = get_pos(tempstr)
    neg = get_neg(tempstr)
    net = pos - neg
    rd.write("{}, {}, {}, {}, {}".format(templst[1], templst[2], pos, neg, net))
    rd.write("\n")
rd.close()