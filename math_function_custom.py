# File with functions that have a mathematical component.
import math

# Function for calculating the coefficients of the Newton binomial expansion.
def binomial_expansion():
    a = str(input("Привіт. \nВведіть першу змінну в вашому виразі: "))
    b = str(input("\nВведіть другу змінну в вашому виразі: "))
    n = int(input("\nВведіть степінь бінома в вашому виразі: "))
    
    # Conversion of degrees to superscript
    superscript = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    
    terms = []
    
    for k in range(n + 1):
        coefficient = comb(n, k)
        if n - k > 1:
            term_a = f'{a}{str(n-k).translate(superscript)}'
        elif n - k == 1:
            term_a = f'{a}'
        else:
            term_a = ''

        if k > 1:
            term_b = f'{b}{str(k).translate(superscript)}'
        elif k == 1:
            term_b = f'{b}'
        else:
            term_b = ''

        if coefficient != 1:
            term = f'{coefficient}{term_a}{term_b}'
        else:
            term = f'{term_a}{term_b}'
        
        terms.append(term)
    
    print(' + '.join(terms))

# Function for finding the n-th element in geometric progression.
def geometric_progression():
    a1 = int(input("Привіт. Введіть перший елемент в геометричні прогресії: "))
    q = float(input("\nВведіть знаменник прогресії : "))
    n = int(input("\nВведіть номер елемента в прогресії : "))
        
    an = a1 * (q ** (n-1))
        
    print(f"n-елемент геометричної прогресії становить: {an}")
    
# Function for finding the n-th element in an arithmetic progression.
def аrefmatic_progression():
    a = int(input("Привіт. Введіть перший елемент арифметичної прогресії: "))
    d = float(input("\nВведіть різницю між елементами прогресії: "))
    n = int(input("\nВведіть номер елемента в прогресії: "))
    
    progression = []
    for i in range(n):
        an = a + i * d
        progression.append(an)
    
    print(f"n-елемент арифметичної прогресії: {an}")

# Function for finding the Euler number up to the nth number of a sequence.
def euler_numbers():
    n = int(input("Введіть номер числа Ейлера: "))
    
    euler_numbers = [0] * (n + 1)
    
    euler_numbers[0] = 1  # E_0 = 1
    if n > 0:
        euler_numbers[1] = 0  # E_1 = 0
    if n > 1:
        euler_numbers[2] = -1  # E_2 = -1

    for i in range(2, n + 1, 2):
        euler_numbers[i] = 0
        for j in range(i):
            if (i - j) % 2 == 0:
                euler_numbers[i] -= euler_numbers[j] * (1 / (i + 1))

    print(f"Обраховане число Ейлера: {euler_numbers[n]}") 


