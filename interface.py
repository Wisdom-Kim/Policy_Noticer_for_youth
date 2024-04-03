from tkinter import *
from tkinter import simpledialog
import tkinter as tk
from custom_filter import Filter
import time

class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("정책 필터 설정")
        self.category_vars = []
        self.target_vars = []
        self.my_filter=Filter()
        
        
    def close_widgets(self):
        self.root.destroy()
        
    def create_widgets(self):
        # 카테고리 라벨 및 체크박스
        self.root.geometry("500x300")
        tk.Label(self.root, text="").grid(row=1, column=0, padx=10, pady=5)
        
        tk.Label(self.root, text="카테고리").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        for i, category in enumerate(self.my_filter.cate_list()):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.root, text=category, variable=var)
            cb.grid(row=1 + i//5, column=i%5, padx=10, pady=5, sticky="w")
            self.category_vars.append(var)
        
        # 타겟 라벨 및 체크박스
        tk.Label(self.root, text="대상").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        
        for i, target in enumerate(self.my_filter.target_list()):
            var = tk.BooleanVar()
            cb = tk.Checkbutton(self.root, text=target, variable=var)
            cb.grid(row=6+i//5, column=i%5, padx=5, pady=10, sticky="w")
            self.target_vars.append(var)
        
        # # 확인 버튼
        # tk.Label(self.root, text="메일 주소를 입력하시면 관련 정책을 보내드릴게요!").grid(row=8, column=1, padx=10, pady=5, sticky="w")
        # self.email_entry = tk.Entry(self.root, width=40)
        # self.email_entry.grid(row=9, column=1, padx=10, pady=5, sticky="w")  # 이메일 입력 상자는 세 번째 행에 배치
        
        tk.Button(self.root, text="확인", command= lambda : self.apply_filter()).grid(row=10, column=4, padx=10, pady=5, sticky="e")
        self.root.mainloop()
        
    def apply_filter(self) ->object:
        #filter 객체 반환
        
        #선택한 요소의 인덱스를 필터 객체에 저장
        #print("야야야야야ㅑ야ㅑ~!~!~!")
        self.my_filter.cate = [idx for idx, var in enumerate(self.category_vars) if var.get()]
        self.my_filter.target = [idx for idx, var in enumerate(self.target_vars) if var.get()]
        #self.root.destroy()
        # self.cm.crawling_init(self.my_filter)
        #self.root.destroy()
        
        return self.my_filter
        
    def input_email(self) -> str:
        return simpledialog.askstring('이메일',"메일 주소를 입력하면 관련 정책을 보내드려요!")