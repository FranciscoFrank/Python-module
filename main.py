# The file is for demonstrating the capabilities of a custom Python module.
from math_function_custom import binomial_expansion
from math_function_custom import geometric_progression
from math_function_custom import аrefmatic_progression
from math_function_custom import euler_numbers

def main():
    options = {
        "1": binomial_expansion,
        "2": geometric_progression,
        "3": аrefmatic_progression,
        "4": euler_numbers
    }
    
    while True:
            print("\nВиберіть функцію:")
            print("1. Розклад Бінома Ньютона")
            print("2. Геометрична прогресія")
            print("3. Арифметична прогресія")
            print("4. Пошук числа Ейлера")
            print("0. Вихід")

            choice = input("Ваш вибір: ")

            if choice == "0":
                print("Вихід з програми.")
                break
            elif choice in options:
                options[choice]() 
            else:
                print("Неправильний вибір. Спробуйте ще раз.")
                
if __name__ == "__main__":
    main()