import random as r

action = input('Выберите число от одного до трёх')
if action == '1':
    print('Вы встали с постели')
    action = input('Выберите число от одного до трёх: 1. Выйти на улицу 2. Остаться дома 3. Лечь спать')
    if action == '1':
        print('Вы вышли на улицу')
        action = input('Выберите число от одного до двух 1. Пойти прямо 2. Остаться на месте')
        if action == '1':
            action = input('Вы встретили указатель. Выберите направление 1.Тренировочный лагерь воинов 2.Школа '
                           'разбойников'
                           '3.Академия волшебников ')
            if action == '1':
                action = input('Вы прибыли в тренировочный лагерь. Подойти к мастеру? 1. Да 2. Нет ')
                if action == '1':
                    action = input(
                        'Вы подошли к мастеру. Вы согласны пройти обучение и стать воином? 1.Да 2.Пока подумаю ')  #

                    if action == '1':
                        war_inventory = ['Деревянный меч', 10, 'Щит', 10, 'Нагрудник', 10, 'Штаны', 10, 'Шлем', 10,
                                         'Ботинки', 10, 'Перчатки', 10]
                        action = input(
                            'Мастер говорит: Отлично. Возьми этот меч и отправляйся убивать монстров недалеко '
                            'от входа.'
                            '1. Отправиться на охоту 2. Пока подождать ')
                        if action == '1':
                            action = input('Вы увидели монстра. 1. Атаковать его мечом 2. Убежать ')
                            if action == '1':
                                print(f'Вы сразили монстра свои мечом, нанеся ему {r.randint(10, 15)} урона. ')
                                war_inventory[1] -= 1
                                print(f'Прочность меча уменьшилась. Текущая прочность: {war_inventory[1]}')
                                print('После убийства монстра вы возвращаетесь к мастеру. Он говорит: "Ты '
                                      'справился с заданием, воин. Возьми эти 10 золотых и зелья здоровья, '
                                      'они пригодятся тебе в твоих приключениях. ')
                                print('Мастер говорит "Теперь отправляйся в гробницу к северу от лагеря, там обитает '
                                      'тролль, который совершает набеги на деревню и не даёт крестьянам спокойно '
                                      'жить. Твоя задача убить его. Чтобы проникнуть в склеп тебе потребуется этот '
                                      'ключ.')
                                war_inventory_expendable = ['Золотые монеты', 10, 'Малое зелье здоровья', 5, 'Ключ от '
                                                                                                             'гробницы',
                                                            1]
                                action = input('Отправиться на выполнение задания? 1. Да 2. Нет')
                                if action == '1':
                                    action = input('После недолгого пути на север вы прибыли к гробнице. На входе в '
                                                   'склеп висит большой ржавый замок. Мастер говорил что-то про ключ. '
                                                   '1. Использовать ключ 2. Попытаться сломать замок мечом')
                                    if action == '1':
                                        war_inventory_expendable[5] = 0
                                    else:
                                        print('Вы попытались сломать замок мечом, но он оказался слишком крепким. '
                                              'Возможно, стоит использовать ключ, который дал мастер')
                                    if war_inventory_expendable[5] == 0:
                                        action = input('Проникнув в склеп вы увидели огромного тролля, склонившегося '
                                                       'над трупом крестьянина. 1. Атаковать его 2. Убежать')
                                        if action == '1':
                                            action = input('Тихо подкравшись вы атаковали тролля мечом сзади. Издав '
                                                           'истошный рык, он развернулся и ударил вас своей когтистой '
                                                           'лапой. Кажется, нужно срочно использовать зелье здоровья. '
                                                           '1. Использовать зелье 2. Продолжить бой')
                                            if action == '1':
                                                war_inventory_expendable[3] -= 1
                                                print('Отскочив назад, вы выпили зелье здоровья. Вам сразу же стало '
                                                      f'лучше. Вторым точным ударом вы сразили тролля наповал, нанеся '
                                                      f'ему {r.randint(10, 15)} урона  . Забрав'
                                                      'стоявший рядом с ним мешок, вы отправились обратно к мастеру.')
                                                war_inventory_expendable.append('Мешок из гробницы')
                                                print('Прибыв к мастеру вы протянули ему мешок. Достав из мешка '
                                                      'костяную подвеску, он говорит "Отлично, воин. Возьми этот '
                                                      'амулет тролля. Он будет доказательством твоей силы. Собрав ещё '
                                                      'несколько таких амулетов ты сможешь обрести новую силу.')
                                                war_inventory_expendable.pop(-1)
                                                war_inventory_quest = ['Костяной амулет тролля', 1]

                                            else:
                                                print('Вторым ударом тролль убил вас')
                                        else:
                                            print('Вы убежали из пещеры')
                                    else:
                                        print('Используйте ключ!')

                                else:
                                    print('Вы остались стоять на месте')
                            else:
                                print('Вы убежали')
                        else:
                            print('Вы остались ждать')

                    else:
                        print('Вы молча стоите в раздумиях ')
                else:
                    print('Вы остались стоять на входе в лагерь ')

            elif action == '2':
                action = input('Вы пришли к школе разбойников. Подойти к мастеру? 1. Да 2. Нет '
                               '')
                if action == '1':
                    action = input('Мастер говорит: "Ты готов пройти обучение и стать разбойником?" 1. Да 2. Нет')
                    if action == '1':
                        rogue_inventory = ['Деревянный лук', 10, 'Кожаная рубаха', 10, 'Кожаные штаны', 10, 'Кожаный '
                                                                                                            'шлем',
                                           10, 'Кожаные ботинки', 10, 'Кожаные перчатки', 10]
                        action = input('Отлично! Возьми этот лук и стрелы и отправляйся на охоту на монстров. 1. '
                                       'Отправиться на охоту 2. Остаться на месте')
                        if action == '1':
                            action = input('Вы увидели монстра. 1. Выстрелить в него 2. Ударить его луком 3. Убежать ')
                            if action == '1':
                                print(f'Вы убили монстра метким выстрелом из лука, нанеся ему {r.randint(12,18)} урона ')
                                rogue_inventory[1] -= 1
                                print(f'Прочность оружия уменьшилась. Текущая прочность: {rogue_inventory[1]}')
                                print('После убийства монстра вы возвращаетесь к мастеру. Он говорит: "Ты '
                                      'справился с заданием, воин. Возьми эти 10 золотых и зелья здоровья, '
                                      'они пригодятся тебе в твоих приключениях. ')
                                print('Мастер говорит "Теперь отправляйся в гробницу к северу от лагеря, там обитает '
                                      'тролль, который совершает набеги на деревню и не даёт крестьянам спокойно '
                                      'жить. Твоя задача убить его. Чтобы проникнуть в склеп тебе потребуется этот '
                                      'ключ.')
                                rogue_inventory_expendable = ['Золотые монеты', 10, 'Малое зелье здоровья', 5, 'Ключ от'
                                                                                                               'гробницы',
                                                              1]
                                action = input('Отправиться на выполнение задания? 1. Да 2. Нет')
                                if action == '1':
                                    action = input('После недолгого пути на север вы прибыли к гробнице. На входе в '
                                                   'склеп висит большой ржавый замок. Мастер говорил что-то про ключ. '
                                                   '1. Использовать ключ 2. Попытаться снять замок руками')
                                    if action == '1':
                                        rogue_inventory_expendable[5] = 0
                                    else:
                                        print('Вы попытались сломать замок мечом, но он оказался слишком крепким. '
                                              'Возможно, стоит использовать ключ, который дал мастер')
                                    if rogue_inventory_expendable[5] == 0:
                                        action = input('Проникнув в склеп вы увидели огромного тролля, склонившегося '
                                                       'над трупом крестьянина. 1. Атаковать его 2. Убежать')
                                        if action == '1':
                                            action = input('Вы выстрелили в тролля. Издав '
                                                           'истошный рык, он развернулся и набросился на вас. '
                                                           'Кажется, нужно срочно использовать зелье здоровья.'
                                                           '1. Использовать зелье 2. Продолжить бой')
                                            if action == '1':
                                                rogue_inventory_expendable[3] -= 1
                                                print('Отскочив назад, вы выпили зелье здоровья. Вам сразу же стало '
                                                      f'лучше. Вторым точным выстрелом вы сразили тролля наповал, '
                                                      f'нанеся ему {r.randint(12,18)} урона . Забрав'
                                                      'стоявший рядом с ним мешок, вы отправились обратно к мастеру.')
                                                rogue_inventory_expendable.append('Мешок из гробницы')
                                                print('Прибыв к мастеру вы протянули ему мешок. Достав из мешка '
                                                      'костяную подвеску, он говорит "Отлично, разбойник. Возьми этот '
                                                      'амулет тролля. Он будет доказательством твоей силы. Собрав ещё '
                                                      'несколько таких амулетов ты сможешь обрести новую силу.')
                                                rogue_inventory_expendable.pop(-1)
                                                rogue_inventory_quest = ['Костяной амулет тролля', 1]
                                            else:
                                                print('Тролль ударил вас ещё раз и вы погибли')
                                        else:
                                            print('Вы убежали')
                                    else:
                                        print('Вы остались стоять на месте')
                            elif action == '2':
                                print('Вы попытались ударить монстра луком, но он напал на вас и убил. ')
                            else:
                                print('Вы убежали прочь')
                        else:
                            print('Вы остались стоять на месте')
                    else:
                        print('Вы остались стоять в раздумиях')
                else:
                    print('Вы остались стоять на входе в школу')
            if action == '3':
                action = input('Вы прибыли в академию волшебников. Подойти к верховному магу? 1. Да 2. Нет')
                if action == '1':
                    action = input('Верховный маг спрашивает: "Ты готов пройти обучение и стать волшебником?" 1. Да. '
                                   '2. Нет')
                    if action == '1':
                        mage_inventory = ['Деревянный посох', 10, 'Мантия мага', 10, 'Штаны мага', 10, 'Диадема мага',
                                          10, 'Ботинки мага', 10, 'Перчатки мага', 10]
                        action = input('Похвально, тогда держи эту книгу мага и посох, отправляйся отрабатывать '
                                       'самое'
                                       'первое заклинание на монстрах близь академии. 1. Отправиться 2. Остаться на '
                                       'месте')
                        if action == '1':
                            action = input('Вы увидели монстра. 1. Использовать заклинание 2. Ударить кулаком 3. '
                                           'Убежать')
                            if action == '1':
                                print(f'Вы прочли заклинание, нанеся монстру {r.randint(15,20)} урона, и монстр упал '
                                      f'замертво')
                                mage_inventory[1] -= 1
                                print(f'Прочность оружия уменьшилась. Текущая прочность: {mage_inventory[1]}')
                                print('После убийства монстра вы возвращаетесь к мастеру. Он говорит: "Ты '
                                      'справился с заданием, волшебник. Возьми эти 10 золотых и зелья здоровья, '
                                      'они пригодятся тебе в твоих приключениях. ')
                                print('Мастер говорит "Теперь отправляйся в гробницу к северу от лагеря, там обитает '
                                      'тролль, который совершает набеги на деревню и не даёт крестьянам спокойно '
                                      'жить. Твоя задача убить его. Чтобы проникнуть в склеп тебе потребуется этот '
                                      'ключ.')
                                mage_inventory_expendable = ['Золотые монеты', 10, 'Малое зелье здоровья', 5, 'Ключ от '
                                                                                                              'гробницы',
                                                             1]
                                action = input('Отправиться на выполнение задания? 1. Да 2. Нет')
                                if action == '1':
                                    action = input('После недолгого пути на север вы прибыли к гробнице. На входе в '
                                                   'склеп висит большой ржавый замок. Мастер говорил что-то про ключ. '
                                                   '1. Использовать ключ 2. Попытаться сломать замок руками')
                                    if action == '1':
                                        mage_inventory_expendable[5] = 0
                                    else:
                                        print('Вы попытались сломать замок мечом, но он оказался слишком крепким. '
                                              'Возможно, стоит использовать ключ, который дал мастер')
                                    if mage_inventory_expendable[5] == 0:
                                        action = input('Проникнув в склеп вы увидели огромного тролля, склонившегося '
                                                       'над трупом крестьянина. 1. Атаковать его 2. Убежать')
                                        if action == '1':
                                            action = input('Вы атаковали тролля боевым заклинанием. Издав '
                                                           'истошный рык, он развернулся, подбежал к вам и ударил '
                                                           'своей когтистой'
                                                           'лапой. Кажется, нужно срочно использовать зелье здоровья. '
                                                           '1. Использовать зелье 2. Продолжить бой')
                                            if action == '1':
                                                mage_inventory_expendable[3] -= 1
                                                print('Отскочив назад, вы выпили зелье здоровья. Вам сразу же стало '
                                                      f'лучше. Вторым заклинанием вы сразили тролля, нанеся ему {r.randint(12,18)} урона. Забрав'
                                                      'стоявший рядом с ним мешок, вы отправились обратно к мастеру.')
                                                mage_inventory_expendable.append('Мешок из гробницы')
                                                print('Прибыв к мастеру вы протянули ему мешок. Достав из мешка '
                                                      'костяную подвеску, он говорит "Отлично, волшебник. Возьми этот '
                                                      'амулет тролля. Он будет доказательством твоей силы. Собрав ещё '
                                                      'несколько таких амулетов ты сможешь обрести новую силу.')
                                                mage_inventory_expendable.pop(-1)
                                                mage_inventory_quest = ['Костяной амулет тролля', 1]
                                            else:
                                                print('Вторым ударом тролль убил вас')
                                        else:
                                            print('Вы убежали')
                            elif action == '2':
                                print('Вы замахнулись на монстра кулаком, но он оказался быстрее и разорвал вас '
                                      'своими лапами')
                            else:
                                print('Вы убежали')
                        else:
                            print('Вы остались стоять в раздумиях')
                else:
                    print('Вы остались стоять у входа в академию')
        else:
            print('Вы остались стоять у дома')

    elif action == '2':
        print('Вы остались дома')
    else:
        print('Вы легли обратно спать')

elif action == '2':
    print('Вы остались дома')
elif action == '3':
    print('Дальше спим')
else:
    print('Выберите число от 1 до 3')
