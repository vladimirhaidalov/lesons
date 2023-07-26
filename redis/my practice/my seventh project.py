
def create_note(notes):
    title = input('Введите заголовок заметки: ')
    content = input('Введите текст заметки: ')
    notes[title]=content
    print('Заметка успешно завершина/n')

def view_note(notes):
    title = input('Введите заголовок заметки, которую хотите просмотреть: ')
    if title in notes:
        print('/nЗаголовок: ',title)
        print('Текст: ', notes[title])
        print()
    else:
        print('Заметка с таким заголовком не найдена./n')

def edit_note(notes):
    title = input('Введите заголовок заметки, которую хотите отредактировать: ')
    if title in notes:
        print('Текущий текст заметки:/n', notes[title])
        content = input('Введите новый текст заметки: ')
        notes[title] = content
        print('Заметка успешно отредактирована!/n')
    else:
        print('Заметка с таким заголовком не найдена./n')

def delete_notes(notes):
    title = input('Введите заголовок заметки, которую хотите удалить: ')
    if title in notes:
        del notes[title]
        print('Заметка успешно удалена!/n')
    else:
        print('Заметка с таким заголовком не найдена./n')

def main():
    notes = {}
    while True:
        print('===Заметки===')
        print('1. Создать заметку')
        print('2. Промотреть заметку')
        print('3. Редактировать земетку')
        print('4. Удалить заметку')
        print('5. Выйти')

        chois = input('Выберите опцию (1/2/3/4/5): ')
        if chois == '1':
            create_note(notes)
        elif chois == '2':
            view_note(notes)
        elif chois == '3':
            edit_note(notes)
        elif chois == '4':
            delete_notes(notes)
        elif chois == '5':
            print('Выход из программы.')
            break
        else:
            print('Ошибка: Неправельный выбор, выберите опцию снова.')

if __name__ == '__main__':
    main()    
    







