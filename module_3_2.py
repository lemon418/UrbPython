def send_email(message, recipient, sender = "university.help@gmail.com" ):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        sign1 = recipient.find('@')
        sign2 = sender.find('@')

        if ((recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and
            (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
            if sign1 > -1 and sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
            elif sign1 > -1 and sign2 > -1:
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            else:
                 print(f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}.')
        else:
            print(f'Невозможно отправить письмо с адреса {recipient} на адрес {sender}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
