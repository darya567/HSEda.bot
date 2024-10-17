from restaurant_model import Restaurant



restaurants = [
        Restaurant(
            id=1, 
            title='Вспышка',
            description='Первая пышечная в Нижнем Новгороде, в которой можно купить невероятно вкусные и свежие пышки всего по 30 рублей за 1 штуку',
            photo_url='https://avatars.mds.yandex.net/get-altay/10447847/2a0000018afa0f65d8cbcc3f30398879460b/L_height',
            address='Нижний Новгород, Алексеевская, 11'
            ),
         Restaurant(
            id=2, 
            title='Ёмаё',
            description='Группа компаний «Ё-маё» гордо шагает по Нижнему Новгороду с 2013 года. Именно тогда, 17 марта,  открылось наше первое заведение «Пельмени и вареники Ё-маё». С тех пор нашей главной задачей является не только накормить своих посетителей вкусной и разнообразной едой, но и украсить их досуг, сделав его более веселым и доступным',
            photo_url='https://lh3.googleusercontent.com/gps-proxy/ALd4DhHrxNqqhSrNcJEVod2bLbN_wsKuzXnKa1tbE41XctLJqk8k8BLvtGUP39lMaYtNKEitNnwyy_vOAb5Z_AQvbgA-VsrK7IKKGSWY3uC54EMKgsWBHWpNGABQJFPZFa4tKI7xGtFTWvPo-WTKIc_zc-7hqlEXVKdTqUN-sYJ2D8Q1ZlyUH8yjYDnNXQ=s1360-w1360-h1020',
            address='Нижний Новгород, Большая Покровская ул., 22'
            ),
        Restaurant(
            id=3,
            title='Местечко моей мечты',
            description='«Местечко моей мечты» — это заведение быстрого питания, где можно вкусно и сытно перекусить. Гостям нравится местная шаурма, особенно шаурма с жульеном, а также бистро с курицей или мясом.Средний чек выходит всего на 350 рублей!!!',
            photo_url='https://yandex.ru/maps/org/mestechko_moyey_mechty/231615246267/gallery/?ll=44.032917%2C56.323049&photos%5Bbusiness%5D=231615246267&photos%5Bid%5D=urn%3Ayandex%3Asprav%3Aphoto%3ASpUu9M08MTrTaFRaduKv80SxmxthMQupl&z=15',
            address='Нижний Новгород, Большая Печёрская ул., 48А'
        ),
        Restaurant(
            id=4, 
            title='Столовая №1',
            description='Столовая №1 — это место, где можно вкусно и недорого поесть. Здесь большой выбор блюд, включая супы, вторые блюда, гарниры, салаты, выпечку и десерты.',
            photo_url='https://lh3.googleusercontent.com/p/AF1QipMoiY50TTtdG2I8QmenbfWLqCwQdHXMWm0BpoBb=s1360-w1360-h1020',
            address='Нижний Новгород, Большая Покровская ул., 24/22'
            ),
        Restaurant(
            id=5, 
            title='Совок',
            description='«Совок» — это место, где можно попробовать вкусную лапшу вок и венские вафли. Лапша вок здесь готовится вручную, а в меню есть конструктор, который позволяет выбрать лапшу, соус, источник белка и дополнительные ингредиенты, такие как овощи.',
            photo_url='https://aaanya.ru/wp-content/uploads/2018/05/Sovok.jpg',
            address='Нижний Новгород, Большая Покровская ул., 2'
            ),
        Restaurant(
            id=6, 
            title='Noot',
            description='Кафе Noot — это место, где вы можете насладиться вкусной и свежей едой, а также уютной атмосферой и дружелюбным персоналом.',
            photo_url='https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/ea/b1/4a/caption.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 15'
            ),
         Restaurant(
            id=7, 
            title='Лепи Тесто',
            description='Даже привычный продукт при внимании к деталям обретает дополнительную гастрономическую ценность. Лепи тесто-это новая модная пельменная,которая никого не оставит равнодушным.',
            photo_url='https://a-a-ah-ru.s3.amazonaws.com/uploads/items/142565/291914/large_XXXL.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 47 \ Нижний Новгород, ул. Минина, 12 \ Нижний Новгород, ул. Героя Фильченкова, 12'
            ),
         Restaurant(
            id=8,  
            title='Skuratov Coffee Roasters',
            description='Skuratov Coffee — это сеть стильных кофеен, которые полюбились фрилансерам и студентам. В каждой кофейне есть своя фишка в интерьере и неизменно хороший кофе',
            photo_url='https://cdn-imgproxy.mamado.su/gOit_8WDiD-nZ2Oxs0xTdf0Ls3LtAN8Fxli_KMlicvs/rs:fit:2000:2000:1/g:ce/q:90/czM6Ly9tYW1hZG8t/YXBpLXByb2R1Y3Rp/b24vc3RvcmFnZS8x/MTE4MTc2L1hYWEwu/anBlZw.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 2 \ Нижний Новгород, ул. Большая Печерская, 44 \ Нижний Новгород, ул. Ковалихинская, 4А \ Нижний Новгород,ул. Верхне-Волжская набережная, 2а'
            ),
        Restaurant(
            id=9, 
            title='Coffee Cake',
            description='Coffee Cake - место, где можно отвлечься от всего. С хорошим кофе, вкусной выпечкой и дружелюбным персоналом. Место, куда захочется возвращаться снова и снова.',
            photo_url='https://static.tildacdn.com/tild3135-3433-4830-a531-623366663331/A062D844-4980-4005-8.JPG',
            address='Нижний Новгород, ул. Большая Покровская, 2 \ Нижний Новгород, аэропорт Стригино \ Нижний Новгород, Парк "Швейцария"'
            ),
        Restaurant(
            id=10, 
            title='Библиотека',
            description='Кафе Biblioteca находится на третьем этаже книжного магазина «Дирижабль» и предлагает своим гостям широкий выбор блюд, включая пиццу, пасту, лазанью, салаты и десерты, такие как чизкейки и крем-брюле.',
            photo_url='https://galina-lukas.ru/sites/default/files/568/img_5225.jpg',
            address='Нижний Новгород, ул. Большая Покровская, 46'
            ),

]
