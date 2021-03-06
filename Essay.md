# Реферат
## по курсу "Логическое программирование"

### студент: Трунов А.В.

## ТЕМА Логические языки и базы данных. 

## Результат проверки

| Преподаватель     | Дата         |  Оценка       |
|-------------------|--------------|---------------|
| Сошников Д.В. |              |               |
| Левинская М.А.|              |               |

> *Комментарии проверяющих (обратите внимание, что более подробные комментарии возможны непосредственно в репозитории по тексту программы)*

## Логические языки и базы данных. 

СУБД, или системы управления базами данных, в целом можно описать следующим набором характеристик:

1) Долговременное хранение больших данных.
2) Использование вспомогательной внешней памяти.
3) Коллективное пользование, а значит, параллельный доступ к данным и их многопоточное обновление.
4) Надёжность и защищённость.
5) Использование запросов, посредством которых из БД извлекается необходимая информация.
6) Использование ограничений, посредством которых поддерживается целостность БД и пресекаются попытки помещения в неё «неправильных» данных. [1]

В свою очередь, системы логического программирования в общем, и Пролог в частности, как наиболее распространённая из них, не полностью отвечают этим характеристикам. Пролог-программы часто называют базами знаний, чтобы подчеркнуть, что они управляются с более сложными данными. Однако, чаще всего, такие базы знаний являются внутренними (динамическими) и размещаются в оперативной памяти компьютера, то есть они не могут быть больших размеров и не обеспечивают коллективного пользования. Пролог, за счёт гибкости своей декларатировной составляющей, позволяет более конструктивно и выразительно формулировать запросы и составлять ограничения. Однако, его процедурная составляющая (которой нет в языках запросов вроде SQL), несколько нарушает «множественную» логику структуры баз данных, так как из-за неё он чувствителен как к порядку выполнения правил, так и к порядку их частей. Впрочем, за счёт своей процедурности, Пролог является Тьюринг-полным языком, в отличие от SQL. Ещё одним недостатком баз знаний Пролога можно назвать то, что в ответ на запрос пользователь получает ответ, состоящий из одного факта (например, подстановки переменной) за раз, и получает следующие факты, соответствующие форме запроса, только после специального требования (;). От языка запросов к базам данных мы ожидаем выдачи множества всех фактов (кортежей) сразу.  

В Прологе, как и в логическом программировании в целом, запрос реализуется через построение цепей логических выводов, в процессе фактическая информация и правила сопоставляются друг с другом для доказательства истинности или ложности утверждения. В СУБД выражается на специальном языке манипуляций с данными, оптимизируется на внешнем обработчике запросов, возможно, перестраивается в ходе оптимизации для нахождения наиболее эффективных путей доступа к большим данным, хранящимся в базе данных. 

Ограничения — условия правильности и целостности БД, в логическом программировании естественным образом описываются с помощью всеобъемлющих правил, соответствие которым проверяется при любом изменении базы данных. В СУБД набор ограничений, которые можно легко выразить на языке определения данных, обычно невелик. 

При совокупном рассмотрении проблем классического подхода к управлению базами данных и подхода со стороны логического программирования, становится ясно, что их решение лежит где-то на стыке этих областей. Обе дисциплины развивались одновременно, и с 70-х годов, после появления реляционной модели баз данных, активно проводились исследования их взаимосвязей. После публикации строгого изложения теории реляционных баз данных, стали появляться работы, предлагающие строить её на основе некоторой формальной системы или исчисления, расширяя таким образом «реляционную парадигму».  Базы данных, реализующие такой подход, стали называть дедуктивными. В 80-е годы была даже инициатива создания ЭВМ 5-го поколения, использующих мощный искусственный интеллект и параллельными процессорами,  которые могли бы работать с большими базами данных с помощью языка логического программирования на базе Пролога. Несмотря на то, что проект так и не был завершён, интерес к исследованиям на стыке направлений не исчез. [2]

## Реляционная модель и её связь с логикой

Реляционная модель — наиболее распространённая. Некоторые системы до сих пор используют иерархические и сетевые модели, но их с уверенностью можно назвать устаревшими. Существуют также объектно-ориентированная модель, но она менее распространена и не имеет чёткого однозначного определения.  

В базах данных, построенных на реляционной модели, данные хранятся в виде таблиц, которые задают между ними определённые отношения. 
Каждому столбцу таблицы в соответствие (взаимно однозначное) ставится его имя, а его имени — множество переменных, которым в свою очередь ставится множество их значений. Это множество значений называют доменом. Реляционная база данных подразумевает, что все значения чётко заданы и конкретизированы.  Помимо этого, логическая схема реляционной БД включает в себя набор ограничений, сохраняющих её целостность. Эти ограничения наиболее правильно выражать в логических формулах. 

Основа реляционной модели баз данных и её математический аппарат — реляционная алгебра – замкнутая система операций над отношениями. Основными операторами этого языка, через которые выражаются и другие операторы, являются следующие: 

1) Оператор выбора строки из таблицы
2) Оператор проекции
3) Операторы объединения, пересечения и разности. Они определены так же, как их аналоги в алгебре множеств.
4) Оператор декартова произведения.

Реляционное исчисление — альтернатива реляционной алгебре, сравнимо с ней по своей выразительности. [3]Более того, они логически эквивалентны. Принципиальное различие между ними заключается в том, что в реляционной алгебре явно определяются замкнутые операции над отношениями, а в реляционном исчислении задаётся набор обозначений, которые определяют требуемое отношение в терминах уже существующих. Вообще, реляционное исчисление весьма приближено к формальной теории исчисления предикатов первого порядка. Если при использовании реляционной алгебры указывается явная процедура решения задачи, то есть задача решается в терминах «как», то при использовании реляционного исчисления, мы указываем «что» за проблему мы хотим решить. Это приближает реляционное исчисление к  парадигме логического программирования. Более того, реляционное исчисление полностью декларативно, в отличие от того же Пролога. 
Это очень важно для реляционных БД, так как их реальное физическое хранилище данных как правило сокрыто от пользователя. 

Многие языки запросов к реляционным базам данных, вроде SQL, QUEL или QBE опираются на реляционное исчисление, и позволяют образаться к БД с помощью систем управления, использующих оптимизаторы запросов. 

Помимо простых отношений, языки запросов позволяют определять сложные (или производные). Так как результатом запроса является опять же отношение, можно составить запрос, определяющий отношения, не лежащие в самой базе данных, но выводящиеся из них. Такие отношения составляют то, что называют интенциональной базой данных. Отношения, находящиеся непосредственно в физической памяти базы данных, составляют экстенциональную базу данных.

Реляционное исчисление позволяет отношениям интенциональной базы данных быть достаточно сложными, но всё же его выразительной мощи не хватает для того, чтобы обеспечить их рекурсивностью. Этот факт является весьма существенным препятствием на пути к созданию «умных» баз данных. 

## Объединение Пролога и реляционной модели

На протяжении всего своего существования, Пролог является наиболее распространённым и, наверно, наиболее выразительным языком в парадигме логического программирования. У Пролога много общего с реляционным исчислением, так как они оба основаны на формальных логических теориях. 

Объединение этих двух дисциплин — естественный шаг, и он кажется концептуально простым, однако попытки сделать это «в лоб» привели к неэффективным решениям и выявили множество фундаментальных проблем. Как уже было упомянуто, факты и правила в Прологе зависят от порядка их расположения (и расположения их частей), в то время как в реляционных базах данных отношения образуют неупорядоченные множества. К тому же, Пролог содержит такие процедурные черты, как, например, предикат отсечения, с помощью которого программист сам управляет перебором вариантов ответа. Процедурная часть природы Пролога предоставляет программисту решать задачу оптимизации своих запросов. При использовании реляционного исчисления и языков запросов, построенных на нём, решение этой задачи остаётся за обработчиком (процессором) запросов, который может сам преобразовать запрос в целях оптимизации. 


За долгое время исследования проблемы объединения Пролога и реляционной модели баз данных, было предложено множество решений, ни одно из которых не оказалось достаточно эффективным, чтобы получить повсеместное распространение. Было рассмотрено множество различных подходов к самому интерпретатору Пролога (особенно к тому, как он использует основную экстенциональную базу данных), к его интерфейсу, к интерфейсу базы данных (варьировалась допустимая сложность запросов: от простейших, не отличающихся от принятых в реляционном исчислении, до сложных рекурсивных), и т. д. 


Эти поиски привели к созданию языка Datalog — языка на стыке Пролога и реляционных СУБД.

## Datalog

Дейталог — это язык, предназначенный для управления дедуктивными базами данных, которые являются сложными системами, объединяющими логику, искусственный интеллект и основные характеристики систем баз данных. 


Как язык логического программирования, Дейталог, как и Пролог, строится на дизъюнктах Хорна — дизъюнктивных одночленах, содержащих либо одну положительную (не содержащую логическое отрицание) атомарную формулу, либо ни одной. [4]
Как язык систем баз данных, Дейталог является содержащим рекурсию расширением реляционного исчисления. 
Развитие Пролога, приведшее к появлению Дейталога, напоминает развитие систем баз данных, протекавшее примерно в те же годы, в течение которого люди постепенно отказывались от иерархических и сетевых архитектур баз данных, двигаясь к реляционной.

Синтаксически, Дейталог мало чем отличается от Пролога. Например, моё задание курсового проекта (за исключением, возможно, правила related(X, Y) ) можно было бы выполнить и на Дейталоге, в частности, приведённый выше запрос был бы правильным запросом Дейталога. [5]



Однако, первое отличие заключается в том, что если, например, базе знаний родственных отношений, включающей факты:
```prolog
родитель(„Иван“, „Мария“). 
родитель(„Иван“, „Дарья“).
```
задать запрос: 
```prolog
?- родитель(„Иван“, X).
```
Дейталог ответит нам сразу: X = {„Мария“, „Дарья“}.

Проблема порядка расположения правил также частично решена в Дейталоге. Например, для определения отношения «Предок» в Прологе и Дейталоге мы можем использовать как предикат: 
```prolog
предок(X, Y) :- родитель (X, Y).
предок(X, Y) :- родитель(X, Z), предок(Z, Y).
```
так и предикат:
```prolog
предок(X, Y) :- предок(Z, Y), родитель(X, Z).
предок(X, Y) :- родитель (X, Y).
```
Но когда мы зададим Прологу вопрос:
```prolog
?- предок(X, Y)
```
То при процедуре логического вывода по второму предикату Пролог уйдёт в бесконечный цикл. Дейталог же будет работать одинаково в обоих случаях, и в обоих случаях выдаст правильный ответ. Зацикливание — одна из частых проблем, с которыми сталкивается программист на Прологе. Используя Дейталог, программист может о ней забыть. К тому же, при поиске ответов Дейталог обычно использует поиск в ширину, что более логично при работе с базами данных.

Дейталог не является процедурным языком, что приближает его к реляционному исчислению, но лишает части выразительной силы Пролога. В нём отсутствуют многие специальные предикаты, вроде отсечения. Таким образом, как язык логического программирования, Дейталог на самом деле представляет из себя что-то вроде усечённой версии Пролога, из которого убрали некоторые возможности, добавив при этом возможности, обеспечивающие адекватное общение с реляционными базами данных с помощью сложных (даже рекурсивных) запросов. 

Как формальная логическая система, чистый Дейталог не включает оператор разности, и поэтому запросы, использующие этот оператор, не могут быть записаны в нём иначе как с помощью логического отрицания. Однако, Дейталог поддерживает рекурсию, которая невыразима в реляционной алгебре. Таким образом, используя существующие дополнения к Дейталогу, а не чистый его вариант, мы добиваемся выразительности, строго большей чем та, которую можно добиться средствами реляционной алгебры. Помня о том, что реляционная алгебра логически эквивалентна реляционному исчислению, мы получаем, что «расширенный» Дейталог является действительно мощной логической системой.

Вопрос оптимизации запросов к базе данных также частично решён в Дейталоге и его расширениях. В конце прошлого века было разработано множество методов оптимизации, применимых к этой области, и исследования всё ещё ведутся. 

Как уже было сказано, на протяжении десятилетий, в течение которых разрабатавался Дейталог и исследовались его возможности, возникло множество расширений. Наиболее важным является дополнение, позволяющее использовать логическое отрицание в теле любого правила, что позволяет Дейталогу уйти от требования, чтобы все правила соответствовали модели дизъюнктов Хорна. Другие расширения также определяют встроенные предикаты вроде =, <, >, или арифметические операции: +, -, *, /, позволяют использовать функторы для работы с более сложными запросами и т. д.   

На самом деле, Дейталог сложно назвать полноценным языком, решающим все поставленные задачи. Это скорее удачная абстракция, позволяющая понять, в каких направлениях стоит двигаться в процессе их решения.


## Альтернативные архитектуры

Пролог и Дейталог задали направление исследований, но для того, чтобы полностью соединить парадигму логического программирования и языки баз данных, и получить эффективный непротиворечивый инструмент, требуется разработка новых решений и построение новых систем.

Два концептуально разных подхода к построению таких систем – через «связывание» и через «интеграцию». [6]

Связывание подразумевает создание интерфейса для общения различных систем логического программирования и баз данных между собой. Иными словами, каждая система разрабатывается отдельно и обладает индивидуальностью, а интерфейс, используя различные процедуры для транспортировки данных из долговременной памяти (среды хранения БД) в кратковременную (исполнительную среду логического программирования) при обработке поступающих запросов или при проверке ограничений. Именно этот подход был положен в основу проекта ЭВМ 5-го поколения. Он более характерен для систем, базирующихся на Прологе. 

Интеграция подразумевает создание 	единой системы, в которой язык логического программирования как бы обеспечивает «надстройку» над базисом базы данных. Этот подход можно назвать более радикальным, он требует разработки новых специфических алгоритмов и структур данных. Однако, он потенциально эффективнее своего собрата. Он более характерен для систем, базирующихся на Дейталоге. 

Несмотря на то, что связывание уступает интеграции в эффективности, в ряде задач достаточно и его. В свою очередь, связывание также принято делить на два типа: сильное и слабое. 

При слабом связывании, которое ещё называют статическим, взаимодействие между базой данных и системой логического программирования ограничено, оно происходит при компиляции, либо при загрузке процесса интерпретатором, и не зависит от процесса вывода. Из  базы данных извлекаются все базовые дизъюнкты, которые могут потребоваться программе во время её работы.  

При сильном связывании, которое также называют динамическим, обмен информацией между системами реализован в процессе вывода. Он происходит, когда для продолжения этого процесса системе логического программирования становятся необходимы дополнительные данные из базы. При сильном связывании осуществляется больше запросов к базе данных, чем при слабом, в то же время,  сильное связывание более избирательно, оно реализует только релевантные запросы в каждый отдельно взятый момент времени и требует меньше памяти для хранения необходимых данных. Впрочем, нельзя однозначно сказать, какой из подходов эффективнее.


## Заключение

Как было установлено, логика и логическое программирование предоставляют солидный фундамент для построения сложных систем баз данных, способных обрабатывать рекурсивные запросы. Теоретические исследования в различных областях дали нам возможность проектировать такие системы. Однако, Дейталог не нашёл повсеместного применения в современной науке и промышленности, прежде всего, из-за своей неэффективности и «размытости». Впрочем, он оказал большое влияние на развитие SQL — главного современного языка систем баз данных. Надо так же сказать, что в отдельных местах, таких как Стэнфордский университет, исследования в этом направлении продолжаются и по сей день.

Дальнейшее развитие дедуктивных баз данных было бы крайне полезно в ряде других дисциплин. Прежде всего, пользу из такого развития могло бы извлечь одно из крупных течений науки об искусственном интеллекте – разработка экспертных систем. В отличие от, например, нейронных сетей, это направление исследований не слишком бурно развивается в наши дни. Однако, потребность в его развитии есть. Экспертные системы чаще всего используются для решения задач, которые:
1) Не могут быть полно выражены в числовой форме (что весьма близко, например, языку Пролог, который используют преимущественно для решения символьных задач).


2) Либо не имеют точного алгоритмического решения, либо обладают ресурсами (память, время) настолько ограниченными, что прибегнуть к этому решению не представляется возможным (что близко к подходу решения задач со стороны искусственного интеллекта).
3) Требуют наличия чётко выстроенной базы знаний, состоящей из опыта экспертов в предметной области (что, очевидно, требует эффективного взаимодействия с большими базами данных).

При этом, при проектировании и разработке таких систем, возникает естественная потребность  в долговременных отказоустойчивых базах данных с конкурентным доступом, которые могли бы выполнять больше количество дедуктивных выводов за единицу времени (при работе над проектом ЭВМ 5-го поколения, например, ожидалось что они будут способны выполнять около миллиона выводов в секунду). 

Помимо экспертных систем, развитие дедуктивных баз данных помогло бы и остальным отраслям искусственного интеллекта. В конце концов, вышеупомянутый проект создания ЭВМ следующего поколения в Японии хоть и был завершён без достижения поставленной цели, это не значит, что к подобным целям не стоит возвращаться. Первый самолёт тоже пролетел над землёй всего несколько метров. 



Литература: 
[1] – Введение в системы баз данных. К. Дж. Дэйт (2018)

[2] – Logic Programming and Databases. Ceri, Stefano, Gottlob, Georg, Tanca, Letizia (1990)

[3] – Системы искусственного интеллект. Владимир Девятков (2001)

[4] – Logic and Databases. Johann Eder (1995)

[5] – Logic and Databases: A Deductive Approach. Herve Gallaire, Jack Minker, Jean-Marie Nicolas (Computing Surveys, Vol.16  no.2, June 1984).

[6] – Программирование на языке Пролог для искусственного интеллекта. Братко. И. (1990).

