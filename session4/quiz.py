quiz = {
    'stimulus':"hom nay lop C4E22 hoc co rat nhieu con trai .",
    'stem':'lop ai dep trai nhat ?',
    'choice':['quan', 'an', 'ca hai', 'khong ai'],
    'right_choice':2

}
print(quiz['stimulus'])
print(quiz['stem'])
print(quiz['choice'])


action = input("choice now : ")

if action == quiz['choice'][1]:
    print("right")
else:
    print("wrong")    


