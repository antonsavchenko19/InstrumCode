import tkinter as tk
from tkinter import messagebox
import random

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Логин')
        self.root.geometry('400x200')
        self.root.configure(bg='beige')
        
        self.label = tk.Label(root, text='Введите логин и пароль', font=("Times New Roman", 14), bg='beige')
        self.label.pack(pady=10)
        
        self.username_label = tk.Label(root, text='Логин:')
        self.username_label.pack()
        self.username_entry = tk.Entry(root, width=20)
        self.username_entry.pack()
        
        self.password_label = tk.Label(root, text='Пароль:')
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show='*', width=20)
        self.password_entry.pack()
        
        self.login_button = tk.Button(root, text='Войти', command=self.login)
        self.login_button.pack(pady=10)
        
    def login(self):
        # Check username and password here
        if self.username_entry.get() == 'admin' and self.password_entry.get() == 'admin':
            self.root.destroy()
            self.open_main_app()
        else:
            messagebox.showerror('Ошибка', 'Неправильный логин или пароль')
        
    def open_main_app(self):
        root = tk.Tk()
        app = MonitoringAppTkinter(root)
        root.mainloop()

class MonitoringAppTkinter:
    def __init__(self, master):
        self.master = master
        self.master.title('Мониторинг мобильных сотрудников')
        self.master.geometry('400x300')
        self.master.configure(bg='beige')
        
        self.label = tk.Label(master, text='Выберите действие:', font=("Times New Roman", 14), bg='beige')
        self.label.pack()

        btn_style = {
            'background': 'green',
            'foreground': 'black',
            'borderwidth': 2,
            'font': ('Times New Roman', 14, 'bold'),
            'padx': 5,
            'pady': 15
        }

        self.locations = ['Office', 'Client Meeting', 'Home', 'On the way']
        self.activities = ['Working on a project', 'In a meeting', 'On a break', 'Travelling']

        for i in range(1, 6):
            btn_check_location = tk.Button(master, text=f'Проверить местоположение сотрудника {i}', **btn_style,
                                           command=lambda num=i: self.check_location(num))
            btn_check_location.pack()

        btn_check_activity = tk.Button(master, text='Проверить активность сотрудника', **btn_style,
                                       command=self.check_activity)
        btn_check_activity.pack()

        btn_employees_table = tk.Button(master, text='Показать таблицу сотрудников и их должностями', **btn_style, command=self.show_employees)
        btn_employees_table.pack()

    def check_location(self, employee_id):
        location = random.choice(self.locations)
        messagebox.showinfo('Местоположение сотрудника', f'Местоположение сотрудника {employee_id}: {location}')

    def check_activity(self):
        activity = random.choice(self.activities)
        messagebox.showinfo('Активность сотрудника', f'Активность сотрудника: {activity}')
    
    def show_employees(self):
        employees = {
            'John Doe': 'Developer',
            'Jane Smith': 'Designer',
            'Michael Johnson': 'Manager',
            'Emily Davis': 'Marketing Specialist',
            'Chris Brown': 'Analyst'
        }

        table_window = tk.Tk()
        table_window.title('Таблица сотрудников и их должностями')
        for employee, position in employees.items():
            label = tk.Label(table_window, text=f'{employee} - {position}', font=("Times New Roman", 12))
            label.pack()

        table_window.mainloop()

root = tk.Tk()
login = LoginWindow(root)
root.mainloop()