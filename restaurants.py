from restaurant_model import Restaurant



restaurants = [
        Restaurant(
            id=1, 
            title='Вспышка',
            description='Первая пышечная в Нижнем Новгороде, в которой можно купить невероятно вкусные и свежие пышки всего по 30 рублей за 1 штуку',
            photo_url='https://avatars.mds.yandex.net/get-altay/10447847/2a0000018afa0f65d8cbcc3f30398879460b/L_height',
            address='Нижний Новгород, ул. Алексеевская, 11',
            avg_price=200.0
            ),
         Restaurant(
            id=2, 
            title='Ёмаё',
            description='Группа компаний «Ё-маё» гордо шагает по Нижнему Новгороду с 2013 года. Именно тогда, 17 марта,  открылось наше первое заведение «Пельмени и вареники Ё-маё». С тех пор нашей главной задачей является не только накормить своих посетителей вкусной и разнообразной едой, но и украсить их досуг, сделав его более веселым и доступным',
            photo_url='https://lh3.googleusercontent.com/gps-proxy/ALd4DhHrxNqqhSrNcJEVod2bLbN_wsKuzXnKa1tbE41XctLJqk8k8BLvtGUP39lMaYtNKEitNnwyy_vOAb5Z_AQvbgA-VsrK7IKKGSWY3uC54EMKgsWBHWpNGABQJFPZFa4tKI7xGtFTWvPo-WTKIc_zc-7hqlEXVKdTqUN-sYJ2D8Q1ZlyUH8yjYDnNXQ=s1360-w1360-h1020',
            address='Нижний Новгород, ул. Большая Покровская, 22',
            avg_price=200.0
            ),
        Restaurant(
            id=3,
            title='Местечко моей мечты',
            description='«Местечко моей мечты» — это заведение быстрого питания, где можно вкусно и сытно перекусить. Гостям нравится местная шаурма, особенно шаурма с жульеном, а также бистро с курицей или мясом.',
            photo_url='https://yandex.ru/maps/org/mestechko_moyey_mechty/231615246267/gallery/?ll=44.032917%2C56.323049&photos%5Bbusiness%5D=231615246267&photos%5Bid%5D=urn%3Ayandex%3Asprav%3Aphoto%3ASpUu9M08MTrTaFRaduKv80SxmxthMQupl&z=15',
            address='Нижний Новгород, ул. Большая Печёрская, 48А',
            avg_price=350.0
            ),
        Restaurant(
            id=4, 
            title='Столовая №1',
            description='Столовая №1 — это место, где можно вкусно и недорого поесть. Здесь большой выбор блюд, включая супы, вторые блюда, гарниры, салаты, выпечку и десерты.',
            photo_url='https://lh3.googleusercontent.com/p/AF1QipMoiY50TTtdG2I8QmenbfWLqCwQdHXMWm0BpoBb=s1360-w1360-h1020',
            address='Нижний Новгород, ул. Большая Покровская, 24/22',
            avg_price=200.0
            ),
        Restaurant(
            id=5, 
            title='Совок',
            description='«Совок» — это место, где можно попробовать вкусную лапшу вок и венские вафли. Лапша вок здесь готовится вручную, а в меню есть конструктор, который позволяет выбрать лапшу, соус, источник белка и дополнительные ингредиенты, такие как овощи.',
            photo_url='https://aaanya.ru/wp-content/uploads/2018/05/Sovok.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 2',
            avg_price=200.0
            ),
        Restaurant(
            id=6, 
            title='Noot',
            description='Кафе Noot — это место, где вы можете насладиться вкусной и свежей едой, а также уютной атмосферой и дружелюбным персоналом.',
            photo_url='https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/ea/b1/4a/caption.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 15',
            avg_price=200.0
            ),
         Restaurant(
            id=7, 
            title='Лепи Тесто',
            description='Даже привычный продукт при внимании к деталям обретает дополнительную гастрономическую ценность. Лепи тесто-это новая модная пельменная,которая никого не оставит равнодушным.',
            photo_url='https://a-a-ah-ru.s3.amazonaws.com/uploads/items/142565/291914/large_XXXL.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 47 \ Нижний Новгород, ул. Минина, 12 \ Нижний Новгород, ул. Героя Фильченкова, 12',
            avg_price=200.0
            ),
         Restaurant(
            id=8,  
            title='Skuratov Coffee Roasters',
            description='Skuratov Coffee — это сеть стильных кофеен, которые полюбились фрилансерам и студентам. В каждой кофейне есть своя фишка в интерьере и неизменно хороший кофе',
            photo_url='https://cdn-imgproxy.mamado.su/gOit_8WDiD-nZ2Oxs0xTdf0Ls3LtAN8Fxli_KMlicvs/rs:fit:2000:2000:1/g:ce/q:90/czM6Ly9tYW1hZG8t/YXBpLXByb2R1Y3Rp/b24vc3RvcmFnZS8x/MTE4MTc2L1hYWEwu/anBlZw.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 2 \ Нижний Новгород, ул. Большая Печерская, 44 \ Нижний Новгород, ул. Ковалихинская, 4А \ Нижний Новгород,ул. Верхне-Волжская набережная, 2а',
            avg_price=200.0
            ),
        Restaurant(
            id=9, 
            title='Coffee Cake',
            description='Coffee Cake - место, где можно отвлечься от всего. С хорошим кофе, вкусной выпечкой и дружелюбным персоналом. Место, куда захочется возвращаться снова и снова.',
            photo_url='https://static.tildacdn.com/tild3135-3433-4830-a531-623366663331/A062D844-4980-4005-8.JPG',
            address='Нижний Новгород, ул. Большая Покровская, 2 \ Нижний Новгород, аэропорт Стригино \ Нижний Новгород, Парк "Швейцария"',
            avg_price=200.0
            ),
        Restaurant(
            id=10, 
            title='Библиотека',
            description='Кафе Biblioteca находится на третьем этаже книжного магазина «Дирижабль» и предлагает своим гостям широкий выбор блюд, включая пиццу, пасту, лазанью, салаты и десерты, такие как чизкейки и крем-брюле.',
            photo_url='https://galina-lukas.ru/sites/default/files/568/img_5225.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 46',
            avg_price=200.0
            ),
        Restaurant(
            id=11, 
            title='Юла Pizza',
            description='Ресторан «Юла пицца» — это популярное молодёжное место, где можно попробовать настоящую неаполитанскую пиццу, приготовленную в дровяной печи. Кроме пиццы, в ресторане можно заказать супы, салаты, горячие блюда и десерты, такие как лазанья, тирамису и медовик с кокосовым мороженым. \n Заведение удобно разделено на 3 секции-зала, общий стол для компании, винный и обычный зал, создающие спокойную, уютную атмосферу. В ресторане также есть летняя веранда, откуда открывается вид на детскую площадку, что делает его идеальным местом для семейного отдыха. \n P.S. Отдельно хочется отметить пиццу с красным луком и халапеньо для любителей острого) ',
            photo_url='https://avatars.mds.yandex.net/get-altay/10829645/2a00000189d003c3c4fecf2267f1d41b8483/XXXL.jpg',
            address='Нижний Новгород, Октябрьская ул., 9Б',
            avg_price=700.0
            ),
        Restaurant(
            id=12, 
            title='БлинБери',
            description='«БлинБери» — это приятное место, в котором можно не только вкусно и сытно покушать за небольшие деньги, но и поработать, так как там есть большие столы, мягкие диванчики и розетки у каждого стола. Вы можете попробовать различные виды блинов: мясные, рыбные, овощные и сладкие. Кроме того, в меню есть супы, каши и омлеты, а также кофе и молочные коктейли. \n Заведение оформлено в уютном и светлом интерьере, а персонал всегда готов помочь с выбором блюд. \n P.S. Всего за 149 рублей Вы можете отведать студенческий блин: сосиска из мяса индейки с картофельным пюре, хрустящими солёными огурцами и петрушкой.',
            photo_url='https://avatars.mds.yandex.net/get-altay/13930885/2a000001918ee36758886f193b3dd0ad587b/XXXL.jpg',
            address='Нижний Новгород, ул. Большая Печёрская, 65 \n Нижний Новгород, ул. Большая Покровская, 73 \n Нижний Новгород, просп. Ленина, 79Е',
            avg_price=350.0
            ),
        Restaurant(
            id=13,
            title='Моя Узола',
            description='Мы радуем не только настоящей домашней кухней. Всегда приветливые сотрудники, современный дизайнерский интерьер, чистота и высокий сервис — это наша гарантия вашего комфорта. Мы про здоровое питание: натуральные продукты, чистые составы блюд - вы всегда знаете, что едите. И всё по доступным ценам!',
            photo_url='https://avatars.mds.yandex.net/get-altay/10829645/2a0000018a46479d7bcf45fda68e629babd4/XXXL',
            address='Нижний Новгород, ул. Салганская, 24.',
            avg_price=300.0
            ),
        Restaurant(
            id=14,
            title='Верхушка кофе',
            description='В «Верхушке» делают эспрессо и американо, фильтр-кофе и напитки с молоком, например, горячий аффогато, в котором плавает шарик мороженого. Из сладкого — шоколадные какао и мокко, капучино с медовой гранолой, мандариновый раф. Любой кофе с небольшой доплатой можно взять на растительном молоке — банановом, ванильном, соевом или кокосовом. Есть травяные и ягодные чаи со специями, глинтвейн, молочные коктейли. Украшение витрины — выпечка: карамельно-яблочный пирог, домашний чизкейк, морковный торт, эклеры и овсяное печенье. Еще в кофейне можно съесть овсянку с медом, сырники со сметаной, бельгийские вафли, мороженое и легкий крем-суп. Новинка — рулеты-врапы с курицей, тунцом, вялеными томатами, шпинатом и моцареллой. Слева от входа на полках выставлены пакеты с зернами из разных регионов мира — все сорта можно приобрести домой.',
            photo_url='https://avatars.mds.yandex.net/get-altay/10445027/2a0000018c00cdf76abeb65378bcfd43b854/orig',
            address='Нижний Новгород, Большая Покровская, 2 — 1 этаж',
            avg_price=550.0
            ),
        Restaurant(
            id=15,
            title='О`Суси',
            description='«О`Суси» — это небольшое, но уютное японское кафе, расположенное в самом центре Нижнего Новгорода. Вам точно понравится местная кухня, особенно запеченные роллы, суп «Том Ям» и поке с лососем. Кроме того, можно отметить вежливость персонала и быструю подачу блюд. \n P.S. С 1 сентября студенты получают скидку 15% на всё меню! Просто покажите свой студенческий билет и наслаждайтесь вкуснейшими блюдами японской кухни',
            photo_url='https://avatars.mds.yandex.net/get-altay/1924793/2a0000016e711c0f82d6a23871654c319ea7/XXXL.jpg',
            address= 'Нижний Новгород, ул. Большая Покровская, 2 ',
            avg_price=1200.0
            ),
        Restaurant(
            id=16, 
            title='Хачапури | Выпечка и вино (Хачапурия)',
            description='Если Вы любите, чтобы было много и вкусно, «Хачапури | Выпечка и вино» - то, что Вам нужно! \n Здесь вы найдете широкий выбор блюд, включая хинкали, хачапури, долму и мцвади, а также домашние вина и чачу. Интерьер ресторана выполнен в грузинском стиле, с удобными диванами и приглушенным светом. Заботливый сервис и настоящее грузинское гостеприимство, Грузия ближе, чем Вы думаете! \n P.S. Вот, что действительно стоит попробовать - домашнее гранатовое вино, которого Вы не найдёте больше нигде!',
            photo_url='https://avatars.mds.yandex.net/get-altay/6955494/2a00000182ef1739857b5bb2ce71714b3bbb/XXXL.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 2/1 \n Нижний Новгород, ул. Большая Покровская, 6 \n Нижний Новгород, ул. Большая Покровская, 49 \n Нижний Новгород, ул. Бетанкура, 1 \n Нижний Новгород, пл. Советская, 5 \n Нижний Новгород, просп. Ленина, 67/1 \n Нижний Новгород, просп. Гагарина, 105А \n Нижний Новгород, просп. Гагарина, 35 \n Нижний Новгород, ул. Рождественская, 18',
            avg_price=1200.0
            ),
        Restaurant(
            id=17, 
            title='Салют',
            description='Бургерная «Салют» — это модное, современное и чистое место около центральной улицы города. Здесь нет стандартного обслуживания за столиками, а есть своя культура, которая начинается с приветствия «Салют!» на входе и заканчивается раздельной подачей напитков и блюд. В меню представлены вкусные бургеры с говядиной, курицей, окунем и разными овощами, а также картофель фри, салаты и напитки. / P.S. По будням с 11:50 до 16:00 можно заказать комплексный обед по цене бургера: любой бургер + картофель фри или салат коул слоу + куриный бульон.',
            photo_url='https://avatars.mds.yandex.net/get-altay/10233337/2a0000018f786a6a442daa95541571174073/XXXL.jpg',
            address='Нижний Новгород, Октябрьская, 9А',
            avg_price=600.0
            ),
        Restaurant(
            id=18, 
            title='Столовая199',
            description='Надоели замысловатые кафе, а готовить самому лень? Тогда «Столовая199» ваш фаворит! Почти за копейки можно поесть вкусно и сытно самую обычную еду, которую вам готовила мама.',
            photo_url='https://avatars.mds.yandex.net/get-altay/12850229/2a0000018e69a0f20ee4ab723259d171c96b/XXXL.jpg',
            address='ул. Ванеева, 199 (БЦ На Ванеева, этаж 2)',
            avg_price=400.0
            ),
        Restaurant(
            id=19, 
            title='Сиба Ину',
            description='«Сиба Ину» - место, где вы сможете открыть для себя азиатскую кухню. Приятная атмосфера, наличие мест для зарядок, вежливые сотрудники - всё это идеальные условия для уставшего и голодного студента.',
            photo_url='https://avatars.mds.yandex.net/get-altay/6195924/2a0000018f8683d779328705ec38ea46fd9c/XXXL.jpg',
            address='Большая Печёрская ул., 26, Нижний Новгород',
            avg_price=1500.0
            ),
        Restaurant(
            id=20, 
            title='Ахтуба',
            description='Кафе «Ахтуба» - самая близкая к корпусу на Большой Печёрской точка питания. Если вы устали после занятий, и у вас совсем не осталось сил никуда идти, то вам точно стоит заглянуть «Ахтубу»! \n В этом кафе есть и первые, и вторые, и горячие блюда, а также салаты. Кафе способно удивить и любителей чая своими необычными ароматами чая, и кофеманов вкусом свежесваренного кофе. \n P.S. В кафе можно заказать бизнес-ланч всего за 309 рублей, состоящий из первого, второго, салата и напитка.',
            photo_url='https://avatars.mds.yandex.net/get-altay/6010116/2a00000189cdb59652477cb510dd663122a8/XXXL.jpg',
            address='Нижний Новгород, ул. ​Большая Печёрская, 35​, цокольный этаж',
            avg_price=250.0
            ),
        Restaurant(
            id=21, 
            title='Столовая Буфетъ',
            description='Cеть кафе быстрого обслуживания «Буфетъ» — это быстро, вкусно и удобно. Здесь представлены полноценные обеды, различные напитки и вкуснейшие десерты. На раздаче приветливая и вежливая продавщица. Поток посетителей небольшой, поэтому очереди бывают крайне редко. Зал просторный и уютный, поддерживается чистота и порядок, светло и комфортно. Порции средние, цена очень приятная, что важно для студентов.  А ещё весь день действует бизнес-ланч от 250 рублей с широким выбором блюд.',
            photo_url='https://avatars.mds.yandex.net/get-altay/5495309/2a0000017cbb31162e110d201c6f0b2cb595/XXXL',
            address='ул. Пискунова, 31А, Нижний Новгород, этаж 1',
            avg_price=300.0
            ),
        Restaurant(
            id=22, 
            title='Космо',
            description='Добро пожаловать в КОСМОлаундж — место, где космос и комфорт объединяются в идеальный отдых. Приятная атмосфера, качественное обслуживание, современный интерьер, европейская, русская и паназиатская кухня. С 12:00 до 17:00 продаются бизнес-ланчи стоимостью от 280 до 349 рублей',
            photo_url='https://avatars.mds.yandex.net/get-altay/11622009/2a000001912c08880b15305d9b52d2b04611/XXXL',
            address='Большая Печёрская ул., 37, Нижний Новгород, этаж цокольный',
            avg_price=370.0
            ),
        Restaurant(
            id=23, 
            title='Старик Хинкалыч',
            description='«Старик Хинкалыч» — это кафе грузинской кухни, где вы можете попробовать различные виды хинкали: с мясом, грибами, сыром, креветками и зеленью, а также хачапури по-аджарски. Отличное место для встреч как с друзьями, так и с семьей. Вкусные хинкали, стоимостью от 45 рублей за штуку, в самом центре города. Приветливый персонал, уютная атмосфера, быстрое время приготовления',
            photo_url='https://avatars.mds.yandex.net/get-altay/11302718/2a0000018ff72d103099ca45c532c03e6f00/XXXL',
            address='Большая Покровская ул., 60',
            avg_price=400.0
            ),
        



]
