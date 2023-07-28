## Проект UI - автотестов для сервиса онлайн-меню GisMenu


### Основные моменты
- Тест-кейсы разработаны на языке Python с использованием фреймворков Selene, Pytest с применением PageObject и ООП
- Тест-кейсы выполняются на мобильных версиях браузеров Chrome (используется эмуляция устройств iPad, iPhone, Nexus) или Firefox (используется user-agent от браузера Safari)
- По умолчанию тест-кейсы выполняются на всех трех устройствах, но на продолжительных тест-кейсах использована параметризация
- Тест-кейсы запускаются удаленно на Selenoid
- Используется Allure Reports для  генерации отчетности и интерграции с системой тест-менеджмента Allure Test Ops
- Реализована интеграция с системой трекинга ошибок Jira
- Оповещение о результатах выполнения тестов приходят в Telegram


## Используемые технологии
<p align="center">
  <code><img width="5%" title="Python" src="images/techs/python.png"></code>
  <code><img width="5%" title="Pycharm" src="images/techs/pycharm.png"></code>
  <code><img width="5%" title="Selene" src="images/techs/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/techs/selenium.png"></code>
  <code><img width="5%" title="Pytest" src="images/techs/pytest.png"></code>
  <code><img width="5%" title="Selenoid" src="images/techs/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/techs/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/techs/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/techs/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/techs/tg.png"></code>
  <code><img width="5%" title="GitHub" src="images/techs/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/techs/jenkins.png"></code>
</p>

## Реализованные тест-кейсы

- Добавление и удаление позиций меню в корзину из индивидуальных карточек, а также основного меню
- Добавление и удаление позиций меню в меню корзины
- Поиск позиций в меню
- Переключение между меню
- Переключение между основным вкладками меню и информации, проверка контента во вкладках
- Проверка бокового меню

## Настройка проекта для удаленного запуска
- Переименовать файл .env.example в .env, внести свои данные

- Настроить запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/azavialov-qa-guru-python-5-26/) и нажать "Собрать сейчас". Выбрать браузер и версию браузера. Пример завершенной сборки по [ссылке](https://jenkins.autotests.cloud/job/azavialov-qa-guru-python-5-26/68/).
<img src="images/screens/jenkins_build.png" alt="Jenkins"/>

- Информация о прохождении тестов доступна в Allure - отчете сборки, в аттачментах есть исходный код страницы, скриншот и видео прохождения тест-кейса
<img src="images/screens/jenkins_allure_main.png" alt="Jenkins Allure report"/>
В разделе Suites представлена информация об устройствах, на которых запускались тест-кейсы
<img src="images/screens/jenkins_allure.png" alt="Jenkins Allure report"/>

- В разделе Graphs доступна статистика прохождения тест-кейсов
<img src="images/screens/allure_graphs.png" alt="Allure Graphs"/>

## Интеграция с Allure TestOps 
- После выполнения в Allure Test Ops создаются тест-кейсы, разделенный по тест-сьютам, с уже заполненными шагами, которые берутся из лямбда-степов внутри тест-кейсов
<img src="images/screens/test_ops_cases.png" alt="Allure Test Ops"/>
В этом же списке можно вручную добавить ручной тест-кейс

- Суммарная информация по автоматизированным и ручным кейсам доступна в дашборде
<img src="images/screens/test_ops_dashboard.png" alt="Allure Test Ops Dashboard"/>

## Интеграция с Jira
- К уже созданной в Jira задаче в разделе сьютов Allure Test Ops можно привязать тест-кейсы
<img src="images/screens/test_ops_link_cases_jira.png" alt="Link Test Ops test cases to Jira"/>

- Из раздела Launches можно привязать тестовый прогон
<img src="images/screens/test_ops_launches.png" alt="Link Test Ops launch to Jira"/>

- Тикет в Jira
<img src="images/screens/jira.png" alt="Jira"/>

## Настроена отправка отчета в Telegram

<img src="images/screens/telegram2.png" alt="Telegram"/>
