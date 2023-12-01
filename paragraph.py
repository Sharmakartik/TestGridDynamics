


# This Programme will help to convert the input string into a fixed size of paragraph


def logic(words, maxWidth):

    try:
        result, line, width = [], [], 0

        for w in words:
            if width + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
                result, line, width = result + [''.join(line)], [], 0
            line += [w]
            width += len(w)

        # Handling the last line
        last_line = "".join(line)
        extra_space = maxWidth - len(last_line)
        space = extra_space // max(1, len(line) - 1)
        reminder = extra_space % max(1, len(line) - 1)

        for j in range(max(1, len(line) - 1)):
            line[j] += " "*space
            if reminder:
                line[j] += " "
                reminder -= 1

        # Overall Result
        result.append("".join(line))

    except Exception as e:
        print("Need to handle error : "+ str(e))

    return result

# Input String
input = """This is a sample text but a complicated problem to be solved, 
so we are adding more text to see that it actually works."""

# Page width
width = 60

# Function calling
logic(input.split(), width)


# # Testing the Logic by running this command `python .\paragraph.py`
# output = logic(input.split(), width)
# for item in range(len(output)):
#    print(output[item] + ": size :: " + str(len(output[item])))


#########################################################

## A Sample Output

# Input : """This is a sample text but a complicated problem to be solved, 
# so we are adding more text to see that it actually works."""

# Output : ['This   is  a  sample', 'text      but      a', 'complicated  problem', 'to  be solved, so we', 'are adding more text', 'to   
# see   that   it', 'actually      works.']

#########################################################
