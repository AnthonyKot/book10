import os

tsv_path = "/home/diablo/book10/corpus/by-2024.tsv"

header = [
    "author", "title", "author_born", "author_died", "origin",
    "genre", "subject_era", "exam_status", "memorize", "grade",
    "source", "doc_year", "retrieved", "note"
]

rows = [
    # Belarusian Literature Track (Беларуская літаратура - 9 клас)
    [
        "Народная творчасць (Folk Literature)",
        "Балада «Дамавікова ўдзячнасць» (Folk Ballad \"The Domovoy's Gratitude\")",
        "traditional", "traditional", "domestic",
        "poem", "none/folklore", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Prescribed folklore ballad in Grade 9 Belarusian Literature"
    ],
    [
        "Невядомы автор (Unknown author)",
        "«Жыціе Еўфрасінні Полацкай» (\"Life of Saint Euphrosyne of Polotsk\")",
        "12th c.", "12th c.", "domestic",
        "essay", "Kyivan-Rus", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Foundational 12th-century hagiographic work of Belarusian literature"
    ],
    [
        "Кірыл Тураўскі (Kirill of Turov)",
        "«Словы», «Казанні», «Павучанні» (\"Sermons, Orations, and Instructions\")",
        "~1130", "~1182", "domestic",
        "essay", "Kyivan-Rus", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Old Belarusian sermon literature of the 12th century"
    ],
    [
        "Летапісны пераказ (Chronicle Narrative)",
        "«Аповесць пра Усяслава Полацкага» (\"Tale of Vseslav of Polotsk\")",
        "12th c.", "12th c.", "domestic",
        "epic", "Kyivan-Rus", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Chronicle story of Prince Vseslav the Sorcerer of Polotsk"
    ],
    [
        "Беларуска-літоўскі летапіс (Belarusian-Lithuanian Chronicle)",
        "«Летапіс вялікіх князёў літоўскіх» (урывак «Пахвала Вітаўту») (\"Chronicle of the Grand Dukes of Lithuania\" (excerpt \"Praise of Vytautas\"))",
        "15th c.", "15th c.", "domestic",
        "essay", "Grand-Duchy-Lithuania", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Grand Duchy of Lithuania panegyric chronicle excerpt"
    ],
    [
        "Францыск Скарына (Francysk Skaryna)",
        "Прадмовы да кніг Бібліі (у тым ліку «З прадмовы да Кнігі Юдзіф») (Prefaces to Bible Books (including \"From the Preface to Judith\"))",
        "~1490", "~1551", "domestic",
        "essay", "Renaissance-Enlightenment", "mandatory", "excerpt", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Recitation of excerpt from Judith preface mandated in Grade 9 memorization list"
    ],
    [
        "Сымон Будны (Symon Budny)",
        "«Прадмова да Катэхізіса» (\"Preface to the Catechism\")",
        "~1530", "1593", "domestic",
        "essay", "Renaissance-Enlightenment", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Reformation printing and patriotic preface in Old Belarusian"
    ],
    [
        "Васіль Цяпінскі (Vasil Tsiapinski)",
        "«Прадмова да Евангелля» (\"Preface to the Gospel\")",
        "~1540", "~1604", "domestic",
        "essay", "Renaissance-Enlightenment", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Reformation polemical preface defending Belarusian language"
    ],
    [
        "Мікола Гусоўскі (Mikola Husouski)",
        "Паэма «Песня пра зубра» (\"Song of the Bison\")",
        "~1470", "~1533", "domestic",
        "poem", "Grand-Duchy-Lithuania", "mandatory", "excerpt", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Renaissance Latin poem on Belarusian nature and Grand Duchy history; excerpt mandated for memorization"
    ],
    [
        "Каятан Марашэўскі (Kajetan Maraszewski)",
        "«Камедыя» (\"Comedy\")",
        "~1750", "~1811", "domestic",
        "play", "Enlightenment", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "18th-century school drama comedy in Belarusian/Polish"
    ],
    [
        "Невядомы автор (Unknown author)",
        "Паэма «Энеіда навыварат» (\"Eneida Navavyvarat / Trojan Parody\")",
        "~1790", "~1840", "domestic",
        "poem", "Enlightenment", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Anonymous burlesque epic poem parodying Virgil's Aeneid"
    ],
    [
        "Ян Чачот (Jan Czeczot)",
        "Вершы («Покуль сонца ўзыдзе...», «Да мілых мужычкоў», «На прыезд Адама Міцкевіча») (Poems (\"Until the Sun Rises...\", \"To Dear Peasants\"))",
        "1796", "1847", "domestic",
        "poem-cycle", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Early 19th-century Philomath romantic poetry"
    ],
    [
        "Адам Міцкевіч (Adam Mickiewicz)",
        "Паэма «Гражына», эпас «Пан Тадэвуш» (урыўкі) (Poems \"Grażyna\", \"Pan Tadeusz\" (excerpts))",
        "1798", "1855", "domestic",
        "poem-cycle", "Grand-Duchy-Lithuania", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Polish-language epic poems of Belarusian heritage; read in Belarusian translation"
    ],
    [
        "Ян Баршчэўскі (Jan Barszczewski)",
        "Зборнік «Шляхціц Завальня, або Беларусь у фантастычных апавяданнях» (\"Nobleman Zavalnya, or Belarus in Fantastic Stories\")",
        "~1794", "1851", "domestic",
        "short-story", "none/folklore", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Romantic collection of Belarusian gothic tales and folklore"
    ],
    [
        "Уладзіслаў Сыракомля (Władysław Syrokomla)",
        "Вершы («Добрыя весці», «Не я пяю - народ Божы...», «Паштальён») (Poems (\"Good News\", \"The Postman\"))",
        "1823", "1862", "domestic",
        "poem-cycle", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "19th-century village-lyric romantic poetry"
    ],
    [
        "Тарас Шаўчэнка (Taras Shevchenko)",
        "Верш «Не грэе сонца на чужыне...» (\"The Sun Doesn't Warm in a Foreign Land\")",
        "1814", "1861", "translated:ukrainian",
        "poem", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Ukrainian national poet included in Grade 9 Belarusian Literature syllabus"
    ],
    [
        "Вінцэнт Дунін-Марцінкевіч (Vincent Dunin-Marcinkievich)",
        "Фарс-вадэвіль «Пінская шляхта», опера «Ідылія» (Farce-vaudeville \"Pinsk Nobility\", Opera \"Idyll\")",
        "1808", "1884", "domestic",
        "play", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Foundational modern Belarusian play satirizing tsarist bureaucracy and gentry"
    ],
    [
        "Канстанцін Вераніцын (Kanstantsin Veranitsyn)",
        "Паэма «Тарас на Парнасе» (\"Taras on Parnassus\")",
        "1834", "1903", "domestic",
        "poem", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Famous 19th-century humorous/satirical Belarusian poem"
    ],
    [
        "Францішак Багушэвіч (Frantsishak Bahushevich)",
        "Прадмова да зборніка «Дудка беларуская», вершы («Мая хата», «Быў у чысцы!», «Бог не роўна дзеле», «Хмаркі») (Prefaces and Poems from \"Dudka Belaruskaya\")",
        "1840", "1900", "domestic",
        "poem-cycle", "serfdom", "mandatory", "yes", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Manifesto of modern Belarusian national identity; \"Хмаркі\" mandated for memorization"
    ],
    [
        "Адам Гурыновіч (Adam Hurynovich)",
        "Вершы («Дзякуй табе, браце, Бурачок Мацею») (Poems (\"Thank You, Brother Maciej Burachok\"))",
        "1869", "1894", "domestic",
        "poem-cycle", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Late 19th-century Belarusian peasant-realist poetry"
    ],
    [
        "Эліза Ажэшка (Eliza Orzeszkowa)",
        "Аповесць «Хам», апавяданне «Зімовым вечарам» (Novella \"The Boor\", Short story \"On a Winter Evening\")",
        "1841", "1910", "domestic",
        "novella", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Positivist prose on Grodno rural life; read in Belarusian translation"
    ],
    [
        "Янка Лучына (Janka Lucyna)",
        "Вершы («Старасць не радасць...», «З крывавых дзён», «Роднай старонцы») (Poems (\"Old Age Is No Joy\", \"To My Native Land\"))",
        "1851", "1897", "domestic",
        "poem-cycle", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Late 19th-century patriotic lyric poetry"
    ],
    [
        "Цішка Гартны, Канстанцыя Буйла, А. Гурло (Tishka Hartny, Kanstantsyya Buyla, A. Hurlo)",
        "Вершы (на выбар) (Poems (by choice))",
        "~1887", "~1937", "domestic",
        "poem-cycle", "revolution-1905?", "choice-list", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Early 20th-century Belarusian rebirth lyric poetry (open choice formula)"
    ],
    [
        "Ядвігін Ш. (Yadvigin Sh.)",
        "Апавяданне «Бярозка» (\"Little Birch\")",
        "1869", "1922", "domestic",
        "short-story", "serfdom", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Early 20th-century realistic short story"
    ],
    [
        "Янка Купала (Yanka Kupala)",
        "Вершы («Мая вера», «А хто там ідзе?», «Прарок», «Явар і каліна»), паэма «Бандароўна» (Poems and poem \"Bandarouna\")",
        "1882", "1942", "domestic",
        "poem-cycle", "serfdom", "mandatory", "yes", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "National poet of Belarus; \"Явар і каліна\" mandated for memorization"
    ],
    [
        "Якуб Колас (Yakub Kolas)",
        "Паэма «Сымон-музыка», паэма «Новая зямля» (урыўкі), верш «Родныя вобразы» (Poems and epic poems \"Symon the Musician\", \"New Land\")",
        "1882", "1956", "domestic",
        "poem-cycle", "serfdom", "mandatory", "yes", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "National poet of Belarus; \"Родныя вобразы\" and \"Новая зямля\" excerpts mandated for memorization"
    ],
    [
        "Максім Багдановіч (Maksim Bahdanovich)",
        "Вершы («Санет» - «Паміж пяскоў Егіпецкай зямлі...», «Маладыя гады»), апавяданне «Апокрыф» (Sonnet, Lyric poems, Story \"Apocrypha\")",
        "1891", "1917", "domestic",
        "poem-cycle", "none/romance", "mandatory", "yes", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Foundational symbolist poet; \"Санет\" mandated for memorization"
    ],
    [
        "Алесь Гарун (Ales Harun)",
        "Вершы («Паэту», «Жыццё», «У прыпар», «Мяцеліца», «Малітва») (Poems (\"To the Poet\", \"Life\", \"Prayer\"))",
        "1887", "1920", "domestic",
        "poem-cycle", "revolution-1905?", "mandatory", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Early 20th-century lyric poetry"
    ],
    [
        "Леся Украінка (Lesya Ukrainka)",
        "Вершы (на выбар) (Poems (by choice))",
        "1871", "1913", "translated:ukrainian",
        "poem-cycle", "none/romance?", "choice-list", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Ukrainian classic translated into Belarusian"
    ],
    [
        "Яніс Райніс (Jānis Rainis)",
        "Вершы (на выбар) (Poems (by choice))",
        "1865", "1929", "translated:latvian",
        "poem-cycle", "none/romance?", "choice-list", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "Latvian national poet translated into Belarusian"
    ],
    [
        "Поль Верлен (Paul Verlaine)",
        "Вершы (у перакладзе А. Лойкі) (Poems (translated by A. Loyka))",
        "1844", "1896", "translated:french",
        "poem-cycle", "none/romance?", "choice-list", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "French symbolist lyric poetry translated into Belarusian"
    ],
    [
        "Артюр Рэмбо (Arthur Rimbaud)",
        "Вершы (на выбар) (Poems (by choice))",
        "1854", "1891", "translated:french",
        "poem-cycle", "none/romance?", "choice-list", "no", "9",
        "https://knihi.com/none/Vucebnaja_prahrama_dla_ahulnaadukacyjnych_ustanou_z_bielaruskaj_i_ruskaj_movami_navucannia_Bielaruskaja_litaratura_V-XI_klasy.html",
        "2023", "2026-08-10", "French symbolist poetry translated into Belarusian"
    ],

    # Russian Literature Track (Русская литература - 9 класс)
    [
        "Неизвестный автор (Unknown author)",
        "«Слово о полку Игореве» (\"The Lay of Igor's Campaign\")",
        "~1185", "~1185", "translated:russian",
        "epic", "Kyivan-Rus", "mandatory", "excerpt", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Mandatory Grade 9 Russian Literature curriculum text (re-recitation of Yaroslavna's Lament excerpt mandated)"
    ],
    [
        "М.В. Ломоносов (M.V. Lomonosov)",
        "Стихотворения (в том числе «Ода на день восшествия... 1747 года») (Poems (including \"Ode on the Accession Day... 1747\"))",
        "1711", "1765", "translated:russian",
        "poem-cycle", "Enlightenment", "mandatory", "excerpt", "9",
        "https://adu.by",
        "2023", "2026-08-10", "18th-century Russian classicism ode"
    ],
    [
        "Г.Р. Державин (G.R. Derzhavin)",
        "Стихотворения («Властителям и судиям», «Памятник») (Poems (\"To Rulers and Judges\", \"Monument\"))",
        "1743", "1816", "translated:russian",
        "poem-cycle", "Enlightenment", "mandatory", "excerpt", "9",
        "https://adu.by",
        "2023", "2026-08-10", "18th-century Russian classicist/pre-romantic poetry"
    ],
    [
        "Д.И. Фонвизин (D.I. Fonvizin)",
        "Комедия «Недоросль» (Comedy \"The Minor\")",
        "1745", "1792", "translated:russian",
        "play", "serfdom", "mandatory", "no", "9",
        "https://adu.by",
        "2023", "2026-08-10", "18th-century Russian satirical comedy"
    ],
    [
        "Н.М. Карамзин (N.M. Karamzin)",
        "Повесть «Бедная Лиза» (Novella \"Poor Liza\")",
        "1766", "1826", "translated:russian",
        "novella", "serfdom", "mandatory", "no", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Russian sentimentalist novella"
    ],
    [
        "В.А. Жуковский (V.A. Zhukovsky)",
        "Баллада «Светлана», элегия «Море» (Ballad \"Svetlana\", Elegy \"The Sea\")",
        "1783", "1852", "translated:russian",
        "poem-cycle", "1812-napoleonic-war?", "mandatory", "excerpt", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Russian romanticism ballad"
    ],
    [
        "А.С. Грибоедов (A.S. Griboyedov)",
        "Комедия «Горе от ума» (Comedy \"Woe from Wit\")",
        "1795", "1829", "translated:russian",
        "play", "decembrist-era", "mandatory", "excerpt", "9",
        "https://adu.by",
        "2023", "2026-08-10", "19th-century verse satire comedy; Chatsky monologue recitation mandated"
    ],
    [
        "А.С. Пушкин (A.S. Pushkin)",
        "Стихотворения, роман в стихах «Евгений Онегин» (Poems and novel in verse \"Eugene Onegin\")",
        "1799", "1837", "translated:russian",
        "novel", "1820s-gentry-life", "mandatory", "yes", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Core 19th-century Russian novel in verse; poem and letter recitations mandated"
    ],
    [
        "М.Ю. Лермонтов (M.Yu. Lermontov)",
        "Стихотворения, роман «Герой нашего времени» (Poems and novel \"A Hero of Our Time\")",
        "1814", "1841", "translated:russian",
        "novel", "caucasus-war?", "mandatory", "yes", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Psychological novel and lyrics; poem recitation mandated"
    ],
    [
        "Н.В. Гоголь (N.V. Gogol)",
        "Поэма «Мёртвые души» (Novel \"Dead Souls\")",
        "1809", "1852", "translated:russian",
        "novel", "serfdom", "mandatory", "no", "9",
        "https://adu.by",
        "2023", "2026-08-10", "19th-century Russian satirical epic prose novel"
    ],
    [
        "У. Шекспир (William Shakespeare)",
        "Трагедия «Гамлет» / сонеты (Tragedy \"Hamlet\" / Sonnets)",
        "1564", "1616", "translated:english",
        "play", "antiquity?", "choice-list", "no", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Prescribed foreign literature sub-unit inside Grade 9 Russian Literature"
    ],
    [
        "И.В. Гёте (Johann Wolfgang von Goethe)",
        "Трагедия «Фауст» (урыўкі) (Tragedy \"Faust\" (excerpts))",
        "1749", "1832", "translated:german",
        "play", "antiquity?", "choice-list", "no", "9",
        "https://adu.by",
        "2023", "2026-08-10", "Prescribed foreign literature sub-unit inside Grade 9 Russian Literature"
    ]
]

with open(tsv_path, "w", encoding="utf-8") as f:
    f.write("\t".join(header) + "\n")
    for r in rows:
        assert len(r) == 14, f"Row length mismatch: {len(r)}"
        f.write("\t".join(r) + "\n")

print(f"Successfully wrote {len(rows)} rows to {tsv_path}")

dom_count = sum(1 for r in rows if r[4] == "domestic")
trans_count = sum(1 for r in rows if r[4].startswith("translated:"))
print(f"Domestic works: {dom_count}")
print(f"Translated works: {trans_count} ({trans_count/len(rows)*100:.1f}%)")

# Break down translated by source language
trans_langs = {}
for r in rows:
    if r[4].startswith("translated:"):
        lang = r[4].split(":")[1]
        trans_langs[lang] = trans_langs.get(lang, 0) + 1
print("Translated breakdown by language:", trans_langs)
