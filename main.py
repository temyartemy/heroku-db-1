import logging
from aiogram import Bot, Dispatcher, executor, types

import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import Text

bot = Bot(token="5244928426:AAG89A2EAvyif48BJpxviAlqQstAjV6dMHg")

dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

@dp.message_handler(Text(equals="Інструкція"))
async def cmd_help(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["На головну"]
    keyboard.add(*buttons)
    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold("Hello!")),
            fmt.text("Цей бот призначений для наступного:"),
            fmt.text(fmt.hbold("1)Міста."),
                     "Тут ви можете отримати посилання на основні інфо-чати певних міст України."),
            fmt.text(
                fmt.text(fmt.hbold("2)Транспорт."), "Тут будуть наведені чати по 2 категоріях:"),
                fmt.text(fmt.hitalic("2.1) Чат водіїв."),
                         "Отримайте чати для доступу до актуального авто-життя країни!"),
                fmt.text(fmt.hitalic("2.2) Чат Укрзалізниці."),
                         "Отримайте чати з інфою щодо теперешніх перевезень потягами."),
                sep='\n'
            ),
            fmt.text(fmt.hbold("3)Загальні джерела."),
                     "Наявні як офіційні, так і неофіційні джерела інформації. Було додано іноземні ЗМІ, адже декілька точок зору породжують краще розуміння ситуації."),
            fmt.text(
                fmt.text(fmt.hbold("4)Допомога."), "Тут будуть наведені чати по 2 категоріях:"),
                fmt.text(fmt.hitalic("4.1) Житло."),"Оберіть місто, проживання в якому вас цікавить. Там будуть окремі чати."),
                fmt.text(fmt.hitalic("4.2) Волонтерство."), "Наявні основні чати задля допомоги по всій країні"),
                sep='\n'
                     ),
            fmt.text("Якщо виникають якісь питання або пропозиції, то буду надзвичайно радий, якщо отримаю їх в особисті повідомлення!",
                     "Для зв'язку зі мною треба перейти до:", fmt.hbold("Адмін, є питаннячко!")),
            fmt.text(fmt.hitalic("Будь-ласка, не намагайтеся ламати мого бота усілякими смс-нісенітницями!"),
                     "На будь-якому етапі використання бота ви можете прописувати вручну фрази із усіх існуючих кнопок, навіть якщо цих кнопок наразі немає на екрані"),
            fmt.text("Визначення: ламати бота - надсилати будь-який текст, що не передбачений кнопками бота"),
            sep='\n\n'
        ), parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Загальні джерела", "Міста", "Допомога",
               "Транспорт","Інструкція", "Адмін, є питаннячко!"]
    keyboard.add(*buttons)
    await message.answer("Сміливі завжди мають щастя...тож будь сміливим - обери щось:", reply_markup=keyboard)

@dp.message_handler((Text(equals="Допомога")))
async def helper(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Житло", "Волонтерство", "На головну"]
    keyboard.add(*buttons)

    await message.answer("Обирайте бажане:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Волонтерство"))
async def cmd_admin(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold("Слід одразу зрозуміти, що всі волонтерські питання можна знайти також і в загальних інфо-чатах відповідного міста!")),
            fmt.text(fmt.hitalic("Для IT-армії #1"), 'https://t.me/itforua'),
            fmt.text(fmt.hitalic("Для IT-армії #2"), 'https://t.me/+9GPKhDPGHPAzZjdi'),
            fmt.text(fmt.hitalic("Для Луцька"), 'https://t.me/V_Lutsk'),
            fmt.text(fmt.hitalic("Для Харкова"), 'https://t.me/volontery_kh'),
            fmt.text(fmt.hitalic("Для Києва"), 'https://t.me/volonterykyiv'),
            fmt.text(fmt.hitalic("Для Тернополя"), 'https://t.me/volonteryternopil'),
            fmt.text(fmt.hitalic("Для Донбасу"), 'https://t.me/KirillovTalk'),
            fmt.text(fmt.hitalic("Для Дніпра (місто)"), 'https://t.me/volonteryDnepr'),
            fmt.text(fmt.hitalic("Для Львова"), 'https://t.me/volonterylviv'),
            fmt.text(fmt.hitalic("Для Богуслава"), 'https://t.me/boguslav_sos'),
            sep="\n\n"
        ),
        parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Житло"))
async def cmd_admin(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold("Не забувайте про основні інфо-чати віповідного міста! Бот надає здебільшого канали, у коментарях яких є чати.")),
            fmt.text(
                fmt.text(fmt.hitalic("Офіційне №1"), 'https://www.airbnb.com.ua/'),
                fmt.text("Невеличка інструкція з використання: Зверху справа є планетка, у якій ви зможете змінити мову (спочтаку, зазвичай, надається російська). Зміна на українську перетворить рублі в гривні."),
                sep='\n'
            ),
            fmt.text(fmt.hitalic("Офіційне №2"), 'https://www.booking.com'),
            fmt.text(fmt.hitalic("Офіційне №3"), 'https://prykhystok.in.ua/'),
            fmt.text(fmt.hitalic("Чернівці"), 'https://t.me/centralne'),
            fmt.text(fmt.hitalic("Івано-Франківськ"), 'https://t.me/orendaivanofrankivsk'),
            sep="\n\n"
        ),
        parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Адмін, є питаннячко!"))
async def cmd_admin(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["На головну"]
    keyboard.add(*buttons)

    await message.answer(
        fmt.text(
            fmt.text(fmt.hbold("Hello!")),
            fmt.text('@temyartemy'),
            sep="\n"
        ),
        parse_mode="HTML", reply_markup=keyboard
    )

@dp.message_handler(Text(equals="Транспорт"))
async def transport(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Чат водіїв", "Чат Укрзалізниці", "На головну"]
    keyboard.add(*buttons)

    await message.answer("Обирайте бажане:", reply_markup=keyboard)

@dp.message_handler(Text(equals="На головну"))
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Загальні джерела", "Міста", "Допомога",
               "Транспорт","Інструкція", "Адмін, є питаннячко!"]
    keyboard.add(*buttons)
    await message.answer("Сміливі завжди мають щастя...тож будь сміливим - обери щось:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Чат водіїв"))
async def first(message: types.Message):

    await message.answer(
        fmt.text(
            fmt.text("Чат водіїв: ", 'https://t.me/VoditeliUA'),
            fmt.text("Укравтодор: ", 'https://www.facebook.com/Ukravtodor.Gov.Ua'),
            fmt.text("Держ. служба з безпеки на транспорті (ДСБТ)", 'https://www.facebook.com/DSBT.UA'),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Чат Укрзалізниці"))
async def first(message: types.Message):

    await message.answer(
        fmt.text(
            fmt.text("Мініст. інфраструктури України: ", 'https://t.me/miUkraune'),
            fmt.text("Укрзалізниця: ", 'https://t.me/UkrzalInfo'),
            fmt.text("Держ. служюа з безпеки на транспорті (ДСБТ)", 'https://www.facebook.com/DSBT.UA'),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Загальні джерела"))
async def first(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Офіційні", "Неофіційні", "Іноземні", "На головну"]
    keyboard.add(*buttons)

    await message.answer("Обирайте:",  reply_markup=keyboard)

@dp.message_handler(Text(equals="Офіційні"))
async def official (message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("Офіс президента України"), 'https://www.facebook.com/president.gov.ua'),
            fmt.text(fmt.hitalic("Генштаб ЗСУ"), 'https://www.facebook.com/GeneralStaff.ua'),
            fmt.text(fmt.hitalic("Держслужба надзвичайних ситуацій"), 'https://www.facebook.com/MNS.GOV.UA'),
            fmt.text(fmt.hitalic("Сухопутні війська ЗСУ"), 'https://www.facebook.com/UkrainianLandForces'),
            fmt.text(fmt.hitalic("Тероборона"), 'https://www.facebook.com/TerritorialDefenseForces'),
            fmt.text(fmt.hitalic("Координація (раджу)"),
                     'https://ukraineisforever.notion.site/ukraineisforever/925902b5c48a4d7589fdeff2deba6233'),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Неофіційні"))
async def unofficial (message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("УНІАН"), 'https://t.me/uniannet'),
            fmt.text(fmt.hitalic("УП. Стрічка"), 'https://t.me/ukrpravda_news'),
            fmt.text(fmt.hitalic("Інформатор Україна"), 'https://t.me/informator_UKR'),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Іноземні"))
async def unofficial (message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("CNN (USA)"), 'https://edition.cnn.com/'),
            fmt.text(fmt.hitalic("DV (Germany)"), 'https://www.dw.com/en/top-stories/s-9097'),
            fmt.text(fmt.hitalic("BBC (England)"), 'https://www.bbc.com/'),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Міста"))
async def cmd_cities(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Київ", "Харків", "Дніпро",
               "Запоріжжя", "Одеса", "Миколаїв",
               "Маріуполь", "Вінниця", "Чернігів",
               "Херсон", "Івано-Франківськ", "Суми",
               "На головну"]
    keyboard.add(*buttons)
    await message.answer("Оберіть, будь-ласка, місто:", reply_markup=keyboard)

@dp.message_handler(Text(equals="Київ"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("Офіційне джерело:"), 'https://t.me/KyivCityOfficial'),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/kyivoperativ'),
                fmt.text("2) ", 'https://t.me/kievreal1'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Харків"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/synegubov'),
                fmt.text("2) ", 'https://t.me/suspilnekharkiv'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/truexanewsua'),
                fmt.text("2) ", 'https://t.me/kharkivlife1'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Дніпро"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilnednipro'),
                fmt.text("2) ", 'https://t.me/dnipropetrovskaODA'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/dp_informator_ua'),
                fmt.text("2) ", 'https://t.me/hyevuy_dnepr'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Запоріжжя"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("Офіційне джерело:"), 'https://t.me/suspilnezaporizhzhya'),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/joinchat/AAAAAE6e9ACI_WWct0SNHg'),
                fmt.text("2) ", 'https://t.me/etozp'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Одеса"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilneodesa'),
                fmt.text("2) ", 'https://t.me/odesacityofficial'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/xydessa'),
                fmt.text("2) ", 'https://t.me/our_odessa'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Миколаїв"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilnemykolaiv'),
                fmt.text("2) ", 'https://t.me/mykolaivskaODA'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/tpnik'),
                fmt.text("2) ", 'https://t.me/novostiniko1'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Маріуполь"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/mariupolrada'),
                fmt.text("2) ", 'https://t.me/polkazov'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/mariupolnow'),
                fmt.text("2) ", 'https://t.me/marik_news'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Вінниця"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(fmt.hitalic("Офіційне джерело:"), 'https://t.me/suspilne_vinnytsia'),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/vinnitsa_info'),
                fmt.text("2) ", 'https://t.me/vinnytsia_people'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Чернігів"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilnechernihiv'),
                fmt.text("2) ", 'https://t.me/chernigivskaODA'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/typical_chernihiv'),
                fmt.text("2) ", 'https://t.me/ChernihivOperative'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Херсон"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilnekherson'),
                fmt.text("2) ", 'hhttps://t.me/khersonskaODA'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/hueviyherson'),
                fmt.text("2) ", 'https://t.me/kherson_typical'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Івано-Франківськ"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/galkaifuanews'),
                fmt.text("2) ", 'https://t.me/onyshchuksvitlana'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/signal_if'),
                fmt.text("2) ", 'https://t.me/kurs_if'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler(Text(equals="Суми"))
async def first(message: types.Message):
    await message.answer(
        fmt.text(
            fmt.text(
                fmt.hitalic("Офіційні джерела:"),
                fmt.text("1) ", 'https://t.me/suspilnesumy'),
                fmt.text("2) ", 'https://t.me/Sumy_news_ODA'),
                sep="\n"
            ),
            fmt.text(
                fmt.hitalic("Неофіційні джерела:"),
                fmt.text("1) ", 'https://t.me/sumy_sumy'),
                fmt.text("2) ", 'https://t.me/sumygo'),
                sep="\n"
            ),
            sep="\n\n"
        ), parse_mode="HTML"
    )

@dp.message_handler()
async def any_text_message(message: types.Message):
    await message.answer("<b>Не ламай бота!</b>", parse_mode="HTML")

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)