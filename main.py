import random
from random import randint

import requests
import telebot
from telebot import types

from config import TgBot_Token, WeatherAPI

TextMessageAnswerChance = 50
bot = telebot.TeleBot(TgBot_Token)


# VARIABLES=====Чем больше число тем меньше шанс===== [> = 1]

PhotoMessageAnswerChance = 2
VideoMessageAnswerChance = 2

# CONST_ARRAYS======================================
photoPhrases = ["Дэм бро на этом фото ты изобразил заебись вещь!!",
                "Чел я конечно все понимаю но такое я не оценю поверь", "Сходи в дурку подлечись клоуняра",
                "более менее я хуе как разобрал что за хуйня на этом фото\n\nсходи купи камеру получше",
                "ахуеть не встать", "я шокирован увиденным, ты чел лютый!!",
                "я ничего так и не смог понять, нормальное фото пришли", "чел мне за тебя стыдно",
                "могу с уверенностью сказать что на фото изображена фигня!!11!!",
                "ну и зачем ты эту фотку прислал?", "еще раз такое фото говяное прищлешь, удалю к чертовой матери!",
                "вы мистер, я смотрю ахуели такой фотоконтент присылать!?",
                "чел был бы ты ромчиком я бы еще простил это фото", "похуй на фото, видео кидай",
                "я по-ботовскому за тебя рад!!", "это фото кинул стаммо?\n если нет то это пиздец",
                "норм фото, только в следующий раз держи камеру ровно",
                "ну что я тут могу сказать, я все равно за это не шарю",
                "чел шо за фото ты кинул, не присылай такое больше!!",
                "ВЫ получили СЕкРетную реакцию на фото!&!!!!!&%*#\n\n(шанс ее получения 84% ахахахахах)",
                "идеи как на такое фото ответить у меня кончились честно...", "мне особо все равно на это фото",
                "фото топчик", "где такое купить, как на фото??", "чел купи мозги и не снимай больше такое!!",
                "-_-", ":\\", "по итогу ничего позитивного сказать не могу(", "мне такое фото нрав!"]

videoPhrases = ["пупа может круче, чем здесь показано!!", "моя реакция на это видео бесценна",
                "рома клоп +видео хуета", "шев недоволен этим видеоконтентом", "дэм бро найс видео",
                "чел удали этот видос и не присылай такое больше", "видеоматериал кал", "лайк подписка",
                "дызлайк отписка", "чел шо ты снял", "ты хоть сам понимаешь что на этом видео?"]

Myds = ["Сложнее всего начать действовать, все остальное зависит только от упорства.\n\nАмелия Эрхарт",
        "Вы никогда не пересечете океан, если не наберетесь мужества потерять берег из виду.\n\nХристофор Колумб",
        "Есть только один способ избежать критики: ничего не делайте, ничего не говорите и будьте никем.\n\nАристотель",
        "Лучше быть уверенным в хорошем результате, чем надеяться на отличный.\n\nУоррен Баффет",
        "Когда закрывается одна дверь к счастью, тут же открывается другая. Но мы часто так долго смотрим на первую, что не замечаем вторую.\n\nЭлен Келлер",
        "Успех — это способность идти от поражения к поражению, не теряя оптимизма\n\nУинстон Черчилль",
        "Неудача – это просто возможность начать снова, но уже более мудро.\n\nГенри Форд",
        "Никогда не делает ошибок только тот, кто не пробует ничего нового.\n\nАльберт Эйнштейн",
        "Не столь важно, как медленно ты идешь, как то, как долго ты идешь, не останавливаясь.\n\nКонфуций",
        "Мир делится на два класса — одни веруют в невероятное, другие совершают невозможное.\n\nОскар Уайлд",
        "Выживает не самый сильный, а самый восприимчивый к переменам.\n\nЧарльз Дарвин",
        "Когда кажется, что весь мир настроен против вас, вспомните, что самолет взлетает не по ветру, а против него.\n\nГенри Форд",
        "Единственный способ сделать что-то очень хорошо – любить то, что ты делаешь.\n\nСтив Джобс",
        "У истоков каждого успешного предприятия стоит однажды принятое смелое решение.\n\nПитер Друкер"]

Faces = ["\U0001F609", "\U0001F618", "\U0001F975", "\U0001F974", "\U0001F60E", "\U0001F480", "\U0001F479",
         "\U0001F921", "\U0001F608", "\U0001F64A", "\U00002764", "\U0001F595", "\U0001F44E", "\U0001F44D"]

reactPhotos = [open("Answers/reactions/img_1.png", "rb"), open("Answers/reactions/img_2.png", "rb"), open("Answers/reactions/img_3.png", "rb"),
            open("Answers/reactions/img_4.png", "rb"),
            open("Answers/reactions/img_5.png", "rb"),
            open("Answers/reactions/img_6.png", "rb"),
            open("Answers/reactions/react1.png", "rb"),
            open("Answers/reactions/react2.png", "rb"),
            open("Answers/reactions/react3.png", "rb"),
            open("Answers/reactions/react4.png", "rb"),
            open("Answers/reactions/react5.png", "rb"),
            open("Answers/reactions/react6.png", "rb"),
            open("Answers/reactions/react7.png", "rb"),
            open("Answers/reactions/react8.png", "rb"),
            open("Answers/reactions/react9.png", "rb"),
            open("Answers/reactions/react10.png", "rb"),
            open("Answers/reactions/react11.png", "rb"),
            open("Answers/reactions/react12.png", "rb"),
            open("Answers/reactions/react13.png", "rb"),
            open("Answers/reactions/react14.png", "rb"),
            open("Answers/reactions/react15.png", "rb"),
            open("Answers/reactions/react16.png", "rb"),
            open("Answers/reactions/react17.png", "rb"),
            open("Answers/reactions/react18.png", "rb")]

phrase = [f'Дэм, бро, найс сообщение',
              f'шо ты скинул чел прими таблетки от шизы',
              f'о, Мне такое  по душе',
              f'Шеф недоволен, переделывай', 'Ну ок',
              'На фото изображена фигня!11!', 'это ашкуди?',
              f'я могу лучше',
              'Z', "так нахуй я бот ты слит", " ну что тут можно сказать", "чел сверху ахуенен", "ГеЙ бомба: если никто не ответит в течение 10 мин, бомба взорвется и все станут геями!!", "витя лох", "пупа топ", "так я не понял, ты ахуел?", "мне кажется что ты хахуел" , "я бот ты компот", "верхний, ебало офф", "ты не прав", "ты прав", "ок", "чел дело базарит", "я шарю", "хуйню сказал", "очень много хуйни сказал", "я согласен", "админ в чате ебало офф", "аъахххахахахахахахах", "ебать разрыв", "вопрос: ты хуесос?", "без б", "я посылаю тебя нахуй", "чел хорош", "чел плох", "хахахах ебать рофлан", "@Sh1i1sh", "@Vladq777", "ей @De44iK меня пиздят спасай", "люто", "пиздец", "ахуел?", "рома клоп", "а вы знали что вышла кс 2?", "ладно я гей", "...", "я промолчу","че за хуйню ты сказал?", "ты про меня не шути", ")))", "да я ахуел", "а че, я настырный как хуй по утрам", "да, вопросы?", "нет, вопросы?", "вот ты меня спросишь, а я нихуя не отвечу", "где твоя совесть?", "мама увидит по попе даст", "так кто это тут ахуел?"]

anekdotPhrases = ["Берегись, кидаю разрывную!! Выбирай:", "Тут полно лютых, выбирай)", "че, устроим цирк?", "кныш, я вызываю тебя на анекдот-баттл со мной", "разрыв жопы обеспечен", "может вариантов пока что мало, но зато какие)", "вышел заяц на крыльцо...выбирать анекдот", "выбирай", "кнопки видишь? так тыкай", "таки норм анекдот про еврея", "вы спросите - \"Где пупа?\" А я отвечу что он помер со смеху", "выбирай, не стесняйся)", "я заебался писать эти заголовки если честно - Ден4ик", "почему так", "анекдот сам себя не выберет", "админ в чате читает анекдоты", "база данных что надо", "\U0001F921", "\U0001F608", "ложись, разрывная"]

anekdots = ["Штирлиц стрелял вслепую. Слепая испугалась и побежала скачками, но качки быстро отстали.", "Штирлиц шёл по улице, когда внезапно перед ним что-то упало. Штирлиц поднял глаза -- это были глаза профессора Плейшнера.", "Штирлицу попала в голову пуля. \"Разрывная,\" - раскинул мозгами Штирлиц.", "— Моня, почему ты не даришь мне цветы?\n— Циля, я подарил тебе весь мир! Иди нюхай цветы на улицу!..", "— Расскажи-ка нам, Вовочка, что надо сделать, чтобы попасть в рай?\n— Сдохнуть надо, дяденька священник!", "— Будешь выходить — труп вынеси!\n— Может быть, мусор?\n— Может — мусор, может — сантехник, бог его знает…", "— Беня, я гарантирую вам, шо через пять лет мы будем жить лучше, чем в Европе!\n— А шо у них случится?", "Когда изобретатель USB-порта умрет, его гроб сначала опустят в яму, потом поднимут и перевернут и опустят снова правильной стороной." , "— Кот умер год назад. Так я до сих пор замедляю шаг в коридоре, там, где он любил лежать, чтобы не споткнуться об него в темноте.— Может, пора его похоронить?", "Если бы моя бабушка знала, сколько денег я сэкономил на ее похоронах, то она бы перевернулась в канаве."]
# BOT_INFO===========================================

photRe = len(photoPhrases)
mydRe = len(Myds)
facRe = len(Faces)
phRe = len(phrase)
vidRe = len(videoPhrases)
# MAIN_CMD===========================================

@bot.message_handler(commands=["start"])
def commands(message):

    bot.send_message(message.chat.id,
                     f"⠀⠀⠀\U0001F975\U0001F975\U0001F975Бот онлайн\U0000203C\n\U0001F60EИ теперь он в край ахуел\U0001F60E\n\n  /cmds | /knyshVer")


@bot.message_handler(commands=["calc"])
def calc(message):
    msg_split = message.text.split(' ')
    try:
        otv = 0
        match msg_split[2]:
            case '+':
                otv = float(msg_split[1]) + float(msg_split[3])
            case '-':
                otv = float(msg_split[1]) - float(msg_split[3])
            case '*':
                otv = float(msg_split[1]) * float(msg_split[3])
            case '/':
                otv = float(msg_split[1]) / float(msg_split[3])
            case '^':
                otv = float(msg_split[1]) ** float(msg_split[3])
        bot.send_message(message.chat.id, f"Ответ: {otv}")

    except:
        bot.send_message(message.chat.id, "Недопустимый пример")

@bot.message_handler(commands=["cmds"])
def cmds(message):
    bot.send_photo(message.chat.id, open("Answers/changelog/Commands.png", "rb"))

@bot.message_handler(commands=["knyshVer", "knyshver", "KnyshVer", "Knyshver"])
def ver(message):
    bot.send_photo(message.chat.id, open("Answers/changelog/Changelog.png", "rb"))
    bot.send_message(message.chat.id,
                     f"\U0001F533 Версия: KnyshBot ver 5.0.1 release update\n\U0001F533 Всего реакций: {vidRe + photRe + mydRe + facRe + phRe}\n\nИз них:\n\U000025AA Реакций на текст: {phRe}\n\U000025AB Реакций на фото: {photRe}\n\U000025AA Реакций на видео: {vidRe}\n\U000025AB Мудрых фраз: {mydRe}")


# TEXT_HANDLER=======================================

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    msg_split = message.text.split(' ')

    # USR_ARRAYS =============================

    if message.text == "Пошел нахуй" or message.text == "Иди нахуй" or message.text == "пошел нахуй" or message.text == "иди нахуй":
        bot.send_message(message.chat.id, "Сам пошел нахуй, токсик\U0001F92C", parse_mode='html')

    elif message.text == "Мудрое дерево" or message.text == "мудрое дерево":

        mydRand = randint(0, len(Myds) - 1)
        bot.send_message(message.chat.id, Myds[mydRand])

    elif message.text == "Рожа" or message.text == "рожа":

        bot.send_message(message.chat.id, Faces[random.randint(0, len(Faces) - 1)])

    # WEATEHR_STRT ==================================================
    elif msg_split[0] == "Погода" or msg_split[0] == "погода":

        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={msg_split[1]}&appid={WeatherAPI}&units=metric"
            )
            data = r.json()

            cur_weather = data["main"]["temp"]
            wind = data["wind"]["speed"]
            weather_description = data["weather"][0]["main"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "ERROR, contact admin"
            bot.send_message(message.chat.id,
                             f"\U00002600\U0001F975 ПОГОДА ОТ ДЕ44ИКА \U00002744\U0001F976\n\n"
                             f"\U000025AA Погода в городе: {msg_split[1]}\n\U000025AB Температура: <b>{cur_weather}C°</b> {wd}\n\U000025AA Ветер: {wind} м/с\n\U000025AB Влажность: {humidity}%\n\U000025AA Давление: {pressure} мм.рт.ст\n", parse_mode='html')


        except:
            bot.send_message(message.chat.id, "Проверьте название города")

        # WEATEHR_END ============================================================

    elif message.text == "Aperol" or message.text == "aperol":
        photo_aperol1 = open("186620868.jpg", "rb")
        photo_aperol2 = open("img_13.png", "rb")
        photo_aperol3 = open("img_14.png", "rb")
        photo_aperol4 = open("img_15.png", "rb")
        aperolist = [photo_aperol1, photo_aperol2, photo_aperol3, photo_aperol4]
        randd = randint(0, 3)
        bot.send_photo(message.chat.id, aperolist[randd])
        if randd == 3:
            bot.send_message(message.chat.id, "Может вот это?")

    elif message.text == "Hqd" or message.text == "hqd":
        photo_ahka1 = open("Answers/hqd/img.png", "rb")
        photo_ahka2 = open("Answers/hqd/img_7.png", "rb")
        photo_ahka3 = open("Answers/hqd/img_8.png", "rb")
        photo_ahka4 = open("Answers/hqd/img_9.png", "rb")
        photo_ahka5 = open("Answers/hqd/img_10.png", "rb")
        photo_ahka6 = open("Answers/hqd/img_11.png", "rb")
        photo_ahka7 = open("Answers/hqd/img_12.png", "rb")
        ahki = [photo_ahka1, photo_ahka2, photo_ahka3, photo_ahka4, photo_ahka5, photo_ahka6, photo_ahka7]
        rad = randint(0, 6)
        bot.send_photo(message.chat.id, ahki[rad])

    elif message.text == "Ок" or message.text == "Пон" or message.text == "Понял" or message.text == "ок" or message.text == "пон" or message.text == "понял":
        bot.send_message(message.chat.id, "Я тоже понял", parse_mode='html')

    elif message.text == "Команды" or message.text == "команды":
        bot.send_message(message.chat.id,
                         "\U00002705 Добро пожаловать в список команд \U0001F609:\n\n\U0001F539 Ид - узнать кныш-айди \U0001F194\n\n\U0001F539 Aperol - прислать апероль \U0001F943\n\n\U0001F539 Погода - узнать погоду где угодно! (пример: погода Одесса)\n\n\U0001F539Hqd - прислать ашкудишку \U0001F6AC\n\n\U0001F539 Кал - калькулятор епта))(пример: \"кал 2 + 2\")\n\n\U0001F539 Ебало - отправить рандом ебало (внимание, может выпасть клоуняра!!)\n\n\U0001F539 ДТ - узнать дату и время (хз зачем)\n\n\U0001F539 КнышВер - узнать информацию о текущей версии KnyshBot\n\n\U0001F539 Муд — скинуть рандом мудрую цитату\n\n\U0001F539 ",
                         parse_mode='html')

    elif msg_split[0] == "Настырность" or msg_split[0] == "настырность":
        if int(msg_split[1]) > 0 and int(msg_split[1]) < 6:
            global TextMessageAnswerChance
            match int(msg_split[1]):
                case 1:
                    TextMessageAnswerChance = 100
                case 2:
                    TextMessageAnswerChance = 50
                case 3:
                    TextMessageAnswerChance = 30
                case 4:
                    TextMessageAnswerChance = 15
                case 5:
                    TextMessageAnswerChance = 1

            bot.send_message(message.chat.id, f"Настырность бота установлена в значение {msg_split[1]}")
        else:
            bot.send_message(message.chat.id, f"Ошибка: Некорректное значение {msg_split[1]}\nВозможны значения от 1 до 5")
    elif message.text == "Анекдот" or message.text == "анекдот":

        markupAnekdot = types.InlineKeyboardMarkup(row_width=1)
        i1 = types.InlineKeyboardButton("Разрывной про Штирлица", callback_data="a1")
        i2 = types.InlineKeyboardButton("Такой же как первый", callback_data="a2")
        i3 = types.InlineKeyboardButton("Еще один", callback_data="a3")
        i4 = types.InlineKeyboardButton("Лютый про еврея)", callback_data="a4")
        i5 = types.InlineKeyboardButton("Про Вовочку", callback_data="a5")
        i6 = types.InlineKeyboardButton("Чернее негра", callback_data="a6")
        i7 = types.InlineKeyboardButton("Еврейский Евопейский", callback_data="a7")
        i8 = types.InlineKeyboardButton("Рофляный", callback_data="a8")
        i9 = types.InlineKeyboardButton("Вонючий", callback_data="a9")
        i10 = types.InlineKeyboardButton("Канавный", callback_data="a10")

        markupAnekdot.add(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10)

        bot.send_message(message.chat.id,
                         anekdotPhrases[random.randint(0, len(anekdotPhrases) - 1)],
                         reply_markup=markupAnekdot)

        @bot.callback_query_handler(func=lambda call: True)
        def callbackAn(call):
            if call.message:
                if call.data == "a1":
                    bot.send_message(message.chat.id, anekdots[0])
                if call.data == "a2":
                    bot.send_message(message.chat.id, anekdots[1])
                if call.data == "a3":
                    bot.send_message(message.chat.id, anekdots[2])
                if call.data == "a4":
                    bot.send_message(message.chat.id, anekdots[3])
                if call.data == "a5":
                    bot.send_message(message.chat.id, anekdots[4])
                if call.data == "a6":
                    bot.send_message(message.chat.id, anekdots[5])
                if call.data == "a7":
                    bot.send_message(message.chat.id, anekdots[6])
                if call.data == "a8":
                    bot.send_message(message.chat.id, anekdots[7])
                if call.data == "a9":
                    bot.send_message(message.chat.id, anekdots[8])
                if call.data == "a10":
                    bot.send_message(message.chat.id, anekdots[9])



    else:
        caseText = randint(0, TextMessageAnswerChance)
        if caseText == 1:
            bot.reply_to(message, phrase[random.randint(0, len(phrase) - 1)])
        elif caseText == 2:
            bot.send_photo(message.chat.id, reactPhotos[random.randint(0, len(reactPhotos) - 1)])


# PHOTO_HANDLER ==========================================
@bot.message_handler(content_types=['photo'])
def get_user_text1(message):
    bot.reply_to(message, photoPhrases[random.randint(0, len(photoPhrases) - 1)])


# VIDEO_HANDLER ==========================================
@bot.message_handler(content_types=['video'])
def get_user_video(message):
    bot.reply_to(message, videoPhrases[random.randint(0, len(videoPhrases) - 1)])


bot.polling(none_stop=True, interval=0)
