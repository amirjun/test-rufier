from PyQt5.QtCore import QTime
win_x, win_y = 200, 100
win_width, win_height = 1000, 600

txt_hello = 'Добро пожаловать в программу по определению состояния здоровья!'
txt_next = 'Начать'
txt_instruction = (
    'Данное приложение позволит вам с помощью тестаРуфье провести первичную диагностику вашего здоровья.\n'
    'Проба Руфье представляет собой нагрузочный комплекс, предназначеный для оценки работоспособности сердца при физических нагрузках.\n'
    'У испытуемого, находящегося в положении лёже на спине в течении 5 мин, определяют частоту пульса за первые 15 секунд;\n'
    'Затем в течении 45 минут испытуемый выполняет 30 приседаний.\n'
    'После окончания нагрузки испытуемый ложится, и у неговновь подчитывается число пульсаций за первые 15 секунд.\n'
    'а потом - за последнии 15 секунд первой минуты периода восстановления.\n'
    'Важно! Если в процессе проведения испытания вы почуствуете себя плохо(появится головокружение, шум в\n'
    'ушах сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.') 
txt_title = 'Здоровье'
txt_name = 'Введите Ф.И.О.:'
txt_hintname = "Ф.И.О."
txt_hintage = "0"
txt_test1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультатзапишите в соответствующее поле.'
txt_test2 = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.'
txt_test3 = 'Лягте на спину и замерьте пульс сначала за первые 15 секундминуты, затем за последние 15 секунд.\nНажмите на кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды,в течение которых необходимо \nпроводить измерения, черным - минуты без замер пульсации. Результатызапишите в соответствующие поля.'
txt_sendresults = 'Отправить результаты'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Начать первый тест'
txt_starttest2 = 'Начать делать приседания'
txt_starttest3 = 'Начать финальный тест'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Полных лет'
txt_finalwin = 'Результаты'
txt_index = 'Индекс Руфье: '
txt_heartwork = 'Работоспособность сердца: '
txt_res1 = 'низкая. Срочно обратитесь к врачу!'
txt_res2 = 'удовлетворительная.Обратитесь к врачу!'
txt_res3 = 'средняя. Возможно, стоит дополнительно обследоваться у врача.'
txt_res4 = 'выше среднего'
txt_res5 = 'высокая'