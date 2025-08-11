import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Завантажуємо змінні оточення
load_dotenv()

token = os.getenv("BOT_TOKEN")

# Список карт
cards = [
    # Старші Аркани
    {
        "name": "0. Шут (Дурак)",
        "keywords": "новий початок, наївність, свобода",
        "meaning": "Розпочинається новий шлях — без страху і з довірою. Це карта ризику та відкритості до нового.",
        "advice": "Відпустіть страхи. Дозвольте собі нові починання, будьте уважні до небезпек, але не відмовляйтеся від пригод.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/1-1.jpg"
    },
    {
        "name": "I. Маг",
        "keywords": "воля, ресурсність, ініціатива",
        "meaning": "У вас є інструменти для впливу на ситуацію. Сила волі та концентрація допоможуть досягти мети.",
        "advice": "Сконцентруйтесь на тому, що можете контролювати. Дійте цілеспрямовано.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/2-1.jpg"
    },
    {
        "name": "II. Верховна Жриця",
        "keywords": "інтуїція, таємниці, духовність",
        "meaning": "Цей день підштовхує прислухатися до внутрішнього голосу та довіряти своїм відчуттям.",
        "advice": "Не поспішай з рішеннями — інтуїція підкаже правильний шлях.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/3-1.jpg"
    },
    {
        "name": "III. Імператриця",
        "keywords": "родючість, творчість, турбота",
        "meaning": "Період росту і плідності. Сприятливий час для творчих і побутових проектів.",
        "advice": "Піклуйтесь про свої ідеї — давайте їм простір для розвитку.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/4-1.jpg"
    },
    {
        "name": "IV. Імператор",
        "keywords": "структура, контроль, авторитет",
        "meaning": "Потрібен порядок і дисципліна. Ваша рішучість зміцнить позицію.",
        "advice": "Встановіть чіткі межі й плани — стабільність прийде через структуру.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/5.jpg"
    },
    {
        "name": "V. Ієрофант",
        "keywords": "традиції, навчання, духовні цінності",
        "meaning": "Пора слідувати перевіреним шляхам — освіта та наставництво принесуть користь.",
        "advice": "Шукайте поради у досвідчених, не нехтуйте традиціями, якщо вони служать меті.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/6.jpg"
    },
    {
        "name": "VI. Закохані",
        "keywords": "вибір, відносини, гармонія",
        "meaning": "Важливий вибір у сфері серця або партнерства. Баланс цінностей відіграє роль.",
        "advice": "Приймайте рішення, слухаючи і розум, і серце. Чесність важлива.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/7.jpg"
    },
    {
        "name": "VII. Колісниця",
        "keywords": "воля, рух, перемога",
        "meaning": "Сила волі і рішучість допомагають подолати перешкоди. Рухайтеся вперед з фокусом.",
        "advice": "Намагайтеся зберігати рівновагу між імпульсом і контролем.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/8.jpg"
    },
    {
        "name": "VIII. Сила",
        "keywords": "терпіння, мужність, ніжність",
        "meaning": "Справжня сила — у м’якості та самоконтролі. Ви здатні приборкати внутрішні страхи.",
        "advice": "Використовуйте співчуття і терпіння як інструменти для досягнення мети.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/9.jpg"
    },
    {
        "name": "IX. Відлюдник",
        "keywords": "усамітнення, пошук, внутрішня мудрість",
        "meaning": "Час на самопізнання і тишу. Відступ, щоб знайти відповіді всередині.",
        "advice": "Приділіть час рефлексії; відповіді часто приходять у тиші.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/10.jpg"
    },
    {
        "name": "X. Колесо Фортуни",
        "keywords": "зміни, удача, цикли",
        "meaning": "Життєві кола обертаються — будьте готові до змін і використайте хвилю.",
        "advice": "Приймайте зміни гнучко; використайте сприятливі моменти, коли вони є.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/11.jpg"
    },
    {
        "name": "XI. Справедливість",
        "keywords": "баланс, правда, відповідальність",
        "meaning": "Справедливі рішення та відповідальність відіграють ключову роль. Карта вироку і рівноваги.",
        "advice": "Будьте чесні й об’єктивні — дії матимуть наслідки.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/12.jpg"
    },
    {
        "name": "XII. Повішений",
        "keywords": "пауза, переосмислення, жертва",
        "meaning": "Період затримки, коли потрібно змінити кут зору. Жертва може відкрити нові шляхи.",
        "advice": "Відпустіть контроль і дозвольте собі побачити ситуацію під іншим кутом.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/13.jpg"
    },
    {
        "name": "XIII. Смерть",
        "keywords": "трансформація, кінець, оновлення",
        "meaning": "Необхідне завершення — старе відходить, щоб звільнити місце новому.",
        "advice": "Приймайте зміни як очищення; дозвольте трансформації відбутися.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/smert.jpg"
    },
    {
        "name": "XIV. Помірність",
        "keywords": "гармонія, баланс, поміркованість",
        "meaning": "Пошук балансу між крайнощами, інтеграція протилежностей.",
        "advice": "Знайдіть золоту середину у справах і емоціях.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/umerennost.jpg"
    },
    {
        "name": "XV. Диявол",
        "keywords": "обмеження, спокуса, прив’язаність",
        "meaning": "Карта попереджає про залежності або зв’язки, що стримують розвиток.",
        "advice": "Визнайте ланцюги — перший крок до їх розірвання.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/diyavol.jpg"
    },
    {
        "name": "XVI. Вежа",
        "keywords": "руйнування, шок, прозріння",
        "meaning": "Раптове руйнування старих конструкцій, після якого настає прояснення.",
        "advice": "Не опирайтеся необхідним змінам; вони відкривають шлях до нового порядку.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/padayushaya-bashnya.jpg"
    },
    {
        "name": "XVII. Зірка",
        "keywords": "надія, зцілення, натхнення",
        "meaning": "Період відновлення і віри; надихає на мрії та творчість.",
        "advice": "Зберігайте надію і дозвольте собі вірити в майбутнє.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/zvezda.jpg"
    },
    {
        "name": "XVIII. Місяць",
        "keywords": "ілюзії, підсвідомість, страхи",
        "meaning": "Неоднозначність і приховані мотиви можуть вводити в оману.",
        "advice": "Перевіряйте факти, не довіряйте лише відчуттям; працюйте з підсвідомістю.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/luna.jpg"
    },
    {
        "name": "XIX. Сонце",
        "keywords": "радість, успіх, ясність",
        "meaning": "Яскравий, позитивний період — ясність, відчуття радості і виконання.",
        "advice": "Розквітаєте — приймайте подарунки життя і діліться своєю радістю.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/solnce.jpg"
    },
    {
        "name": "XX. Суд",
        "keywords": "відродження, рішення, пробудження",
        "meaning": "Оцінка минулого і шанс на нове початок; моральний чи духовний суд.",
        "advice": "Прийміть уроки минулого і відпустіть провини; час на оновлення.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/strashnyi-sud.jpg"
    },
    {
        "name": "XXI. Світ",
        "keywords": "завершення, цілісність, досягнення",
        "meaning": "Цикл завершується успішно — відчуття виконаного обов’язку і повноти.",
        "advice": "Святкуйте досягнення і готуйтеся до нових горизонтів.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/mir.jpg"
    },
    # Молодші Аркани: Жезли
    {
        "name": "Туз Жезлів",
        "keywords": "початок, натхнення, енергія",
        "meaning": "Нове творче натхнення і сила для старту проектів.",
        "advice": "Використовуйте енергію для активних дій.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/tuz-zhezlov.jpg"
    },
    {
        "name": "Двійка Жезлів",
        "keywords": "планування, вибір, стратегія",
        "meaning": "Час обдумати наступні кроки і вибрати напрям.",
        "advice": "Будьте обережні з вибором, думайте стратегічно.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/1-2.jpg"
    },
    {
        "name": "Трійка Жезлів",
        "keywords": "розвиток, перспектива, прогрес",
        "meaning": "Початок руху вперед, відкриття нових можливостей.",
        "advice": "Будьте відкриті до нових ідей і пропозицій.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/2-2.jpg"
    },
    {
        "name": "Четвірка Жезлів",
        "keywords": "свято, стабільність, успіх",
        "meaning": "Період стабільності і приємних результатів.",
        "advice": "Святкуйте досягнення і цінуйте підтримку.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/3-2.jpg"
    },
    {
        "name": "П’ятірка Жезлів",
        "keywords": "конфлікт, конкуренція, випробування",
        "meaning": "Виклики і суперечки, що ведуть до росту.",
        "advice": "Навчіться конструктивно вирішувати конфлікти.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/4-2.jpg"
    },
    {
        "name": "Шістка Жезлів",
        "keywords": "перемога, визнання, успіх",
        "meaning": "Визнання ваших зусиль і досягнень.",
        "advice": "Пишайтесь собою і рухайтесь далі.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/5-1.jpg"
    },
    {
        "name": "Сімка Жезлів",
        "keywords": "оборона, стійкість, боротьба",
        "meaning": "Потрібно відстояти свої позиції і не здаватися.",
        "advice": "Вірте у свої сили і боріться за свої права.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/6-1.jpg"
    },
    {
        "name": "Вісімка Жезлів",
        "keywords": "швидкість, зміни, рух",
        "meaning": "Події розгортаються швидко, важливо встигнути за змінами.",
        "advice": "Будьте готові до стрімких дій і нових рішень.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/7-1.jpg"
    },
    {
        "name": "Дев’ятка Жезлів",
        "keywords": "терпіння, підготовка, захист",
        "meaning": "Залишайтеся напоготові, попереду може бути випробування.",
        "advice": "Не здавайтеся, тримайтеся і готуйтеся.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/8-1.jpg"
    },
    {
        "name": "Десятка Жезлів",
        "keywords": "тягар, відповідальність, навантаження",
        "meaning": "Велика відповідальність може обтяжувати, але близький успіх.",
        "advice": "Не бійтеся просити допомоги і розділяти тягар.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/9-1.jpg"
    },
    {
        "name": "Паж Жезлів",
        "keywords": "початок, ентузіазм, новини",
        "meaning": "Нові ідеї і повідомлення, що надихають на дії.",
        "advice": "Будьте відкриті до нового і вчіться.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/10-1.jpg"
    },
    {
        "name": "Рицар Жезлів",
        "keywords": "енергія, авантюра, рішучість",
        "meaning": "Рух до мети з ентузіазмом, але інколи поспішність.",
        "advice": "Зберігайте баланс між імпульсом і обдуманістю.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/11-1.jpg"
    },
    {
        "name": "Королева Жезлів",
        "keywords": "пристрасність, впевненість, творчість",
        "meaning": "Сильна і натхненна жінка, лідер і творець.",
        "advice": "Довіряйте своїй інтуїції і дійте рішуче.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/12-1.jpg"
    },
    {
        "name": "Король Жезлів",
        "keywords": "лідерство, вплив, відповідальність",
        "meaning": "Впевнений і харизматичний чоловік, який веде за собою.",
        "advice": "Використовуйте силу для добра і розвитку.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/13-1.jpg"
    },
    # Кубки
    {
        "name": "Туз Кубків",
        "keywords": "нове почуття, любов, емоції",
        "meaning": "Початок гармонійних стосунків або емоційне оновлення.",
        "advice": "Відкрийтеся для почуттів і діліться ними.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/tuz-kubkov.jpg"
    },
    {
        "name": "Двійка Кубків",
        "keywords": "партнерство, злагода, союз",
        "meaning": "Гармонійні стосунки і взаєморозуміння.",
        "advice": "Будуйте відносини на довірі і підтримці.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/dvoika-kubkov.jpg"
    },
    {
        "name": "Трійка Кубків",
        "keywords": "свято, дружба, радість",
        "meaning": "Веселі події і спільні радості.",
        "advice": "Насолоджуйтеся моментами з близькими.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/troika-kubkov.jpg"
    },
    {
        "name": "Четвірка Кубків",
        "keywords": "роздуми, незадоволення, пауза",
        "meaning": "Період роздумів, можливо, апатії.",
        "advice": "Прислухайтеся до себе і шукайте нові можливості.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/chetverka-kubkov.jpg"
    },
    {
        "name": "П’ятірка Кубків",
        "keywords": "втрата, сум, розчарування",
        "meaning": "Смуток через минуле, важливо відпустити.",
        "advice": "Зверніть увагу на те, що ще є, а не на втрати.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/1-3.jpg"
    },
    {
        "name": "Шістка Кубків",
        "keywords": "спогади, ностальгія, дитинство",
        "meaning": "Пам’ять про приємні моменти і дитинство.",
        "advice": "Використовуйте позитив минулого для натхнення.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/2-3.jpg"
    },
    {
        "name": "Сімка Кубків",
        "keywords": "ілюзії, вибір, мрії",
        "meaning": "Безліч варіантів, важливо не заблукати в мріях.",
        "advice": "Фокусуйтеся на реальному і робіть вибір свідомо.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/3-3.jpg"
    },
    {
        "name": "Вісімка Кубків",
        "keywords": "відхід, пошук, зміни",
        "meaning": "Покинути щось старе заради нового шляху.",
        "advice": "Не бійтеся залишати те, що не приносить радості.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/4-3.jpg"
    },
    {
        "name": "Дев’ятка Кубків",
        "keywords": "задоволення, щастя, успіх",
        "meaning": "Відчуття емоційного задоволення і реалізації.",
        "advice": "Радійте тому, що маєте, і поділіться з іншими.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/5-2.jpg"
    },
    {
        "name": "Десятка Кубків",
        "keywords": "гармонія, сім’я, щастя",
        "meaning": "Повна гармонія в сімейних і стосунках.",
        "advice": "Будуйте теплі стосунки і цінуйте їх.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/6-2.jpg"
    },
    {
        "name": "Паж Кубків",
        "keywords": "почуття, творчість, новини",
        "meaning": "Нові емоції і творчі ідеї.",
        "advice": "Будьте відкриті до натхнення і експериментів.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/7-2.jpg"
    },
    {
        "name": "Рицар Кубків",
        "keywords": "романтика, рух, мрії",
        "meaning": "Рух в напрямку серця і мрій.",
        "advice": "Довіряйте почуттям, але будьте реалістами.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/8-2.jpg"
    },
    {
        "name": "Королева Кубків",
        "keywords": "співчуття, інтуїція, підтримка",
        "meaning": "Сильна жінка, що підтримує і розуміє.",
        "advice": "Слухайте серце і дбайте про інших.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/9-2.jpg"
    },
    {
        "name": "Король Кубків",
        "keywords": "гармонія, мудрість, контроль",
        "meaning": "Чоловік, який контролює емоції і діє мудро.",
        "advice": "Баланс емоцій і розуму веде до успіху.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/10-2.jpg"
    },
    # Мечі
    {
        "name": "Туз Мечів",
        "keywords": "ясність, правда, рішення",
        "meaning": "Новий початок у думках, ясність і правда.",
        "advice": "Будьте чесні з собою і приймайте рішення.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/tuz-mechei.jpg"
    },
    {
        "name": "Двійка Мечів",
        "keywords": "вибір, баланс, нерішучість",
        "meaning": "Внутрішній конфлікт і потреба у виборі.",
        "advice": "Прислухайтеся до обох сторін, перш ніж обирати.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/dvoika-mechei.jpg"
    },
    {
        "name": "Трійка Мечів",
        "keywords": "біль, розчарування, зрада",
        "meaning": "Серйозний емоційний біль і розчарування.",
        "advice": "Дайте собі час для зцілення і прийняття.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/troika-mechei.jpg"
    },
    {
        "name": "Четвірка Мечів",
        "keywords": "відпочинок, відновлення, пауза",
        "meaning": "Час для відпочинку і відновлення сил.",
        "advice": "Прислухайтеся до потреб тіла і душі.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/chetverka-mechei.jpg"
    },
    {
        "name": "П’ятірка Мечів",
        "keywords": "конфлікт, поразка, урок",
        "meaning": "Суперечки і можливі втрати, важливий урок.",
        "advice": "Вчіться на помилках і уникайте зайвих конфліктів.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/pyaterka-mechei.jpg"
    },
    {
        "name": "Шістка Мечів",
        "keywords": "перехід, рух, зміни",
        "meaning": "Рух від проблем до спокою і нового початку.",
        "advice": "Не бійтеся змін, вони ведуть до кращого.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/shesterka-mechei.jpg"
    },
    {
        "name": "Сімка Мечів",
        "keywords": "обман, хитрість, уникнення",
        "meaning": "Можливий обман або уникнення відповідальності.",
        "advice": "Будьте чесні і обережні у справах.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/semerka-mechei.jpg"
    },
    {
        "name": "Вісімка Мечів",
        "keywords": "обмеження, страх, пастка",
        "meaning": "Відчуття ув’язнення в ситуації або страхах.",
        "advice": "Шукайте вихід і не бійтеся просити допомоги.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/vosmerka-mechei.jpg"
    },
    {
        "name": "Дев’ятка Мечів",
        "keywords": "тривога, страх, нічні кошмари",
        "meaning": "Період сильного стресу і внутрішніх страхів.",
        "advice": "Працюйте з емоціями і шукайте підтримку.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/devyatka-mechei.jpg"
    },
    {
        "name": "Десятка Мечів",
        "keywords": "крах, кінець, звільнення",
        "meaning": "Кінець складного періоду, можливість нового початку.",
        "advice": "Прийміть кінець і рухайтесь вперед.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/desyatka-mechei.jpg"
    },
    {
        "name": "Паж Мечів",
        "keywords": "спостереження, навчання, новини",
        "meaning": "Нові ідеї і пильність у справах.",
        "advice": "Будьте уважні і відкриті до знань.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/pazh-mechei.jpg"
    },
    {
        "name": "Рицар Мечів",
        "keywords": "рішучість, швидкість, ідеали",
        "meaning": "Швидкі дії і тверда віра в ідеали.",
        "advice": "Дійте швидко, але думайте стратегічно.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/rycar-mechei.jpg"
    },
    {
        "name": "Королева Мечів",
        "keywords": "розум, незалежність, чесність",
        "meaning": "Жінка з гострим розумом і сильним характером.",
        "advice": "Будьте чесні і дотримуйтеся принципів.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/koroleva-mechei.jpg"
    },
    {
        "name": "Король Мечів",
        "keywords": "інтелект, авторитет, справедливість",
        "meaning": "Чоловік, що керується розумом і справедливістю.",
        "advice": "Приймайте рішення об’єктивно і без емоцій.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/korol-mechei.jpg"
    },
    # Пентаклі
    {
        "name": "Туз Пентаклів",
        "keywords": "нові можливості, матеріальний початок",
        "meaning": "Початок фінансового або матеріального успіху.",
        "advice": "Будьте відкриті до нових пропозицій і інвестицій.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/11-2.jpg"
    },
    {
        "name": "Двійка Пентаклів",
        "keywords": "баланс, адаптація, гнучкість",
        "meaning": "Вміння балансувати між обов’язками і ресурсами.",
        "advice": "Не забувайте про гнучкість у справах.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/12-2.jpg"
    },
    {
        "name": "Трійка Пентаклів",
        "keywords": "співпраця, майстерність, розвиток",
        "meaning": "Успіх через командну роботу і вміння.",
        "advice": "Працюйте над покращенням навичок і спілкуванням.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/troika-pentaklei.jpg"
    },
    {
        "name": "Четвірка Пентаклів",
        "keywords": "стабільність, накопичення, контроль",
        "meaning": "Прагнення зберегти досягнуте і контроль над ресурсами.",
        "advice": "Не будьте надто жорсткими, відкрийтеся до змін.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/chetverka-pentaklei.jpg"
    },
    {
        "name": "П’ятірка Пентаклів",
        "keywords": "втрати, труднощі, підтримка",
        "meaning": "Фінансові чи матеріальні труднощі, потреба підтримки.",
        "advice": "Не бійтеся просити допомогу у важкий час.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/pyaterka-pentaklei.jpg"
    },
    {
        "name": "Шістка Пентаклів",
        "keywords": "щедрість, допомога, рівновага",
        "meaning": "Баланс у віддачі та отриманні допомоги.",
        "advice": "Будьте відкриті до прийняття і дарування.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/shesterka-pentaklei.jpg"
    },
    {
        "name": "Сімка Пентаклів",
        "keywords": "терпіння, оцінка, праця",
        "meaning": "Період очікування плодів вашої праці.",
        "advice": "Терпіння і віра допоможуть досягти результату.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/semerka-pentaklei.jpg"
    },
    {
        "name": "Вісімка Пентаклів",
        "keywords": "навчання, майстерність, практика",
        "meaning": "Активне вдосконалення навичок і знань.",
        "advice": "Зосередьтеся на розвитку і вдосконаленні.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/vosmerka-pentaklei.jpg"
    },
    {
        "name": "Дев’ятка Пентаклів",
        "keywords": "самодостатність, достаток, комфорт",
        "meaning": "Незалежність і задоволення матеріальним життям.",
        "advice": "Цінуйте свої досягнення і радійте моменту.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/devyatka-pentaklei.jpg"
    },
    {
        "name": "Десятка Пентаклів",
        "keywords": "благополуччя, спадщина, сім’я",
        "meaning": "Стабільність, процвітання і підтримка сім’ї.",
        "advice": "Будуйте міцні основи для майбутніх поколінь.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/desyatka-pentaklei.jpg"
    },
    {
        "name": "Паж Пентаклів",
        "keywords": "новини, навчання, можливості",
        "meaning": "Нові початки у сфері матеріальних справ.",
        "advice": "Будьте відкриті до навчання і нових ідей.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/pazh-pentaklei.jpg"
    },
    {
        "name": "Рицар Пентаклів",
        "keywords": "надійність, наполегливість, обережність",
        "meaning": "Прагматичний рух вперед, крок за кроком.",
        "advice": "Дотримуйтеся плану і будьте наполегливими.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/rycar-pentaklei.jpg"
    },
    {
        "name": "Королева Пентаклів",
        "keywords": "практичність, турбота, стабільність",
        "meaning": "Жінка, яка піклується про дім і матеріальний комфорт.",
        "advice": "Дбайте про себе і створюйте затишок навколо.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/koroleva-pentaklei.jpg"
    },
    {
        "name": "Король Пентаклів",
        "keywords": "успіх, багатство, відповідальність",
        "meaning": "Чоловік, який досягає матеріального успіху і стабільності.",
        "advice": "Використовуйте свої ресурси мудро і відповідально.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/korol-pentaklei.jpg"
    }
]

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Натисни /card, щоб отримати випадкову карту 📜"
    )

# Команда /card
async def card(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = random.choice(cards)
    text = f"**{card['name']}**\n\n{card['advice']}"
    await update.message.reply_photo(photo=card['image'], caption=text, parse_mode="Markdown")

def main():
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("card", card))

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()
