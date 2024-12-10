from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import news_post_form, login_form, register_form
from .models import news_post
import logging

def home_view(request):
    return render(request, 'app/home.html')

@login_required
def news_post_create_view(request):
    form = news_post_form()

    if request.method == 'POST':
        form = news_post_form(request.POST)
        
        if form.is_valid():
            form.save()
            # logger.warning(f'created new news_post: {form}')
            return redirect('news_posts')

    return render(request, 'app/news/news_post_form.html', {'form': form})


def news_posts_view(request):
    news_posts = news_post.objects.all()
    logging.warning('news post view')
    return render(request, 'app/news/news_posts.html', {'news_posts': news_posts})

def news_post_update_view(request, id):
    post = news_post.objects.get(id=id)

    form = news_post_form(instance=post)

    if request.method == 'POST':
        form = news_post_form(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('news_posts')

    return render(request, 'app/news/news_post_form.html', {'form': form})


def news_post_delete_view(request, id):
    post = news_post.objects.get(id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('news_posts')

    return render(request, 'app/news/news_post_confirm_delete.html', {'news_post': post})


def iu_1_view(request):
    images_path = 'images/departments/iu_1/'
    department_info = {
        'name': 'ИУ1',
        'full_name': 'Системы автоматического управления',
        'description': """Кафедра ИУ-1 «Системы автоматического управления» более 70 лет ведет подготовку специалистов и научные работы по системам управления различного назначения. Кафедра имеет устоявшиеся связи со многими ключевыми предприятиями промышленности, ВКП, ОПК и Роскосмоса. Основные направления учебной и научной деятельности кафедры:


системы управления космических аппаратов (спутников, пилотируемых, беспилотных);
системы управления летательных аппаратов в атмосфере (пилотируемые и беспилотные различных видов и конфигураций);
программное и алгоритмическое обеспечение бортовых комплексов управления;
алгоритмы обработки информации и комплексирования в навигационных комплексах летательных аппаратов.""",
        'education_directions': (
            '09.03.03 "Прикладная информатика"',
            '09.06.01 "Информатика и вычислительная техника"',
            '24.04.01 "Ракетные комплексы и космонавтика"',
            '24.05.06 "Системы управления летательными аппаратами"',
            '27.03.04 "Управление в технических системах"',
            '27.04.04 "Управление в технических системах"',
            '2.3.1 "Системный анализ, управление и обработка информации, статистика"',
        ),
        'images': (
            images_path + 'picture_1.jpg',
            images_path + 'picture_2.jpg',
        ), 
        'website_link': 'http://iu1.bmstu.ru/',
        'head_name': 'Пролетарский Андрей Викторович',
        'head_image': 'https://api.www.bmstu.ru/upload/member/2722/images/6181510175c0a/contain_560x560.jpg'
    }
    return render(request, 'app/department.html', {'department_info': department_info})


def iu_2_view(request):
    department_info = {
        'name': 'ИУ2',
        'full_name': 'Приборы и системы ориентации,стабилизации и навигации',
        'description': 'Выпускники кафедры получают как теоретические знания, так и практические навыки в разработке и производстве современных прецизионных гироскопов и навигационных приборов, а также в аналоговых и цифровых системах ориентирования, стабилизации и навигации подвижных объектов. Гироскопы и навигационные приборы представляют собой автономные источники информации, которые предоставляют данные об углах положения объекта, его угловой скорости, линейных ускорениях, скорости и перемещениях. Эта информация, иногда в сочетании с данными спутниковых навигационных систем, обрабатывается компьютерами и используется для автоматического управления, наведения и навигации различных транспортных средств, включая самолеты, ракеты, корабли, подводные лодки, космические аппараты, автомобили, буровые установки и летающие роботы. Также она служит основой для разработки индивидуальных средств навигации.',
        'education_directions': (
            '12.06.01 "Фотоника, приборостроение, оптические и биотехнические системы и технологии"',
            '24.05.06 "Системы управления летательными аппаратами"',
            '2.2.5 "Приборы навигации"',
        ),
        'website_link': 'http://iu2.bmstu.ru/department/department.html#0'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_3_view(request):
    department_info = {
        'name': 'ИУ3',
        'full_name': 'Информационные системы и телекоммуникации',
        'description': """Программы обучения кафедры направлена на подготовку широкопрофильных специалистов и охватывают различные сферы:
разработка программного обеспечения;
модернизация и обслуживание корпоративных информационных систем предприятий и их программное, техническое и организационное обеспечение;
разработка и сопровождение информационных технологий в различных областях и видах производственной и коммерческой деятельности;
создание и сопровождение интернет-пространства различных предприятий и учреждений.""",
        'education_directions' : (
            '09.03.02 "Информационные системы и технологии"',
            '09.04.02 "Информационные системы и технологии"',
            '09.06.01 "Информатика и вычислительная техника"',
            '2.9.8 "Интеллектуальные транспортные системы"',
            '2.3.5 "Математическое и программное обеспечение вычислительных систем, комплексов и компьютерных сетей"',
        ),
        'website_link': 'https://www.iu3.bmstu.ru/Home/NeuroQuest#top'
    }
    return render(request, 'app/department.html', {'department_info': department_info})


def iu_4_view(request):
    images_path = 'images/departments/iu_4/'
    department_info = {
        'name': 'ИУ4',
        'full_name': 'Системы автоматического управления',
        'description': """Базовое научное направление кафедры ИУ4 "Проектирование и производство электронной аппаратуры" - "Конструкторско-технологическая информатика в радиоэлектронике" направлено на исследования методов и разработку средств решения схемотехнических, конструкторских и технологических задач электронных систем в условиях комплексной информационной поддержки жизненного цикла изделий. В его основе лежат три основных компонента:
 - Конструкция (лат. constructio – строение, устройство, построение, план, взаимное расположение частей, англ. – construction, нем. – die Konstruktion, фр. – construction);
 - Технология (греч. techne – исскусство, мастерство + logos – понятие, учение, англ. – technology, нем. – die technologie, фр. - technologie);
 - Информатика (ср. нем. Informatik, англ. Information science, фр. Informatique, англ. computer science — компьютерная наука — в США, англ. computing science — вычислительная наука — в Великобритании) — наука о способах получения, накопления, хранения, преобразования, передачи, защиты и использования информации (в нашем случае конструкторско-технологической)).
 Под конструкцией электронных средств (ЭС) понимается совокупность элементов и деталей с различными физическими свойствами и формами, находящимися в определенной пространственной, механической, тепловой, электромагнитной и энергетической взаимосвязи. Эта взаимосвязь определяется системотехнической, схемотехнической, конструкторской и технологической документацией и обеспечивает выполнение электронной аппаратурой (ЭА) заданных функций с необходимой точностью и надежностью в условиях воздействия на нее различных факторов: эксплуатационных, производственных, социальных.
 Технология производства, или технологический процесс – основная часть производственного процесса, заключающаяся в выполнении определенных действий, направленных на изменение исходных свойств объекта производства (в нашем случае ЭА) и достижения им определенного состояния, соответствующей технической документации. Конструирование и технология производства являются, с одной стороны, отдельными частями сложного процесса разработки ЭА, а с другой, не могут выполняться в отдельности, без учета взаимосвязей между собой и с другими этапами разработки. Являясь этапами более общего процесса «разработка – производства - эксплуатация – утилизация» (жизненного цикла изделия), как конструирование, так и технология определяют в конечном итоге общие потребительские свойства ЭА.
 Информатика решает задачи обработки информации с использованием вычислительных машин и сетей. Тематика исследований в информатике обширна и постоянно расширяется: теория вычислимости и искусственный интеллект, теория сложности вычислений, информационные структуры и базы данных, социальный аспект развития информационных систем, языки программирования, представление знаний и т. п.
 
 По своему характеру, подготовка специалистов на кафедре, является междисциплинарной и охватывает область фундаментальной и прикладной науки и техники, предметом которой являются проектирование и совершенствование методов производства и применения интегрированных систем, основанных на законах и принципах нано- и микросистемной техники в условиях сквозной информатизации жизненного цикла изделий. Учебные программы формируются на основе последних достижений инженерных методов проектирования и системного анализа, физики твердого тела, квантовой электроники, физической химии, оптики и электронных технологий. Их содержание определяется необходимостью установления фундаментальных закономерностей, определяющих физико-химические особенности формирования микро- и наноразмерных структур, формирования заданных механических, электронных и оптических свойств данных структур и синтез на основе микро- и наносистемной элементной базы функциональных средств и систем нового поколения. Направления подготовки включают в себя разработку и создание функционально законченных сложных микро- и нанокомпонентов, материалов, электронной элементной базы, синтез технологических процессов их изготовления, исследования физических и физико-химических явлений в процессах их получения, проектирование и конструирование приборов на основе современной элементной базы и перспективных материалов, методы разработки и применения диагностического и технологического оборудование, синтез математических моделей процессов электронных технологии и объектов электроники в рамках комплексной сквозной информатизации и цифровой трансформации промышленности.
 Коллектив кафедры неоднократно становился победителем конкурса грантов Президента Российской Федерации для государственной поддержки молодых российских ученых и по государственной поддержке ведущих научных школ Российской Федерации.
 Возглавляет кафедру член-корреспондент РАН В.А.Шахнов
""",
        'education_directions' : (
            '11.03.03 "Конструирование и технология электронных средств"',
            '09.06.01 "Информатика и вычислительная техника"',
            '11.04.03 "Конструирование и технология электронных средств"',
            '2.3.1 "Системный анализ, управление и обработка информации, статистика"',
            '2.3.2 "Вычислительные системы и их элементы"',
            '09.06.01 "Информатика и вычислительная техника"',
            '12.06.01 "Фотоника, приборостроение, оптические и биотехнические системы и технологии"'
        ),
        'images': (
            images_path + 'picture_1.jpg',
            images_path + 'picture_2.jpg',
            images_path + 'picture_3.jpg',
            images_path + 'picture_4.jpg',
            images_path + 'picture_5.jpg',
            images_path + 'picture_6.jpg',
        ),
        'website_link': 'https://iu4.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_5_view(request):
    images_path = 'images/departments/iu_4/'
    department_info = {
        'name': 'ИУ5',
        'full_name': 'Системы обработки информации и управления',
        'description': """Кафедра «Системы обработки информации и управления» (ИУ5) является одной из старейших в МГТУ им. Н.Э. Баумана. Она была создана в 1938 году профессорами С.О. Доброгурским и Н.И. Пчельниковым и конструкторами приборостроительных заводов К.Н. Богдановым и С.Н. Калашниковым. Более 25 лет кафедра осуществляла подготовку специалистов по счетно-решающим приборам и устройствам. В последующие годы специалисты готовились для работы в областях специализированных электронно-вычислительных машин, а с 1969 г. – автоматизированных систем управления.
 Сегодня, пройдя такой длинный жизненный путь, она обучает студентов методам и технологиям разработки систем управления для организационных структур широкой отраслевой принадлежности и разной величины: от малых и средних предприятий до отраслевых и общегосударственных систем управления. В проблематику кафедры входит архитектура систем, прикладное программное обеспечение, реализующее конкретные бизнес-процессы, а также платформенное программное и техническое обеспечение, включающее базы данных, хранилища данных, озёра данных, графы знаний, системы блокчейн, сервера приложений, средства интеграции, системы виртуальной и дополненной реальности, платформы интернета вещей и другие компоненты платформ.

 Особое внимание на кафедре уделяется средствам искусственного интеллекта, используемым при разработке систем управления. Активно применяются нейросети, средства логического искусственного интеллекта, сложные графовые и имитационные модели, средства взаимодействия на естественных языках, средства машинного обучения для обработки сигналов, визуальных изображений, речи и видео. В качестве перспективы систем управления кафедра предлагает гибридные интеллектуальные информационные системы, включающие сознание, подсознание, модули этики, целеполагания, адаптации к окружающей среде и другие блоки общего искусственного интеллекта.

Практика и будущая карьера
Карьерный путь выпускника, выбравшего область разработки, внедрения и сопровождения корпоративных систем управления обычно начинается с позиции специалиста технической поддержки пользователей, администратора приложений, консультанта по одному из модулей корпоративной системы, Data-инженера или Machine Learning-инженера. После накопления профессионального опыта выпускники продолжают свою карьеру как руководители команд и групп по этим направлениям, архитекторы приложений. Следующей ступенью являются позиции менеджера проектов или продуктов, специалиста по взаимодействию с клиентами и подрядчиками, руководителя группы ИТ-архитектуры предприятия. Высший эшелон ‒ это ИТ-директора предприятий, руководители консалтингового бизнеса или бизнеса по разработке приложений.

 Выпускники кафедры «Системы обработки информации и управления» работают в крупнейших ИТ-компаниях, как российских (Яндекс, Сбертех, VK, Ozon, НИИ Восход), так и зарубежных (Google, Cisco и других). Большие известные компании – это лидеры отрасли, но они не дают полной картины. Кроме того наши выпускники работают в ИТ-подразделениях тысяч российских компаний и организаций, внедряя и эксплуатируя системы управления во всех секторах экономики и бюджетной сферы.
 Помимо этого, наши выпускники работают в РФ и за рубежом в ведущих международных компаниях–разработчиках корпоративных систем управления: SAP, Microsoft, 1C, Oracle. IBM, Галактика, Infor, а также в сотнях консалтинговых компаний-партнёров по внедрению бизнес-приложений, в том числе в таких крупных, как ассоциированные компании PwC, EY, Deloitte, KPMG, IBM, Accenture. Большая конкуренция за наших выпускников обусловлена их высоким уровнем подготовки. Широкий спектр работодателей обеспечивает им быстрый карьерный рост, высокий уровень оплаты труда и гарантированный социальный пакет.""",
        'education_directions' : (
            '09.03.01 "Информатика и вычислительная техника"',
            '09.06.01 "Информатика и вычислительная техника"',
            '09.04.01 "Информатика и вычислительная техника"',
            '2.3.1 "Системный анализ, управление и обработка информации, статистика"',
            '2.3.5 "Математическое и программное обеспечение вычислительных систем, комплексов и компьютерных сетей"'
        ),
        'images': (
            images_path + 'picture_1.jpg',
            images_path + 'picture_2.jpg',
            images_path + 'picture_3.jpg',
            images_path + 'picture_4.jpg',
        ),
        'website_link': 'https://iu5.bmstu.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})


def iu_6_view(request):
    department_info = {
        'name': 'ИУ6',
        'full_name': 'Интеллектуальные системы и компьютерные науки',
        'description': 'Учебный процесс на кафедре ИУ6 основывается на комбинировании теоретических и практических занятий. Студенты имеют возможность работать над реальными проектами, что способствует развитию их практических навыков и подготовке к будущей профессиональной карьере. Кафедра также активно занимается научной деятельностью, проводя исследования в области искусственного интеллекта, робототехники и прикладной информатики. Студенты могут принимать участие в научных проектах и конференциях, что позволяет им развивать свои исследовательские навыки.',
        'education_directions' : (
            '09.03.01 "Информатика и вычислительная техника"',
            '09.03.03 "Прикладная информатика"',
            '09.04.01 "Информатика и вычислительная техника"',
            '09.06.01 "Информатика и вычислительная техника"',
            '2.3.1 "Системный анализ, управление и обработка информации, статистика"',
            '2.3.5 "Математическое и программное обеспечение вычислительных систем, комплексов и компьютерных сетей"',
            '2.3.8 "Информатика и информационные процессы"'
        ),
        'website_link': 'https://project9612975.tilda.ws/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_7_view(request):
    department_info = {
        'name': 'ИУ7',
        'full_name': 'Программное обеспечение ЭВМ и информационные технологии',
        'description': 'Кафедра готовит универсальных IT-специалистов с широким диапазоном знаний в области проектирования и разработки программного обеспечения. Выпускники кафедры успешно трудятся в таких ролях, как бэкенд и фронтенд разработчики, мобильные разработчики, специалисты по анализу данных и машинному обучению, системные аналитики, архитекторы, тимлиды и руководители различного уровня в ведущих российских и международных компаниях.',
        'education_directions' : (
            '09.03.04 "Программная инженерия"',
            '09.04.04 "Программная инженерия"',
            '09.06.01 "Информатика и вычислительная техника"',
            '1.2.2 "Математическое моделирование, численные методы и комплексы программ"',
            '2.3.5 "Математическое и программное обеспечение вычислительных систем, комплексов и компьютерных сетей"',
            '2.3.7 "Компьютерное моделирование и автоматизация проектирования"'
        ),
        'website_link': 'https://iu7.bmstu.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_8_view(request):
    department_info = {
        'name': 'ИУ8',
        'full_name': 'Информационная безопасность',
        'description': 'Кафедра является одной из ведущих в России в области подготовки специалистов по комплексному обеспечению информационной безопасности. Она охватывает широкий спектр тем, включая математические основы и современные системы защиты информации.',
        'education_directions' : (
            '09.06.01 "Информатика и вычислительная техника"',
            '10.04.01 "Информационная безопасность"',
            '10.05.03 "Информационная безопасность автоматизированных систем"',
            '10.05.01 "Компьютерная безопасность"',
            '10.06.01 "Информационная безопасность"',
            '1.2.4 "Кибербезопасность"',
            '2.3.5 "Математическое и программное обеспечение вычислительных систем, комплексов и компьютерных сетей"',
            '2.3.6 "Методы и системы защиты информации, информационная безопасность"'
        ),
        'website_link': 'https://iu8.bmstu.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_9_view(request):
    department_info = {
        'name': 'ИУ9',
        'full_name': 'Теоретическая информатика и компьютерные технологии',
        'description': """Кафедра предоставляет подготовку бакалавров по направлению «Прикладная математика и информатика» и магистров по направлению «Прикладная математика».

Мы обучаем разработчиков математического и программного обеспечения для высокотехнологичных областей техники и современных информационных технологий, с акцентом на высокоэффективное программирование. Это включает в себя глубокие знания алгоритмов, технологий компиляции и оптимизации программного кода, а также особенности создания многопоточных, параллельных и распределенных приложений.

Учебные программы основаны на прочной математической подготовке, схожей с базовой математической подготовкой на физико-математических специальностях традиционных университетов. Кроме того, студенты знакомятся с рядом предметных областей, где активно применяются последние достижения в математике и программировании, включая лингвистику, биоинформатику и молекулярное моделирование.""",
        'education_directions' : (
            '09.06.01 "Информатика и вычислительная техника"',
            '2.3.5 "Математическое и программное обеспечение вычислительных машин, комплексов и компьютерных сетей"',
            '01.03.02 "Прикладная математика и информатика"'
            '01.04.04 "Прикладная математика"'
        ),
        'website_link': 'https://iu9.bmstu.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_10_view(request):
    department_info = {
        'name': 'ИУ10',
        'full_name': 'Защита информации',
        'description': """Кафедра ИУ10 «Защита информации» МГТУ им. Н.Э. Баумана осуществляет подготовку профессионалов в сфере информационной безопасности для кредитно-финансового сектора.

Программа нацелена на подготовку специалистов, отвечающих за обеспечение информационной безопасности и операционной надежности в организациях, работающих в финансовой сфере. Студенты осваивают навыки разработки систем и инструментов защиты информации, расследования компьютерных преступлений, управления инцидентами безопасности, выявления и предотвращения кибератак, а также борьбы с мошенническими действиями.""",
        'education_directions' : (
            '10.05.03 "Информационная безопасность автоматизированных систем"',
            '10.05.07 "Противодействие техническим разведкам"',
            '10.06.01 "Информационная безопасность"',
            '2.3.6 "Методы и системы защиты информации, информационная безопасность"'
        ),
        'website_link': 'https://iu10.bmstu.ru/'
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_11_view(request):
    department_info = {
        'name': 'ИУ11',
        'full_name': 'Космические приборы и системы',
        'description': """Изучаются принципы проектирования и функционирования систем управления, а также анализируются методы навигации и управления полетом. Студенты исследуют современные технологии автоматизации космических миссий и углубляются в компьютерное моделирование, оптимизацию систем управления и обработку данных с космических аппаратов. Эта программа фокусируется на подготовке студентов к разработке интегрированных систем управления, обеспечивающих эффективное и безопасное функционирование ракетно-космических комплексов и космических устройств.

Учебный план включает углубленное изучение математики, физики, теоретической механики, теории управления и регулирования, системного анализа и информатики. С применением полученных теоретических знаний выпускник способен создавать сложные математические модели исследуемых процессов или технических систем. Он может также разрабатывать алгоритмы обработки информации и управления, которые на основе накопленных знаний в динамической экспертной системе позволяют формировать необходимые команды для достижения поставленных целей системы.""",
        'education_directions' : (
            '2.2.5 "Приборы навигации"',
            '12.06.01 "Фотоника, приборостроение, оптические и биотехнические системы и технологии"'
        ),
        'website_link': ''
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def iu_12_view(request):
    department_info = {
        'name': 'ИУ12',
        'full_name': 'Технологии искусственного интеллекта',
        'description': """Кафедра ИУ12 «Технологии искусственного интеллекта» обучает специалистов в области разработки технологий ИИ и их практического применения в киберфизических системах для различных секторов, таких как промышленность, телекоммуникации, здравоохранение и государственные учреждения.

Студенты кафедры вовлечены в актуальные и передовые научные исследования и практические проекты уже в процессе обучения, сотрудничая с МГТУ и его предприятиями-партнерами.""",
        'education_directions' : (
            '09.04.01 "Информатика и вычислительная техника"',
        ),
        'website_link': ''
    }
    return render(request, 'app/department.html', {'department_info': department_info})

def deans_office_schedule_view(request):
    return render(request, 'app/students/deans_office_schedule.html')


def student_council_view(request):
    return render(request, 'app/students/student_council.html')

def register_view(request):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = register_form()
    return render(request, 'app/auth/register.html', {'form': form})


def login_view(request):
    form = login_form(data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'app/auth/login.html', {'form': form})

        
def logout_view(request): 
    if request.method == 'POST':
        logout(request)

    return redirect('home')


def session_countdown_timer_view(request):
    return render(request, 'app/students/session_countdown_timer.html')
