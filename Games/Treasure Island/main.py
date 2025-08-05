import swalah as sw

print(sw.msg1)

ans1 = sw.question(sw.msg2, sw.answer_lst2)
if ans1.title() == "Right":
    print(sw.msg5)

else:
    ans2 = sw.question(sw.msg3, sw.answer_lst3)
    if ans2.title() == "Swim":
        print(sw.msg5)
    
    else:
        ans3 = sw.question(sw.msg4, sw.answer_lst4)
        if ans3.title() == "Red" or ans3.title() == "Blue":
            print(sw.msg5)
        
        else:
            print(sw.msg6)
