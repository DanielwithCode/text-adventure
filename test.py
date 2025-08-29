# 1단계: Tkinter 기초 학습 예제들

# 예제 1: 첫 번째 윈도우 생성
import tkinter as tk

root = tk.Tk()
root.title("첫 번째 GUI")
root.geometry("300x200")
root.configure(bg='lightblue')
root.mainloop()

print("=" * 50)

# 예제 2: 기본 위젯들 (Label, Button, Entry)
import tkinter as tk

def button_click():
    name = entry.get()
    label_result.config(text=f"안녕하세요, {name}님!")

root = tk.Tk()
root.title("기본 위젯 실습")
root.geometry("400x250")

# Label
label_title = tk.Label(root, text="이름을 입력해주세요", font=("Arial", 14))
label_title.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="확인", command=button_click, 
                  bg='lightgreen', font=("Arial", 12))
button.pack(pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12), fg='blue')
label_result.pack(pady=10)

root.mainloop()

print("=" * 50)

# 예제 3: 색상 설정 예제
import tkinter as tk

root = tk.Tk()
root.title("색상 설정 예제")
root.geometry("300x200")

# 다양한 색상의 라벨들
colors = [('빨강', 'red'), ('파랑', 'blue'), ('초록', 'green'), 
          ('노랑', 'yellow'), ('보라', 'purple'), ('주황', 'orange')]

for i, (name, color) in enumerate(colors):
    label = tk.Label(root, text=name, bg=color, fg='white', 
                    font=("Arial", 12, "bold"), width=10)
    label.grid(row=i//3, column=i%3, padx=5, pady=5)

root.mainloop()