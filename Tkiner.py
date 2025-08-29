# 2단계: 색깔 맞추기 게임 기본 버전

import tkinter as tk
import random

class ColorGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("색깔 맞추기 게임")
        self.root.geometry("500x400")
        self.root.configure(bg='white')
        
        # 게임 변수들
        self.colors = ['빨강', '파랑', '초록', '노랑', '보라', '주황']
        self.color_codes = {
            '빨강': 'red', '파랑': 'blue', '초록': 'green', 
            '노랑': 'yellow', '보라': 'purple', '주황': 'orange'
        }
        self.score = 0
        self.current_word = ""
        self.current_color = ""
        
        self.setup_ui()
        self.new_word()
    
    def setup_ui(self):
        # 제목
        title_label = tk.Label(self.root, text="색깔 맞추기 게임", 
                              font=("Arial", 20, "bold"), bg='white')
        title_label.pack(pady=10)
        
        # 설명
        instruction = tk.Label(self.root, 
                              text="단어의 색깔을 입력하세요 (단어 내용 말고 글자 색깔!)", 
                              font=("Arial", 12), bg='white')
        instruction.pack(pady=5)
        
        # 점수 표시
        self.score_label = tk.Label(self.root, text=f"점수: {self.score}", 
                                   font=("Arial", 14, "bold"), bg='white')
        self.score_label.pack(pady=10)
        
        # 색깔 단어 표시 (여기가 핵심!)
        self.word_label = tk.Label(self.root, text="", 
                                  font=("Arial", 30, "bold"), bg='white')
        self.word_label.pack(pady=20)
        
        # 답안 입력
        input_frame = tk.Frame(self.root, bg='white')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="답:", font=("Arial", 12), bg='white').pack(side=tk.LEFT)
        
        self.answer_entry = tk.Entry(input_frame, font=("Arial", 14), width=15)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # 확인 버튼
        check_button = tk.Button(self.root, text="확인", command=self.check_answer,
                               font=("Arial", 12), bg='lightblue')
        check_button.pack(pady=10)
        
        # 결과 메시지
        self.result_label = tk.Label(self.root, text="", 
                                    font=("Arial", 12, "bold"), bg='white')
        self.result_label.pack(pady=10)
        
        # 다음 문제 버튼
        next_button = tk.Button(self.root, text="다음 문제", command=self.new_word,
                               font=("Arial", 12), bg='lightgreen')
        next_button.pack(pady=5)
    
    def new_word(self):
        # 랜덤으로 단어와 색깔 선택
        self.current_word = random.choice(self.colors)
        self.current_color = random.choice(self.colors)
        
        # 단어와 색깔이 같으면 다시 선택 (너무 쉬우니까)
        while self.current_word == self.current_color:
            self.current_color = random.choice(self.colors)
        
        # 화면에 표시 (단어는 current_word, 색깔은 current_color)
        self.word_label.config(text=self.current_word, 
                              fg=self.color_codes[self.current_color])
        
        # 입력창 초기화
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
        self.result_label.config(text="")
    
    def check_answer(self):
        user_answer = self.answer_entry.get().strip()
        
        if user_answer == self.current_color:
            # 정답!
            self.score += 10
            self.score_label.config(text=f"점수: {self.score}")
            self.result_label.config(text="정답! 🎉", fg='green')
        else:
            # 오답
            self.result_label.config(
                text=f"틀렸습니다. 정답은 '{self.current_color}' 였습니다.", 
                fg='red'
            )
    
    def run(self):
        self.root.mainloop()

# 게임 실행
if __name__ == "__main__":
    game = ColorGame()
    game.run()