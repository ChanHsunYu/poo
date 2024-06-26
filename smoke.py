smoking = input('你有沒有抽菸:') 
age = input('請輸入年齡:')
age = int(age)
if smoking == '沒有':
    if age >= 18:
        print('請繼續保持!')
elif smoking == '有' and age >= 18:
    print('請儘快戒菸!')
elif smoking == '有' and age <= 18:
    print('你犯法囉!')
elif smoking == '沒有' and age <= 18:
    print('你很棒喔!')
else:
    print('只能填有或沒有!')