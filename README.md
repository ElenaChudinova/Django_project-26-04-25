# Django_project
1. Настройка проекта
Создайте новую директорию для проекта и настройте виртуальное окружение.
Инициализируйте новый проект Django внутри этой директории.
Не забудьте про добавление файла 
.gitignore
 и правила ведения разработки по GitFlow. Создайте ветки 
main
, 
develop
 и отдельные ветки для решения домашек. Также не забудьте оформить файл README с описанием проекта.

2. Создание и настройка приложения
Создайте новое приложение под названием 
catalog
 в вашем проекте.
Зарегистрируйте приложение в настройках проекта.
Настройте маршрутизацию для нового приложения, добавив соответствующие URL-адреса.
3. Создание шаблонов
Подготовьте два HTML-шаблона: для домашней страницы и для страницы с контактной информацией.
Для стилизации страниц используйте Bootstrap.
Вы можете взять за основу следующие шаблоны:

home.html,
contacts.html.
4. Реализация контроллеров
Создайте контроллер для отображения домашней страницы.
Создайте контроллер для отображения страницы с контактной информацией.
Настройте маршрутизацию для этих контроллеров.
* Дополнительно
Реализуйте форму обратной связи на странице контактов.
Настройте обработку данных формы в контроллере, чтобы отображать сообщение об успешной отправке данных.

Задание 1
Подключите СУБД PostgreSQL для работы в проекте.

Создайте базу данных в ручном режиме.
Внесите изменения в настройки подключения в файле 
settings.py
.
Вы уже работали с этой СУБД в курсе «Работа с базами данных». В уроке «Введение в работу с базами данных» подробно описан процесс создания базы данных.

Задание 2
В приложении каталога создайте модели 
Product
 и 
Category
 и опишите для них базовые настройки.

Описание моделей:

Product
:
наименование,
описание,
изображение,
категория,
цена за покупку,
дата создания,
дата последнего изменения.
Category
:
наименование,
описание.
Поля «Дата создания» и «Дата последнего изменения» стали стандартом для моделей. Их общепринятые названия — 
created_at
 и 
updated_at
 соответственно.

Задание 3
Перенесите отображение моделей в базу данных с помощью инструмента миграций. Для этого:

создайте миграции для новых моделей;
примените миграции.
Важно сохранять всю историю миграций проекта для сохранения целостности базы данных проекта. Не забудьте добавить все выполненные миграции в коммит, а затем отправить в удаленный репозиторий на GitHub.

Задание 4
Создайте суперпользователя.
Зарегистрируйте модели 
Product
 и 
Category
 в админке.
Настройте отображение для моделей:
Для 
Category
 выведите 
id
 и 
name
 в списке.
Для 
Product
 выведите 
id
, 
name
, 
price
 и 
category
 в списке.
Настройте фильтрацию продуктов по категории.
Настройте поиск по полям 
name
 и 
description
.
Задание 5
Через инструмент shell заполните список категорий, а также выберите список категорий, применив произвольные рассмотренные фильтры.

Войдите в Django shell.
Создайте несколько категорий и продуктов.
Выполните следующие запросы:
Получите все категории.
Получите все продукты.
Найдите все продукты в определенной категории.
Обновите цену для определенного продукта.
Удалите продукт.
В качестве решения отправьте наставнику для проверки скриншоты выполнения команд.

Задание 6
Сформируйте фикстуры для моделей 
Category
 и 
Product
.

Задание 7
Создайте кастомную команду для добавления тестовых продуктов.
В команде удалите все существующие данные из базы перед добавлением новых продуктов.
Этот пункт можно реализовать в связке с инструментом работы с фикстурами, можно описать вставку данных отдельными запросами.

* Дополнительное задание
Добавьте в контроллер отображения главной страницы выборку последних 5 созданных продуктов и выведите их в консоль.
Создайте модель для хранения контактных данных и выведите данные, заполненные через админку, на страницу с контактами.

DZ 3

Задание 1
Создайте новый контроллер и шаблон для отображения страницы с подробной информацией о товаре. На этой странице должна быть показана вся информация о товаре.

Задание 2
Добавьте в шаблон главной страницы код для отображения списка товаров с помощью цикла. Чтобы карточки товаров выглядели одинаково, обрежьте отображаемое описание до первых 100 символов.

Задание 3
Из-за увеличения количества шаблонов возникает много повторяющегося кода. Выделите общий (базовый) шаблон, который будет включать общие элементы страницы, такие как шапка, подвал и стили. Также создайте подшаблон для главного меню, который можно будет включать в другие шаблоны.
