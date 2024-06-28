#получить от пользователя оценку

rate_as_str = input("Оцените работу от 1 до 5:") #str
rate = int(rate_as_str) #int

#проверить, что оценка от 1 до 5

if (rate < 1):
    rate = 1

if (rate > 5):
    rate = 5

#в зависимости от оценки предложить дать обратную связь

feedback = ''

if (rate == 1):
    feedback = input("Расскажите, что нам улучшить: ")
elif rate == 2:
        feedback = input("Что вас смутило: ")
elif rate == 3:
        feedback = input("Как нам стать лучше: ")
elif rate == 4:
        feedback = input("Почему не 5: ")
else: 
    feedback = input("За что похвалить оператора: ")

print(feedback)