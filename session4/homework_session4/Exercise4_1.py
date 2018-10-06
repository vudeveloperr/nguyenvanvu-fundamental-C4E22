
quizspy = {
    'intro': 'who is spy',
    'choice': ['A', 'B', 'C', 'D' ],
    'rightchoice':2,
    'namespy':'B'
}
print(quizspy['intro'])
action = 1
for item in quizspy['choice']:
    print(action,"." ,item)
    action += 1


while True:
    action = int(input("your choice :"))
    if action == quizspy["rightchoice"] :   
        print(quizspy['namespy']," is spy ")
        break          
    print(action ,"isnot spy")
    print("let s' continue ")
