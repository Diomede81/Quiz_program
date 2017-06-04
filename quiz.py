import sys


f=open('questions.txt', 'r')
lines = f.readlines()
f.close()
print lines

def get_questions():
    questions = []
    answers = []
    try:
        with open ('questions.txt', 'r')  as f:
            lines = f.readlines()
    except:
        print 'Questions file not found'
        sys.exit()
    return [(lines[i], lines[i+1].strip()) for i in range(0, len(lines),2)]

def quiz():
    keep_going = True
    while True:
        while keep_going==True:
            confirm = raw_input('Would you like to insert some questions? Y/N').upper()
            if confirm == 'Y':
                new_question = raw_input('Please insert question:')
                with open('questions.txt','a') as f:
                    f.writelines(new_question+"\n")

                new_answer = raw_input('please insert answer to previous question')
                with open('questions.txt', 'a') as f:
                    f.writelines(new_answer+"\n")
            else:
                keep_going=False
        try:
            info = get_questions()
        except IOError:
            print 'Questions File not Found'
            sys.exit()
        except IndexError:
            print 'Error: All questions in the questions file must have an answer'
        score = 0
        for questions, answers in enumerate(info):
            print info[questions][0]
            correct=0
            counter = 0
            while correct < 3:
                answer = raw_input("Please insert the response to the question")

                if len(answer) == len(info[questions][1]):
                    for letters in answer:

                        if letters in info[questions][1]:
                            counter+=1

                if len(info[questions][1]) - counter <= 2:
                    score +=1
                    break
                else:
                    print('you did not get it right you have %s trial left' %(2-correct))
                    correct +=1

        print "You have gotten %s out of %s" % (score, len(info))

quiz()
