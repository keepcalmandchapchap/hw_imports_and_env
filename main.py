import sys
import cv2
import uuid
import datetime
from colored import Fore, Style
from application.salary import calculate_salary
from application.db.people import get_employees

img = cv2.imread('tulen.png', cv2.IMREAD_ANYCOLOR)

if __name__ == '__main__':
    print(datetime.datetime.now())
    calculate_salary()
    get_employees()
    print('------')
    print(f'{Fore.rgb('5%', '32%', '29%')}{uuid.uuid4()}{Style.reset}') # генерирует случайное id и вывод с измененным цветом

    while True: #показывает тюленя
        cv2.imshow('Tulen', img)
        cv2.waitKey(0)
        sys.exit()

