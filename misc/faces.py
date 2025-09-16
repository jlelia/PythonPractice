"""
One of my trainees wanted help with a CS50 online Python class.
I walked him through the problem by writing the following code.
"""

def convert(sentence: str):
    if ':)' in sentence or ':(' in sentence:
        sentence = sentence.replace(':)', '🙂')
        sentence = sentence.replace(':(', '☹️')
        return sentence
    else:
        return sentence


def main():
    sentence = input("Please put your text that contains an emoticon: ")
    print(convert(sentence))

main()