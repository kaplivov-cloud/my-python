import time

print("Добро пожаловать в обратный таймер! ")
limit = 50

while True: 
    try:
        seconds = int(input("Введите количество секунд: "))
        
        if seconds < 0:
            print("Ошибка: количество секунд не может быть отрицательным!")
        elif seconds > limit:
            print(f"Ошибка: превышен лимит в {limit} секунд!")
        else:
          
            break 
            
    except ValueError:
        
        print("Ошибка! Нужно ввести целое число (например, 5). Попробуйте снова.")

print("Таймер запущен...")
for i in range(seconds, 0, -1):
    print(i)
    time.sleep(1)

print("🚀 ПУСК!")