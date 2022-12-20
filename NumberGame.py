from tkinter import *
import random

ramdom_num = random.randint(1,100)
game_count=1
#successText=""

def enter():
    global ramdom_num
    global game_count
    my_num = int(e1.get()) #e1에서 입력한 값을 받아옴
    if my_num<ramdom_num:
        l1['text']="업"
        game_count = game_count +1
    elif my_num > ramdom_num:
        l1['text']="다운"
        game_count = game_count +1
    elif my_num == ramdom_num:
        l1['text']= "축하합니다! "+str(game_count)+" 번 만에 맞추셨습니다" # str형식인 text에 맞추기위해 game_count를 문자열로 형변환
        print(game_count)
        #l1.config(text=successText)

def restart():
    global ramdom_num
    l1['text']="게임을 시작합니다"
    ramdom_num = random.randint(1,100) # 게임 재시작 후 다시 랜덤숫자 생성

window = Tk()
window.title("오픈소스 과제_김지훈,장효선")

#Message(window,text=" 업,다운 숫자맞추기 게임").grid(row=2,column=1)
#message.pack()

l1 = Label(window, text = "< 업, 다운 숫자맞추기 게임 >",background="yellow",padx=10)
l1.grid(row=1,column=4,pady=10)


label=Label(window,text="1-100사이 숫자를 입력하세요 : ").grid(row=2,column=3,padx=10,pady=5)
e1 = Entry(window)
e1.grid(row=2,column=4,padx=10)


b1 = Button(window, text= "입력", fg="red",command=enter).grid(row=3,column=4)
b2 = Button(window, text= "재시작",fg="purple",command=restart).grid(row=4,column=4,pady=5)



window.mainloop()

'''
(교재에 나와있는 코드)
while True :
    try:
        my_num=int(input("1-100사이의 숫자를 입력하세요: "))
        if my_num > ramdom_num:
            print("다운")
        elif my_num < ramdom_num:
            print("업")
        elif my_num == ramdom_num:
            print(f"축하합니다. {game_count} 번 만에 맞추셨습니다")
            break

        game_count = game_count+1

    except:
        print("에러입니다! 숫자를 입력하세요")
'''

