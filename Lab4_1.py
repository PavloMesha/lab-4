# Меша Павло
Str = "Python — це потужна мова програмування, яка проста у вивченні. Він має \
ефективні структури даних високого рівня та простий, але ефективний підхід \
до об’єктно-орієнтованого програмування. Елегантний синтаксис і динамічна \
типізація Python разом з його інтерпретованим характером роблять його \
ідеальною мовою для створення сценаріїв і швидкої розробки додатків у \
багатьох сферах на більшості платформ. Інтерпретатор Python легко \
розширюється за допомогою нових функцій і типів даних, реалізованих у C \
або C++ (або інших мовах, які можна викликати з C). Python також підходить \
як мова розширення для настроюваних програм. Інтерпретатор Python і обширна \
стандартна бібліотека доступні у вихідному або двійковому вигляді для всіх \
основних платформ і можуть вільно поширюватися."

#TEST_HOW_GITHUB_WORKS

# Визначимо довжину рядка
L = len(Str)
# Підрахуємо кількість літери P у рядку
L1 = Str.count('P')
# Розіб'ємо рядок на пробілом
L2 = Str.split(' ')

print(Str)
print('\n')

print("Довжина рядка :",L)
print("Кількість літери P у рядку :",L1)
print('\n')

print(L2)



