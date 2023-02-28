first_int = int(input())  # первый инпут
second_letter = input().strip()  # второй инпут

alphabet = ' abcdefghijklmnopqrstuvwxyz'  # алфавит дан
new_list = []  # новый лист, для записи данных в цикле

for item in second_letter:
    old_index = alphabet.find(item)  # определяем индексы в алфавите
    new_index = (old_index + first_int) % len(alphabet)  # меняем индексы относительно int инпута
    password = alphabet[new_index:new_index + 1]  # срез новых индексов для генерации элементов
    new_list.append(password)  # запись но new_list новых элементов
    fuck_two_hours = ''.join(new_list)  # создаем новую строку и в нее соединяем элементы в строку
print(f' Result: "{fuck_two_hours}"')  # выводим f строку с надписью и результат.

# два часа попрачено на то, что затупил, обидно. Нужно было просто создать новую спроку и в нее записать через
# join элементы листа. А я пытался перезаписать лист, что бы он объеденил значения. Глупая ошибка, которая возникла
# из за желания сделать код более коротким, что привело к проблеме и потере времени.
