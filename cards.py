# cards.py

# Список карт
cards = [
    # Старші Аркани
    {
        "name": "0. Шут (Дурак)",
        "keywords": "новий початок, наївність, свобода",
        "meaning": "Розпочинається новий шлях — без страху і з довірою. Це карта ризику та відкритості до нового.",
        "advice": " Соломон радить -Відпустіть страхи. Дозвольте собі нові починання, будьте уважні до небезпек, але не відмовляйтеся від пригод.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0001.jpg"
    },
    {
        "name": "I. Маг",
        "keywords": "воля, ресурсність, ініціатива",
        "meaning": "У вас є інструменти для впливу на ситуацію. Сила волі та концентрація допоможуть досягти мети.",
        "advice": " Соломон радить -Сконцентруйтесь на тому, що можете контролювати. Дійте цілеспрямовано.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0002.jpg"
    },
    {
        "name": "II. Верховна Жриця",
        "keywords": "інтуїція, таємниці, духовність",
        "meaning": "Цей день підштовхує прислухатися до внутрішнього голосу та довіряти своїм відчуттям.",
        "advice": " Соломон радить -Не поспішай з рішеннями — інтуїція підкаже правильний шлях.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0003.jpg"
    },
    {
        "name": "III. Імператриця",
        "keywords": "родючість, творчість, турбота",
        "meaning": "Період росту і плідності. Сприятливий час для творчих і побутових проектів.",
        "advice": " Соломон радить -Піклуйтесь про свої ідеї — давайте їм простір для розвитку.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0004.jpg"
    },
    {
        "name": "IV. Імператор",
        "keywords": "структура, контроль, авторитет",
        "meaning": "Потрібен порядок і дисципліна. Ваша рішучість зміцнить позицію.",
        "advice": " Соломон радить -Встановіть чіткі межі й плани — стабільність прийде через структуру.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0005.jpg"
    },
    {
        "name": "V. Ієрофант",
        "keywords": "традиції, навчання, духовні цінності",
        "meaning": "Пора слідувати перевіреним шляхам — освіта та наставництво принесуть користь.",
        "advice": " Соломон радить -Шукайте поради у досвідчених, не нехтуйте традиціями, якщо вони служать меті.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0006.jpg"
    },
    {
        "name": "VI. Закохані",
        "keywords": "вибір, відносини, гармонія",
        "meaning": "Важливий вибір у сфері серця або партнерства. Баланс цінностей відіграє роль.",
        "advice": " Соломон радить -Приймайте рішення, слухаючи і розум, і серце. Чесність важлива.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0007.jpg"
    },
    {
        "name": "VII. Колісниця",
        "keywords": "воля, рух, перемога",
        "meaning": "Сила волі і рішучість допомагають подолати перешкоди. Рухайтеся вперед з фокусом.",
        "advice": " Соломон радить -Намагайтеся зберігати рівновагу між імпульсом і контролем.",
        "image": "https://v-kosmose.com/wp-content/uploads/2020/10/8.jpg"
    },
    {
        "name": "VIII. Сила",
        "keywords": "терпіння, мужність, ніжність",
        "meaning": "Справжня сила — у м’якості та самоконтролі. Ви здатні приборкати внутрішні страхи.",
        "advice": " Соломон радить -Використовуйте співчуття і терпіння як інструменти для досягнення мети.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0009.jpg"
    },
    {
        "name": "IX. Відлюдник",
        "keywords": "усамітнення, пошук, внутрішня мудрість",
        "meaning": "Час на самопізнання і тишу. Відступ, щоб знайти відповіді всередині.",
        "advice": " Соломон радить -Приділіть час рефлексії; відповіді часто приходять у тиші.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0010.jpg"
    },
    {
        "name": "X. Колесо Фортуни",
        "keywords": "зміни, удача, цикли",
        "meaning": "Життєві кола обертаються — будьте готові до змін і використайте хвилю.",
        "advice": " Соломон радить -Приймайте зміни гнучко; використайте сприятливі моменти, коли вони є.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0011.jpg"
    },
    {
        "name": "XI. Справедливість",
        "keywords": "баланс, правда, відповідальність",
        "meaning": "Справедливі рішення та відповідальність відіграють ключову роль. Карта вироку і рівноваги.",
        "advice": " Соломон радить -Будьте чесні й об’єктивні — дії матимуть наслідки.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0012.jpg"
    },
    {
        "name": "XII. Повішений",
        "keywords": "пауза, переосмислення, жертва",
        "meaning": "Період затримки, коли потрібно змінити кут зору. Жертва може відкрити нові шляхи.",
        "advice": " Соломон радить -Відпустіть контроль і дозвольте собі побачити ситуацію під іншим кутом.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0013.jpg"
    },
    {
        "name": "XIII. Смерть",
        "keywords": "трансформація, кінець, оновлення",
        "meaning": "Необхідне завершення — старе відходить, щоб звільнити місце новому.",
        "advice": " Соломон радить -Приймайте зміни як очищення; дозвольте трансформації відбутися.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0014.jpg"
    },
    {
        "name": "XIV. Помірність",
        "keywords": "гармонія, баланс, поміркованість",
        "meaning": "Пошук балансу між крайнощами, інтеграція протилежностей.",
        "advice": " Соломон радить -Знайдіть золоту середину у справах і емоціях.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0015.jpg"
    },
    {
        "name": "XV. Диявол",
        "keywords": "обмеження, спокуса, прив’язаність",
        "meaning": "Карта попереджає про залежності або зв’язки, що стримують розвиток.",
        "advice": " Соломон радить -Визнайте ланцюги — перший крок до їх розірвання.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0016.jpg"
    },
    {
        "name": "XVI. Вежа",
        "keywords": "руйнування, шок, прозріння",
        "meaning": "Раптове руйнування старих конструкцій, після якого настає прояснення.",
        "advice": " Соломон радить -Не опирайтеся необхідним змінам; вони відкривають шлях до нового порядку.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0017.jpg"
    },
    {
        "name": "XVII. Зірка",
        "keywords": "надія, зцілення, натхнення",
        "meaning": "Період відновлення і віри; надихає на мрії та творчість.",
        "advice": " Соломон радить -Зберігайте надію і дозвольте собі вірити в майбутнє.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0018.jpg"
    },
    {
        "name": "XVIII. Місяць",
        "keywords": "ілюзії, підсвідомість, страхи",
        "meaning": "Неоднозначність і приховані мотиви можуть вводити в оману.",
        "advice": " Соломон радить -Перевіряйте факти, не довіряйте лише відчуттям; працюйте з підсвідомістю.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0019.jpg"
    },
    {
        "name": "XIX. Сонце",
        "keywords": "радість, успіх, ясність",
        "meaning": "Яскравий, позитивний період — ясність, відчуття радості і виконання.",
        "advice": " Соломон радить -Розквітаєте — приймайте подарунки життя і діліться своєю радістю.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0020.jpg"
    },
    {
        "name": "XX. Суд",
        "keywords": "відродження, рішення, пробудження",
        "meaning": "Оцінка минулого і шанс на нове початок; моральний чи духовний суд.",
        "advice": " Соломон радить -Прийміть уроки минулого і відпустіть провини; час на оновлення.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0021.jpg"
    },
    {
        "name": "XXI. Світ",
        "keywords": "завершення, цілісність, досягнення",
        "meaning": "Цикл завершується успішно — відчуття виконаного обов’язку і повноти.",
        "advice": " Соломон радить -Святкуйте досягнення і готуйтеся до нових горизонтів.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0022.jpg"
    },
    # Молодші Аркани: Жезли
    {
        "name": "Туз Жезлів",
        "keywords": "початок, натхнення, енергія",
        "meaning": "Нове творче натхнення і сила для старту проектів.",
        "advice": " Соломон радить -Використовуйте енергію для активних дій.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0023.jpg"
    },
    {
        "name": "Двійка Жезлів",
        "keywords": "планування, вибір, стратегія",
        "meaning": "Час обдумати наступні кроки і вибрати напрям.",
        "advice": " Соломон радить -Будьте обережні з вибором, думайте стратегічно.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0024.jpg"
    },
    {
        "name": "Трійка Жезлів",
        "keywords": "розвиток, перспектива, прогрес",
        "meaning": "Початок руху вперед, відкриття нових можливостей.",
        "advice": " Соломон радить -Будьте відкриті до нових ідей і пропозицій.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0025.jpg"
    },
    {
        "name": "Четвірка Жезлів",
        "keywords": "свято, стабільність, успіх",
        "meaning": "Період стабільності і приємних результатів.",
        "advice": " Соломон радить -Святкуйте досягнення і цінуйте підтримку.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0026.jpg"
    },
    {
        "name": "П’ятірка Жезлів",
        "keywords": "конфлікт, конкуренція, випробування",
        "meaning": "Виклики і суперечки, що ведуть до росту.",
        "advice": " Соломон радить -Навчіться конструктивно вирішувати конфлікти.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0027.jpg"
    },
    {
        "name": "Шістка Жезлів",
        "keywords": "перемога, визнання, успіх",
        "meaning": "Визнання ваших зусиль і досягнень.",
        "advice": " Соломон радить -Пишайтесь собою і рухайтесь далі.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0028.jpg"
    },
    {
        "name": "Сімка Жезлів",
        "keywords": "оборона, стійкість, боротьба",
        "meaning": "Потрібно відстояти свої позиції і не здаватися.",
        "advice": " Соломон радить -Вірте у свої сили і боріться за свої права.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0029.jpg"
    },
    {
        "name": "Вісімка Жезлів",
        "keywords": "швидкість, зміни, рух",
        "meaning": "Події розгортаються швидко, важливо встигнути за змінами.",
        "advice": " Соломон радить -Будьте готові до стрімких дій і нових рішень.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0030.jpg"
    },
    {
        "name": "Дев’ятка Жезлів",
        "keywords": "терпіння, підготовка, захист",
        "meaning": "Залишайтеся напоготові, попереду може бути випробування.",
        "advice": " Соломон радить -Не здавайтеся, тримайтеся і готуйтеся.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0031.jpg"
    },
    {
        "name": "Десятка Жезлів",
        "keywords": "тягар, відповідальність, навантаження",
        "meaning": "Велика відповідальність може обтяжувати, але близький успіх.",
        "advice": " Соломон радить -Не бійтеся просити допомоги і розділяти тягар.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0032.jpg"
    },
    {
        "name": "Паж Жезлів",
        "keywords": "початок, ентузіазм, новини",
        "meaning": "Нові ідеї і повідомлення, що надихають на дії.",
        "advice": " Соломон радить -Будьте відкриті до нового і вчіться.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0033.jpg"
    },
    {
        "name": "Рицар Жезлів",
        "keywords": "енергія, авантюра, рішучість",
        "meaning": "Рух до мети з ентузіазмом, але інколи поспішність.",
        "advice": " Соломон радить -Зберігайте баланс між імпульсом і обдуманістю.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0034.jpg"
    },
    {
        "name": "Королева Жезлів",
        "keywords": "пристрасність, впевненість, творчість",
        "meaning": "Сильна і натхненна жінка, лідер і творець.",
        "advice": " Соломон радить -Довіряйте своїй інтуїції і дійте рішуче.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0035.jpg"
    },
    {
        "name": "Король Жезлів",
        "keywords": "лідерство, вплив, відповідальність",
        "meaning": "Впевнений і харизматичний чоловік, який веде за собою.",
        "advice": " Соломон радить -Використовуйте силу для добра і розвитку.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0036.jpg"
    },
    # Кубки
    {
        "name": "Туз Кубків",
        "keywords": "нове почуття, любов, емоції",
        "meaning": "Початок гармонійних стосунків або емоційне оновлення.",
        "advice": " Соломон радить -Відкрийтеся для почуттів і діліться ними.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0037.jpg"
    },
    {
        "name": "Двійка Кубків",
        "keywords": "партнерство, злагода, союз",
        "meaning": "Гармонійні стосунки і взаєморозуміння.",
        "advice": " Соломон радить -Будуйте відносини на довірі і підтримці.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0038.jpg"
    },
    {
        "name": "Трійка Кубків",
        "keywords": "свято, дружба, радість",
        "meaning": "Веселі події і спільні радості.",
        "advice": " Соломон радить -Насолоджуйтеся моментами з близькими.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0039.jpg"
    },
    {
        "name": "Четвірка Кубків",
        "keywords": "роздуми, незадоволення, пауза",
        "meaning": "Період роздумів, можливо, апатії.",
        "advice": " Соломон радить -Прислухайтеся до себе і шукайте нові можливості.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0040.jpg"
    },
    {
        "name": "П’ятірка Кубків",
        "keywords": "втрата, сум, розчарування",
        "meaning": "Смуток через минуле, важливо відпустити.",
        "advice": " Соломон радить -Зверніть увагу на те, що ще є, а не на втрати.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0041.jpg"
    },
    {
        "name": "Шістка Кубків",
        "keywords": "спогади, ностальгія, дитинство",
        "meaning": "Пам’ять про приємні моменти і дитинство.",
        "advice": " Соломон радить -Використовуйте позитив минулого для натхнення.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0042.jpg"
    },
    {
        "name": "Сімка Кубків",
        "keywords": "ілюзії, вибір, мрії",
        "meaning": "Безліч варіантів, важливо не заблукати в мріях.",
        "advice": " Соломон радить -Фокусуйтеся на реальному і робіть вибір свідомо.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0043.jpg"
    },
    {
        "name": "Вісімка Кубків",
        "keywords": "відхід, пошук, зміни",
        "meaning": "Покинути щось старе заради нового шляху.",
        "advice": " Соломон радить -Не бійтеся залишати те, що не приносить радості.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0044.jpg"
    },
    {
        "name": "Дев’ятка Кубків",
        "keywords": "задоволення, щастя, успіх",
        "meaning": "Відчуття емоційного задоволення і реалізації.",
        "advice": " Соломон радить -Радійте тому, що маєте, і поділіться з іншими.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0045.jpg"
    },
    {
        "name": "Десятка Кубків",
        "keywords": "гармонія, сім’я, щастя",
        "meaning": "Повна гармонія в сімейних і стосунках.",
        "advice": " Соломон радить -Будуйте теплі стосунки і цінуйте їх.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0046.jpg"
    },
    {
        "name": "Паж Кубків",
        "keywords": "почуття, творчість, новини",
        "meaning": "Нові емоції і творчі ідеї.",
        "advice": " Соломон радить -Будьте відкриті до натхнення і експериментів.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0047.jpg"
    },
    {
        "name": "Рицар Кубків",
        "keywords": "романтика, рух, мрії",
        "meaning": "Рух в напрямку серця і мрій.",
        "advice": " Соломон радить -Довіряйте почуттям, але будьте реалістами.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0048.jpg"
    },
    {
        "name": "Королева Кубків",
        "keywords": "співчуття, інтуїція, підтримка",
        "meaning": "Сильна жінка, що підтримує і розуміє.",
        "advice": " Соломон радить -Слухайте серце і дбайте про інших.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0049.jpg"
    },
    {
        "name": "Король Кубків",
        "keywords": "гармонія, мудрість, контроль",
        "meaning": "Чоловік, який контролює емоції і діє мудро.",
        "advice": " Соломон радить -Баланс емоцій і розуму веде до успіху.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0050.jpg"
    },
    # Мечі
    {
        "name": "Туз Мечів",
        "keywords": "ясність, правда, рішення",
        "meaning": "Новий початок у думках, ясність і правда.",
        "advice": " Соломон радить -Будьте чесні з собою і приймайте рішення.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0051.jpg"
    },
    {
        "name": "Двійка Мечів",
        "keywords": "вибір, баланс, нерішучість",
        "meaning": "Внутрішній конфлікт і потреба у виборі.",
        "advice": " Соломон радить -Прислухайтеся до обох сторін, перш ніж обирати.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0052.jpg"
    },
    {
        "name": "Трійка Мечів",
        "keywords": "біль, розчарування, зрада",
        "meaning": "Серйозний емоційний біль і розчарування.",
        "advice": " Соломон радить -Дайте собі час для зцілення і прийняття.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0053.jpg"
    },
    {
        "name": "Четвірка Мечів",
        "keywords": "відпочинок, відновлення, пауза",
        "meaning": "Час для відпочинку і відновлення сил.",
        "advice": " Соломон радить -Прислухайтеся до потреб тіла і душі.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0054.jpg"
    },
    {
        "name": "П’ятірка Мечів",
        "keywords": "конфлікт, поразка, урок",
        "meaning": "Суперечки і можливі втрати, важливий урок.",
        "advice": " Соломон радить -Вчіться на помилках і уникайте зайвих конфліктів.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0055.jpg"
    },
    {
        "name": "Шістка Мечів",
        "keywords": "перехід, рух, зміни",
        "meaning": "Рух від проблем до спокою і нового початку.",
        "advice": " Соломон радить -Не бійтеся змін, вони ведуть до кращого.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0056.jpg"
    },
    {
        "name": "Сімка Мечів",
        "keywords": "обман, хитрість, уникнення",
        "meaning": "Можливий обман або уникнення відповідальності.",
        "advice": " Соломон радить -Будьте чесні і обережні у справах.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0057.jpg"
    },
    {
        "name": "Вісімка Мечів",
        "keywords": "обмеження, страх, пастка",
        "meaning": "Відчуття ув’язнення в ситуації або страхах.",
        "advice": " Соломон радить -Шукайте вихід і не бійтеся просити допомоги.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0058.jpg"
    },
    {
        "name": "Дев’ятка Мечів",
        "keywords": "тривога, страх, нічні кошмари",
        "meaning": "Період сильного стресу і внутрішніх страхів.",
        "advice": " Соломон радить -Працюйте з емоціями і шукайте підтримку.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0059.jpg"
    },
    {
        "name": "Десятка Мечів",
        "keywords": "крах, кінець, звільнення",
        "meaning": "Кінець складного періоду, можливість нового початку.",
        "advice": " Соломон радить -Прийміть кінець і рухайтесь вперед.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0060.jpg"
    },
    {
        "name": "Паж Мечів",
        "keywords": "спостереження, навчання, новини",
        "meaning": "Нові ідеї і пильність у справах.",
        "advice": " Соломон радить -Будьте уважні і відкриті до знань.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0061.jpg"
    },
    {
        "name": "Рицар Мечів",
        "keywords": "рішучість, швидкість, ідеали",
        "meaning": "Швидкі дії і тверда віра в ідеали.",
        "advice": " Соломон радить -Дійте швидко, але думайте стратегічно.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0062.jpg"
    },
    {
        "name": "Королева Мечів",
        "keywords": "розум, незалежність, чесність",
        "meaning": "Жінка з гострим розумом і сильним характером.",
        "advice": " Соломон радить -Будьте чесні і дотримуйтеся принципів.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0063.jpg"
    },
    {
        "name": "Король Мечів",
        "keywords": "інтелект, авторитет, справедливість",
        "meaning": "Чоловік, що керується розумом і справедливістю.",
        "advice": " Соломон радить -Приймайте рішення об’єктивно і без емоцій.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0064.jpg"
    },
    # Пентаклі
    {
        "name": "Туз Пентаклів",
        "keywords": "нові можливості, матеріальний початок",
        "meaning": "Початок фінансового або матеріального успіху.",
        "advice": " Соломон радить -Будьте відкриті до нових пропозицій і інвестицій.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0065.jpg"
    },
    {
        "name": "Двійка Пентаклів",
        "keywords": "баланс, адаптація, гнучкість",
        "meaning": "Вміння балансувати між обов’язками і ресурсами.",
        "advice": " Соломон радить -Не забувайте про гнучкість у справах.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0066.jpg"
    },
    {
        "name": "Трійка Пентаклів",
        "keywords": "співпраця, майстерність, розвиток",
        "meaning": "Успіх через командну роботу і вміння.",
        "advice": " Соломон радить -Працюйте над покращенням навичок і спілкуванням.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0067.jpg"
    },
    {
        "name": "Четвірка Пентаклів",
        "keywords": "стабільність, накопичення, контроль",
        "meaning": "Прагнення зберегти досягнуте і контроль над ресурсами.",
        "advice": " Соломон радить -Не будьте надто жорсткими, відкрийтеся до змін.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0068.jpg"
    },
    {
        "name": "П’ятірка Пентаклів",
        "keywords": "втрати, труднощі, підтримка",
        "meaning": "Фінансові чи матеріальні труднощі, потреба підтримки.",
        "advice": " Соломон радить -Не бійтеся просити допомогу у важкий час.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0069.jpg"
    },
    {
        "name": "Шістка Пентаклів",
        "keywords": "щедрість, допомога, рівновага",
        "meaning": "Баланс у віддачі та отриманні допомоги.",
        "advice": " Соломон радить -Будьте відкриті до прийняття і дарування.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0070.jpg"
    },
    {
        "name": "Сімка Пентаклів",
        "keywords": "терпіння, оцінка, праця",
        "meaning": "Період очікування плодів вашої праці.",
        "advice": " Соломон радить -Терпіння і віра допоможуть досягти результату.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0071.jpg"
    },
    {
        "name": "Вісімка Пентаклів",
        "keywords": "навчання, майстерність, практика",
        "meaning": "Активне вдосконалення навичок і знань.",
        "advice": " Соломон радить -Зосередьтеся на розвитку і вдосконаленні.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0072.jpg"
    },
    {
        "name": "Дев’ятка Пентаклів",
        "keywords": "самодостатність, достаток, комфорт",
        "meaning": "Незалежність і задоволення матеріальним життям.",
        "advice": " Соломон радить -Цінуйте свої досягнення і радійте моменту.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0073.jpg"
    },
    {
        "name": "Десятка Пентаклів",
        "keywords": "благополуччя, спадщина, сім’я",
        "meaning": "Стабільність, процвітання і підтримка сім’ї.",
        "advice": " Соломон радить -Будуйте міцні основи для майбутніх поколінь.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0074.jpg"
    },
    {
        "name": "Паж Пентаклів",
        "keywords": "новини, навчання, можливості",
        "meaning": "Нові початки у сфері матеріальних справ.",
        "advice": " Соломон радить -Будьте відкриті до навчання і нових ідей.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0075.jpg"
    },
    {
        "name": "Рицар Пентаклів",
        "keywords": "надійність, наполегливість, обережність",
        "meaning": "Прагматичний рух вперед, крок за кроком.",
        "advice": " Соломон радить -Дотримуйтеся плану і будьте наполегливими.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0076.jpg"
    },
    {
        "name": "Королева Пентаклів",
        "keywords": "практичність, турбота, стабільність",
        "meaning": "Жінка, яка піклується про дім і матеріальний комфорт.",
        "advice": " Соломон радить -Дбайте про себе і створюйте затишок навколо.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0077.jpg"
    },
    {
        "name": "Король Пентаклів",
        "keywords": "успіх, багатство, відповідальність",
        "meaning": "Чоловік, який досягає матеріального успіху і стабільності.",
        "advice": " Соломон радить -Використовуйте свої ресурси мудро і відповідально.",
        "image": "https://giggle.com.ua/image/catalog/blog/znachennyatus/Sun-Tarrot_Full%20card_RUS_03.06.23_page-0078.jpg"
    }
]
