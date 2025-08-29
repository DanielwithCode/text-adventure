# 3단계: 고급 기능이 추가된 색깔 맞추기 게임

import tkinter as tk
import random
import threading
import time

class AdvancedColorGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("고급 색깔 맞추기 게임")
        self.root.geometry("600x500")
        self.root.configure(bg='white')
        
        # 게임 변수들
        self.easy_colors = ['빨강', '파랑', '초록', '노랑', '보라', '주황']
        self.medium_colors = self.easy_colors + ['분홍', '갈색']
        self.hard_colors = self.medium_colors + ['회색', '검정']
        
        self.color_codes = {
            '빨강': 'red', '파랑': 'blue', '초록': 'green', 
            '노랑': 'yellow', '보라': 'purple', '주황': 'orange',
            '분홍': 'pink', '갈색': 'brown', '회색': 'gray', '검정': 'black'
        }
        
        self.score = 0
        self.high_score = 0
        self.current_word = ""
        self.current_color = ""
        self.time_left = 30
        self.game_running = False
        self.difficulty = "쉬움"
        
        self.setup_ui()
        
    def setup_ui(self):
        # 제목
        title_label = tk.Label(self.root, text="고급 색깔 맞추기 게임", 
                              font=("Arial", 20, "bold"), bg='white')
        title_label.pack(pady=10)
        
        # 점수 및 시간 표시
        info_frame = tk.Frame(self.root, bg='white')
        info_frame.pack(pady=10)
        
        self.score_label = tk.Label(info_frame, text=f"점수: {self.score}", 
                                   font=("Arial", 14, "bold"), bg='white')
        self.score_label.pack(side=tk.LEFT, padx=20)
        
        self.high_score_label = tk.Label(info_frame, text=f"최고점수: {self.high_score}", 
                                        font=("Arial", 14, "bold"), bg='white')
        self.high_score_label.pack(side=tk.LEFT, padx=20)
        
        self.timer_label = tk.Label(info_frame, text=f"남은 시간: {self.time_left}초", 
                                   font=("Arial", 14, "bold"), bg='white', fg='red')
        self.timer_label.pack(side=tk.LEFT, padx=20)
        
        # 난이도 선택
        difficulty_frame = tk.Frame(self.root, bg='white')
        difficulty_frame.pack(pady=10)
        
        tk.Label(difficulty_frame, text="난이도:", font=("Arial", 12), bg='white').pack(side=tk.LEFT)
        
        self.difficulty_var = tk.StringVar(value="쉬움")
        difficulties = [("쉬움 (6색)", "쉬움"), ("보통 (8색)", "보통"), ("어려움 (10색)", "어려움")]
        
        for text, value in difficulties:
            rb = tk.Radiobutton(difficulty_frame, text=text, variable=self.difficulty_var,
                               value=value, font=("Arial", 10), bg='white')
            rb.pack(side=tk.LEFT, padx=5)
        
        # 게임 시작/재시작 버튼
        self.start_button = tk.Button(self.root, text="게임 시작", command=self.start_game,
                                     font=("Arial", 14), bg='lightgreen')
        self.start_button.pack(pady=10)
        
        # 색깔 단어 표시
        self.word_label = tk.Label(self.root, text="게임 시작을 눌러주세요", 
                                  font=("Arial", 30, "bold"), bg='white')
        self.word_label.pack(pady=30)
        
        # 답안 입력
        input_frame = tk.Frame(self.root, bg='white')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="답:", font=("Arial", 14), bg='white').pack(side=tk.LEFT)
        
        self.answer_entry = tk.Entry(input_frame, font=("Arial", 16), width=15)
        self.answer_entry.pack(side=tk.LEFT, padx=5)
        self.answer_entry.bind('<Return>', lambda e: self.check_answer())
        
        # 확인 버튼
        self.check_button = tk.Button(self.root, text="확인", command=self.check_answer,
                                     font=("Arial", 12), bg='lightblue', state='disabled')
        self.check_button.pack(pady=10)
        
        # 결과 메시지
        self.result_label = tk.Label(self.root, text="", 
                                    font=("Arial", 14, "bold"), bg='white')
        self.result_label.pack(pady=10)
        
    def get_current_colors(self):
        difficulty = self.difficulty_var.get()
        if difficulty == "쉬움":
            return self.easy_colors
        elif difficulty == "보통":
            return self.medium_colors
        else:
            return self.hard_colors
    
    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.game_running = True
        
        self.score_label.config(text=f"점수: {self.score}")
        self.start_button.config(text="게임 진행 중...", state='disabled')
        self.check_button.config(state='normal')
        
        self.new_word()
        self.start_timer()
    
    def start_timer(self):
        self.update_timer()
    
    def update_timer(self):
        if self.game_running and self.time_left > 0:
            self.timer_label.config(text=f"남은 시간: {self.time_left}초")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.game_running:
            self.game_over()
    
    def new_word(self):
        if not self.game_running:
            return
            
        colors = self.get_current_colors()
        self.current_word = random.choice(colors)
        self.current_color = random.choice(colors)
        
        # 단어와 색깔이 같으면 다시 선택
        while self.current_word == self.current_color:
            self.current_color = random.choice(colors)
        
        self.word_label.config(text=self.current_word, 
                              fg=self.color_codes[self.current_color])
        
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.focus()
        self.result_label.config(text="")
    
    def check_answer(self):
        if not self.game_running:
            return
            
        user_answer = self.answer_entry.get().strip()
        
        if user_answer == self.current_color:
            # 정답!
            bonus = 1 if self.difficulty_var.get() == "쉬움" else 2 if self.difficulty_var.get() == "보통" else 3
            self.score += 10 * bonus
            self.score_label.config(text=f"점수: {self.score}")
            self.result_label.config(text="정답! 🎉", fg='green')
            
            # 화면 깜빡임 효과
            self.flash_screen('lightgreen')
            
            # 자동으로 다음 문제로
            self.root.after(800, self.new_word)
            
        else:
            # 오답
            self.result_label.config(
                text=f"틀렸습니다. 정답: '{self.current_color}'", 
                fg='red'
            )
            self.flash_screen('lightcoral')
            self.root.after(1500, self.new_word)
    
    def flash_screen(self, color):
        original_bg = self.root.cget('bg')
        self.root.configure(bg=color)
        self.root.after(200, lambda: self.root.configure(bg=original_bg))
    
    def game_over(self):
        self.game_running = False
        
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"최고점수: {self.high_score}")
            self.word_label.config(text=f"게임 종료!\n최고 기록 갱신!\n점수: {self.score}", fg='gold')
        else:
            self.word_label.config(text=f"게임 종료!\n최종 점수: {self.score}", fg='red')
        
        self.start_button.config(text="다시 시작", state='normal')
        self.check_button.config(state='disabled')
        self.result_label.config(text="")
    
    def run(self):
        self.root.mainloop()

# 게임 실행
if __name__ == "__main__":
    game = AdvancedColorGame()
    game.run()