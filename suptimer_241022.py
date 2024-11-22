
# import
from shutil import copyfile
import tkinter as tk
from tkinter import ttk
import time
import sys
import threading
import winsound as sd
import tkinter.messagebox as msgbox
import pygame

running = False #

'''

2024-08-16(금)
2024-08-17(토)
2024-08-20(화)
2024-08-20(화)
2024-09-02(월)
2024-09-15(일)
2024-09-15(일)
2024-10-02(수)
2024-10-08(화)
2024-10-14(월)
2024-10-14(월)
2024-10-22(화)
- 기존 메모 저장 방식이 (순번).txt에서 현재시간+[순번].txt로 변경되었습니다.
'''

## 전역변수 선언(변수들을 정상작동 시키기 위한 초기화)
# todo_item ~ todo_item4 : 선택하거나 실행시, 일의 정보와 상태를 안내하기 위한 값(요소)들
# selected_value ~ value2 : 마우스로 선택한 값이 그대로 정보에 출력되도록 돕는 변수

todo_item = ""
todo_item2 = ""
todo_item3 = ""
todo_item4 = ""
selected_value = ""
selected_value2 = ""

part = "" # 모름
i = 1 # 할일 목록에 다음요소를 추가할 수 있게 하기위해 i라는 변수를 덧셈 카운트 하려고 초기화함.
j = 11 # 시간에서 분 단위를 1~9로 나눠버리기 위해 11로 초기화해둠.
timer = time.time() # time 외부 기능을 끌어온 것을 구현시키기 위함. 
memobox1 = "" # 메모 저장의 초기화.
index = 0 # 할일 목록의 순서를 표현하기 위한 초기화.
addlist2 = "" # 할일 목록의 텍스트를 초기화.

# 프로그램의 겉껍질(프레임)
root = tk.Tk()
root.title("suptimer")
root.geometry("550x680")
frame = tk.Frame(root)
frame.pack(pady=10)
z=1

# 버튼이나 기능들에서, 사용할 수 없는 함수가 아무것도 없을 때에 임시로 걸쳐놓는 실험용 함수.
def example1():
    x = 1
    print(x)
    return example1

# 외부 보이는 텍스트(이름, 라벨 등)
# 이름붙이기
label1 = tk.Label(root, text="일정 관리")
label1.place(anchor = tk.NW, x=10)
entrynum1 = tk.Label(root, text="수행 이름 : ")
entrynum1.place(anchor = tk.NW, x=10, y=25)
entrynum2 = tk.Label(root, text="수행 시간 : ")
entrynum2.place(anchor = tk.NW, x=10, y=50)
entrynum3 = tk.Label(root, text="쉬는 시간 : ")
entrynum3.place(anchor = tk.NW, x=10, y=75)
entrynum4 = tk.Label(root, text="추가 내용 : ") 
entrynum4.place(anchor = tk.NW, x=10, y=100)
entrynum5 = tk.Label(root, text="<수행 정보>")
entrynum5.place(anchor = tk.NW, x=10, y=170)

# 작성 가능한 엔트리들(작성가능한 빈칸들)
entrytb1 = tk.Entry(root, bd=1 ,relief = tk.SOLID)
entrytb1.place(anchor = tk.NW, width=140, x=85, y=25)
entrytb1.focus()
entrytb1.insert(0, "작업 이름 입력")

# 콤보박스(시간 선택창, 분, 초, 추가 내용(memobox1) 등 입력칸.)
timeselect1_minute = ttk.Combobox(root, state="normal")
timeselect1_minute.place(anchor = tk.NW, width = 60, x=85, y=50)
timeselect1_minute["values"] = [10, 30]
timeselect1_minute.insert(0, "0")
timeselect1_minutetext = tk.Label(root, text = "분") #글자표시
timeselect1_minutetext.place(anchor = tk.NW, x=145, y=50)
timeselect1_second = ttk.Combobox(root, state="normal")
timeselect1_second.place(anchor = tk.NW, width = 60, x=170, y=50)
timeselect1_second["values"] = [10, 30]
timeselect1_second.insert(0, "0")
timeselect1_secondtext = tk.Label(root, text=" 초") #글자표시
timeselect1_secondtext.place(anchor = tk.NW, x=230, y=50)
timeselect2_minute = ttk.Combobox(root, state="normal")
timeselect2_minute.place(anchor = tk.NW, width = 60, x=85, y=75)
timeselect2_minute["values"] = [10, 30]
timeselect2_minute.insert(0, "0")
timeselect2_minutetext = tk.Label(root, text = "분") #글자표시
timeselect2_minutetext.place(anchor = tk.NW, x=145, y=75)
timeselect2_second = ttk.Combobox(root, state="normal")
timeselect2_second.place(anchor = tk.NW, width = 60, x=170, y=75)
timeselect2_second["values"] = [10, 30]
timeselect2_second.insert(0, "0")
timeselect2_secondtext = tk.Label(root, text=" 초") #글자표시
timeselect2_secondtext.place(anchor = tk.NW, x=230, y=75)
memobox1 = tk.Text(root, bd=1, relief=tk.SOLID)
memobox1.place(anchor = tk.NW, width = 140, height = 70, x = 85, y = 100)
memobox1.insert(1.0, "추가 내용 입력") # '추가 내용'항목 입력 칸.

# 메모박스(memobox2, 메모 입력 칸)
memobox2 = tk.Text(root, bd=1, relief=tk.SOLID)
memobox2.place(anchor = tk.NW, width = 320, height = 110, x=30, y = 490)
memobox2.insert(1.0, "메모 입력") #

# 할일 목록(addlist1)과 스크롤창(scrollbar)을 나타냄.
addlist1 = tk.Listbox(root, bd=1, relief = tk.SOLID)
addlist1.config(selectmode="single")
addlist1.config(height = 0)
addlist1.place(anchor = tk.NW, width=200, height=140, x=30, y=195)
scrollbar = ttk.Scrollbar(addlist1)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 세부정보(텍스트)
infolabel1 = ttk.Label(root, state="readonly", text="")
infolabel1.place(anchor = tk.NW, x = 20, y = 340)

# 남은시간(텍스트)
infolabel3 = ttk.Label(root, state="readonly", text="<남은 시간>")
infolabel3.place(anchor = tk.NW, x= 250, y = 360)

# 수행정보(텍스트, 할 일 실행 시 나타남)
infolabel2 = ttk.Label(root, state="readonly", text="")
infolabel2.place(anchor = tk.NW, x= 250, y = 420)

# 현재시간 표시 변수.
l=1
timelabel1 = ttk.Label(root, state="readonly")
timelabel1.place(anchor = tk.NE, x = 500, y = 20)


# 사용자 임의 함수- 현재시간 표시
def update_time():
    current_time = time.strftime('%m월 %d일(%a) %H:%M:%S')
    timelabel1.config(text=f"{current_time}")
    timelabel1.after(1000, update_time)
update_time()


# 빠른 설정 목록(텍스트)
presetlabel1 = ttk.Label(root, state="readonly", text="<빠른 설정>")
presetlabel1.place(anchor = tk.NW, x = 440, y = 40)




# 알림소리 저장
workend = "music\work1.mp3"
restend = "music\work2.mp3"
pygame.mixer.init(16000, -16, 1, 2048)




# 스레드 선언 재차 확인
running = False

# 함수 선언 및 초기화 재점검
todo_items = []  # 작업 항목을 저장할 리스트
i = 1
memoi=1
t=1

# 메모 저장 변수 선언
memolist=[]
memot=time.strftime('%y%m%d%H%M')
item=""
file_path = "memo.txt"

#메모 입력 함수
def addmemo() :
    global memolist, item, memoi, memot
    memolist = (memobox2.get("1.0", tk.END).strip())
    file_path = f"memo\memo{memot}[{memoi}.txt"
    with open(file_path, "w") as file:
        file.write(memolist)
    msgbox.showinfo("정보", f"{memoi} 번째 메모가 저장되었습니다.")
    memoi += 1

# 작업 준비 함수 
e=0
def addtask():
    global todo_item2_2, todo_item3_2, e, file_path, memobox2, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    running = True
    e += 1
    todo_item = entrytb1.get()
    todo_item2 = timeselect1_minute.get()
    todo_item2_2 = timeselect1_second.get()
    todo_item3 = timeselect2_minute.get()
    todo_item3_2 = timeselect2_second.get()
    todo_item4 = memobox1.get("1.0", tk.END).strip()

    # 입력값을 정수로 변환 (시간 측정 용도의 문자가 아닌 숫자라는 것을 확실하게 못박기 위한 작업.)
    try:
        todo_item2_int = int(todo_item2) * 60 + int(todo_item2_2) 
        todo_item3_int = int(todo_item3) * 60 + int(todo_item3_2)
        print(todo_item2_int)
        print(todo_item3_int)
        sum1 = todo_item2_int + todo_item3_int
        print(sum1)
    except ValueError:
        msgbox.showerror("에러", "수행시간과 쉬는시간은 숫자로만 입력 가능합니다.")
        return
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1

# 할일 목록에 할일을 집어넣는 함수
def listput():
    global infolabel1, addlist1, timeselect1, entrytb1
        
    if infolabel1:
        infolabel1.getvar(todo_item, todo_item2)
        infolabel1.config(todo_item, todo_item2)
        
# 준비된 할 일을 선택 시, 해당 할 일의 정보가 텍스트라벨로 출력되는 함수.
def update_label(selected_index):
    if selected_index < len(todo_items):
        todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4 = todo_items[selected_index]
        infolabel1.config(text=(
            "\n 수행 이름 : " f"{todo_item}" 
            "\n 총 수행 시간 : " f"{sum1//60}분"f"{sum1%60}초"
            "\n 수행 시간 : " f"{todo_item2_int//60}분"f"{todo_item2_int%60}초"
            "\n 쉬는 시간 : " f"{todo_item3_int//60}분"f"{todo_item3_int%60}초"
            "\n <추가 내용> \n      " f"{todo_item4}"
        ))

# 할일 목록을 선택 시, 해당 할 일이 출력되기 위해, 내부 이벤트를 작동하는 함수.
def select(event):
    selected_index = addlist1.curselection()
    if selected_index:
        index = selected_index[0]  # 선택된 항목의 인덱스
        update_label(index)
    return select
    


# 선택한 할일을 삭제하는 버튼의 함수.
def delete1():
    global deletebutton1, e
    e = e - 1

    selected_index = addlist1.curselection()

    if selected_index:
        index = selected_index[0]
        addlist1.delete(index)  # 선택된 항목의 인덱스
        del todo_items[index]
        

        if index < len(todo_items) :
            update_label(index)
        else:
            infolabel1.config(text="선택된 항목이 없습니다.")

    return delete1


addlist1.bind("<<ListboxSelect>>", select)


# 레이블 변경상태를 갱신해 주는 함수.
myThread = threading.Thread


# ('선택 시작' 버튼의)현재 남은 시간을 끝까지 갱신해서 텍스트라벨로 알려주는 함수.
def start_timer():
    global todo_items, todo_item, todo_item4, running, sum1, todo_item2_int, todo_item3_int, addlist1, ll, index, workend, restend
    for j in reversed(range(todo_item2_int+1)):
        infolabel2.config(text=("수행 시간이 " f"{j//60}분"f"{j%60}초 남았습니다."))
        time.sleep(1)
        if not running:
            return
        continue
    infolabel2.config(text=("완료되었습니다."))
    infolabel2.update()
    pygame.mixer.music.load(workend)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    for j in reversed(range(todo_item3_int+1)):
        infolabel2.config(text=("쉬는 시간이 " f"{j//60}분"f"{j%60}초 남았습니다."))
        time.sleep(1)
        if not running:
            return
        continue
    infolabel2.config(text=("완료되었습니다."))
    infolabel2.update()
    pygame.mixer.music.load(restend)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

# ('모두 시작' 버튼의)현재 남은 시간을 끝까지 갱신해서 텍스트라벨로 알려주는 함수.
def start_timer2():
    global todo_items, todo_item, todo_item4, e, i, running, sum1, todo_item2_int, todo_item3_int, addlist1, ll, index, workend, restend
    for j in reversed(range(todo_item2_int+1)):
            infolabel2.config(text=("수행 시간이 " f"{j//60}분"f"{j%60}초 남았습니다."))
            time.sleep(1)
            if not running:
                return
            continue
    infolabel2.config(text=("완료되었습니다."))
    infolabel2.update()
    pygame.mixer.music.load(workend)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    for j in reversed(range(todo_item3_int+1)):
            infolabel2.config(text=("쉬는 시간이 " f"{j//60}분"f"{j%60}초 남았습니다."))
            time.sleep(1)
            if not running:
                return
            continue
    infolabel2.config(text=("완료되었습니다."))
    infolabel2.update()
    e = e - 1
    pygame.mixer.music.load(restend)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    if e!=0:
        start2()
    elif e==0:
        infolabel2.config(text=("완료되었습니다."))
        infolabel2.update()
            
# ('선택 시작' 버튼의) 스레드(쉽게말해 프로세스의 부분)의 작동을 시작하는 함수.(톱니바퀴)
def start1():
    global running, addlist1, i, index, myThread, todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4
    running = True

    # 선택된 인덱스 가져오기
    selected_index = addlist1.curselection()
    if selected_index:
        index = selected_index[0]
    else:
        index = 0

    # 해당 인덱스의 작업 정보를 불러옵니다.
    todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4 = todo_items[index]

    myThread = threading.Thread(target=start_timer, daemon=True)
    myThread.start()

# ('모두 시작' 버튼의) 스레드(쉽게말해 프로세스의 부분)의 작동을 시작하는 함수.(톱니바퀴)
def start2():
    global running, addlist1, i, index, myThread, todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4
    running = True
    selected_index = addlist1.curselection()
    if selected_index:
        index = selected_index[0]
    else:
        index = 0

    # 해당 인덱스의 작업 정보를 불러옵니다.
    todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4 = todo_items[index]

    myThread = threading.Thread(target=start_timer2, daemon=True)  # 타이머를 별도의 스레드에서 실행
    myThread.start()

# 중지 함수(일시 중지는 아니고, 작성 시 타이머를 처음부터 다시 실행 해야함.)
def pause():
    global running
    pygame.mixer.music.stop() # 진행되고 있는 타이머 알림소리 마저도 강제로 중지시킴.
    running = False
    infolabel2.config(text=("중지되었습니다."))
    infolabel2.update()
            

# 프로그램 종료 함수(스레드 진행상태와 관계없이 강제종료시킴)
def shutdown1():
    global running
    running = False
    sys.exit()


#버튼 세트 1 - 준비

# addbutton1 - 준비
addbutton1 = tk.Button(root, bd=1, relief = tk.SOLID, text="준비", command=addtask)
addbutton1.place(anchor = tk.NW, width=50, height=40, x=270, y=120)


#버튼 세트 2 - 선택 시작, 모두 시작, 중지, 제거

# startbutton - 선택 시작
startbutton = tk.Button(root, bd=1, relief = tk.SOLID, text="선택 시작", command=start1)
startbutton.place(anchor = tk.NW, width=110, height=40, x=270, y=200)

# startbutton2 - 모두 시작
startbutton2 = tk.Button(root, bd=1, relief = tk.SOLID, text="모두 시작", command=start2)
startbutton2.place(anchor = tk.NW, width=110, height=40, x=270, y=250)

# pausebutton - 중지
pausebutton = tk.Button(root, bd=1, relief = tk.SOLID, text="중지", command=pause)
pausebutton.place(anchor = tk.NW, width=50, height=40, x=270, y=300)

# deletebutton1 - 제거
deletebutton1 = tk.Button(root, bd=1, relief = tk.SOLID, text="제거", command=delete1)
deletebutton1.place(anchor = tk.NW, width=50, height=40, x=330, y=300)


#버튼 세트 3 - 메모 저장, 종료

# memobutton1 - 메모 저장
memobutton1 = tk.Button(root, bd=1, relief = tk.SOLID, text="메모 저장", command=addmemo)
memobutton1.place(anchor = tk.NW, width=100, height=110, x=400, y=490)

# exitbutton - 종료(애플리케이션 종료)
exitbutton = tk.Button(root, bd=1, relief = tk.SOLID, text="종료", command=shutdown1)
exitbutton.place(anchor = tk.NW, width=50, height=40, x=470, y=620)

# 준비해둔 프리셋을 수행정보 창에 추가하기 위한 변수를 초기화 한 공간.
presetz1=1
presetz2=1
presetz3=1
presetz4=1
presetz5=1
presetz6=1
presetz7=1
presetz8=1
presetz9=1
presetz10=1
presetz11=1
presetz12=1

# 프리셋함수(3분)
def preset1():
    global e, presetz1, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"3분-{presetz1}"
    todo_item2 = 3
    todo_item3 = 0
    todo_item4 = "3분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz1 += 1
    
# 프리셋함수(10분)
def preset2():
    global e, presetz2, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1    
    running = True
    todo_item = f"10분-{presetz2}"
    todo_item2 = 10
    todo_item3 = 0
    todo_item4 = "10분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz2 += 1

# 프리셋함수(15분)
def preset3():
    global e, presetz3, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1    
    running = True
    todo_item = f"15분-{presetz3}"
    todo_item2 = 15
    todo_item3 = 0
    todo_item4 = "15분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz3 += 1

# 프리셋함수(20분)
def preset4():
    global e, presetz4, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1    
    running = True
    todo_item = f"20분-{presetz4}"
    todo_item2 = 20
    todo_item3 = 0
    todo_item4 = "20분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz4 += 1

# 프리셋함수(30분)        
def preset5():
    global e, presetz5, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"30분-{presetz5}"
    todo_item2 = 30
    todo_item3 = 0
    todo_item4 = "30분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz5 += 1

# 프리셋함수(40분)
def preset6():
    global e, presetz6, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"40분-{presetz6}"
    todo_item2 = 40
    todo_item3 = 0
    todo_item4 = "40분간 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz6 += 1

# 프리셋함수(60분)
def preset7():
    global e, presetz7, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"1시간-{presetz7}"
    todo_item2 = 60
    todo_item3 = 0
    todo_item4 ="1시간 동안 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz7 += 1

# 프리셋함수(2시간)        
def preset8():
    global e, presetz8, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"2시간-{presetz8}"
    todo_item2 = 120
    todo_item3 = 0
    todo_item4 ="2시간 동안 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz8 += 1

# 프리셋함수(3시간)       
def preset9():
    global e, presetz9, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"3시간-{presetz9}"
    todo_item2 = 180
    todo_item3 = 0
    todo_item4 ="3시간 동안 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz9 += 1

# 프리셋함수(5시간)       
def preset10():
    global e, presetz10, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"5시간-{presetz10}"
    todo_item2 = 300
    todo_item3 = 0
    todo_item4 ="5시간 동안 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz10 += 1
        
# 프리셋함수(12시간)       
def preset11():
    global e, presetz11, running, i, todo_item, todo_item2, todo_item3, todo_item4, i, running, sum1, todo_item2_int, todo_item3_int, memobox1, ll
    e += 1
    running = True
    todo_item = f"12시간-{presetz11}"
    todo_item2 = 720
    todo_item3 = 0
    todo_item4 ="12시간 동안 지속됩니다."
    todo_item2_int = int(todo_item2) * 60
    todo_item3_int = int(todo_item3) * 60
    print(todo_item2_int)
    print(todo_item3_int)
    sum1 = todo_item2_int + todo_item3_int
    if todo_item and i < 20:
        todo_items.append((todo_item, sum1, todo_item2_int, todo_item3_int, todo_item4))
        addlist1.insert(i, todo_item)
        i += 1
        presetz11 += 1


# 프리셋 버튼 모아둚 (같은 버튼인 presetbtn1에 텍스트와 작동함수만 다르게 집어넣음)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="3분", command=preset1)
presetbtn1.place(anchor = tk.NW, x=430, y=70)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="10분", command=preset2)
presetbtn1.place(anchor = tk.NW, x=430, y=100)  
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="15분", command=preset3)
presetbtn1.place(anchor = tk.NW, x=430, y=130)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="20분", command=preset4)
presetbtn1.place(anchor = tk.NW, x=430, y=160)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="30분", command=preset5)
presetbtn1.place(anchor = tk.NW, x=430, y=190)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="40분", command=preset6)
presetbtn1.place(anchor = tk.NW, x=430, y=220)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="1시간", command=preset7)
presetbtn1.place(anchor = tk.NW, x=430, y=250)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="2시간", command=preset8)
presetbtn1.place(anchor = tk.NW, x=430, y=280)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="3시간", command=preset9)
presetbtn1.place(anchor = tk.NW, x=430, y=310)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="5시간", command=preset10)
presetbtn1.place(anchor = tk.NW, x=430, y=340)
presetbtn1 = tk.Button(root, bd=1, relief = tk.SOLID, text="12시간", command=preset11)
presetbtn1.place(anchor = tk.NW, x=430, y=370)


# 마무리.
root.mainloop() 