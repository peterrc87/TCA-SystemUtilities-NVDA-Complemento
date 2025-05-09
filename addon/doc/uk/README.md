## TCA SystemUtilities.

Невеликий додаток, який дозволяє нам швидко виконувати низку дій у Windows за допомогою комбінацій клавіш. 
Він здатний виконувати ремонт системи за допомогою засобу перевірки системних файлів (SFC). Ви можете скопіювати системну інформацію в буфер обміну, увійти в BIOS і багато іншого. 
Ви також можете відкрити офіційний сайт з додатками, щоб отримати додатки для NVDA, видалити налаштування й додатки на захищених екранах.

* Автор: Peter Reina <peterrc87@gmail.com>
* Сумісність: NVDA 2018 до 2023.3

## Функції системи:

* Завершити роботу системи: Вимикає ПК 
 Крім того, він видає класичний звук завершення роботи Windows. Він сповіщає вас про те, що систему буде вимкнено.
 Він пропонує вам можливість вимкнути або скасувати вимкнення за 3 секунди.

* Перезавантажити систему: Перезавантаження Windows 
 Крім того, він видає класичний звук завершення роботи Windows. Він сповіщає вас про те, що систему буде перезавантажено.
 Він пропонує вам можливість перезавантажити або скасувати перезавантаження за 3 секунди.

* Скасувати (вимкнення або перезавантаження): Дозволяє вам скасувати будь-який із двох попередніх варіантів (вимкнення або перезавантаження) 
Крім того, він попереджає вас повідомленням про те, що вимкнення/перезавантаження скасовується.
 Увага! У вас є лише 3 секунди на виконання цієї дії.

* Режим глибокого сну: Дозволяє зручно за допомогою NVDA перевести систему в режим сну.

* Перезавантажити та увійти в безпечний режим з підтримкою мережі: Цю функцію іноді дуже складно реалізувати, але з TCA SystemUtilities це можна виконати надзвичайно легко. 
Додаток дуже легко дозволяє вам увійти в Windows з обмеженими функціями, не завантажуючи непотрібні служби або програми, де ви можете зробити ретельніше очищення, видалити небажані програми, шкідливе програмне забезпечення та багато іншого. 
Важливе зауваження! 
У цьому режимі в системах раніших за Windows 10 може бути відсутній звук, тому читач екрана  не матиме голосової підтримки. 
Після активації цієї функції її можна вимкнути з меню TCA SystemUtilities, в розділі: "Вихід з системи".

* Перезавантажити в звичайному режимі: Дозволяє відключити безпечний режим, якщо ви його активували, він повертає запуск Windows до звичайних значень (завантажуються всі служби та програми, які використовуються при запуску). 

* Сон: Дозволяє за допомогою NVDA призупинити роботу системи. 
* Увійти в BIOS-UEFI: Ви зможете зручним способом за допомогою Windows і NVDA увійти в BIOS-UEFI під час наступного перезавантаження ПК. 
Не потрібно натискати або знати спеціальну клавішу, це дуже легко зробити з TCA SystemUtilities. 
Пам'ятайте, що в BIOS-UEFI ви не зможете скористатися читачем екрана, Як тільки ви захочете завантажитись в систему, ви можете це зробити за допомогою комбінації клавіш: CTRL+ALT+Delete.

* Відкрити командний рядок у цьому шляху: За допомогою комбінації клавіш ви можете відкрити командний рядок Windows (CMD) у будь-якій папці де перебуває фокус.

* Відкрити командний рядок з правами адміністратора: За допомогою комбінації клавіш ви відкриєте командний рядок Windows із усіма правами адміністратора (однак у системах до Windows 10 виберіть шлях до папки, де розташований фокус, інакше це буде відкрито в System32).

* Запуск консолей: Відкриває меню, в якому є списки консолей: CMD, Powershell, Windows Terminal, Git Bash. Звідси можна відкрити будь-яку з цих консолей (навіть з правами адміністратора) в директорії, в якій знаходиться фокус NVDA.

* Цей модуль був розроблений: Héctor Benítez Corredera.

* Очистити буфер обміну та його історію: Зручна функція, яка очищає весь вміст буфера обміну в Windows 10 і 11, також очищає все, що є в історії, якщо вона увімкнена. 

* Закриття процесів будь-яких активних програм: намагається закрити будь-які активні процеси, відмінні від Windows, навіть якщо вони працюють у фоновому режимі.

* Перезапустити провідник: Це дозволяє комфортно перезапустити Провідник Windows з NVDA. 
Ви можете зробити це за допомогою комбінації клавіш, яку перед цим потрібно призначити, або з меню TCA SystemUtilities.

* Закрити всі програми: Примусово закриває всі активні процеси, які не є частиною Windows (Увага! всі процеси будуть примусово закриті, тому ні документи, ні проекти не будуть збережені, і навіть NVDA буде закрито).

* Закрити процеси, які не відповідають: TCA SystemUtilities намагатиметься закрити процеси, які не відповідають. 

* Дізнатись архітектуру системи: Це скаже вам, яка архітектура Windows (32 або 64 біт). 
 
* Приховати папки: Дозволяє встановити атрибут прихованості для папки, в якій ви перебуваєте, тобто ця папка не буде відображатися (ви повинні призначити гарячі клавіші, щоб мати можливість використовувати цю функцію).

* Показати приховані папки: Ця функція дозволяє вам зробити видимими всі папки і файли, які приховані (діє в USB-флешках, зовнішніх дисках і т.д.), дуже корисно при підключенні будь-якого зовнішнього пристрою. Треба зайти в папку і натиснути комбінацію клавіш.
 

## Ремонт і оптимізація. 

* Виконати сканування системи за допомогою SFC: Дозволяє виконати сканування / відновлення файлової системи Windows SFC / SCANNOW.

* Вимкнути зарезервований простір: Повертає майже 10 Гб, які Windows забирає з вашого жорсткого диска для оновлень (не обов'язково вмикати цю функцію для роботи оновлень).

* Увімкнути зарезервований простір: Якщо ви все ще хочете активувати цю функцію Windows і змусити жорсткий диск зарезервувати майже 10 Гб, ця дія активує її.

•	Активувати план високої продуктивності: За допомогою комбінації клавіш або з меню TCA SystemUtilities ви можете активувати план високої продуктивності Windows простим, швидким і прямим способом. Не потрібно переходити до розширених налаштувань живлення на панелі керування.
•	Активувати план збалансованої продуктивності: За допомогою комбінації клавіш або з меню TCA SystemUtilities ви можете активувати план збалансованої продуктивності Windows простим, швидким і прямим способом. Не потрібно переходити до розширених налаштувань живлення на панелі керування.

* Очистити кеш DNS: Швидко і безпосередньо очищає весь кеш DNS Windows (може усунути проблеми з переглядом веб-сторінок). 

* Очистити збережену конфігурацію для запуску на захищених екранах: Видаляє всі додатки та налаштування, які ви скопіювали для запуску на захищених екранах, залишаючи NVDA такою, яка вона є початково. 

* Очищення диска: Дозволяє запустити Windows Disk Cleaner, але з набагато розширеними можливостями. Він очистить всі підключені до системи диски та носії інформації. 
При першому запуску у вас з'явиться діалог для створення профілю очищення, ви можете поставити прапорці на категоріях, які ви хочете очистити. Зручно, що ви натискаєте кнопку: "Створити профіль" лише один раз. У вас буде прапорець, який ви можете позначити, якщо ви більше не хочете, щоб цей діалог з'являвся. 
 
* Ремонт системи за допомогою Dism: Виконує глибоке сканування і намагається виправити проблеми в Windows.



## Прямі функції буфера обміну:

* Копіювання в буфер обміну списку папок чи файлів поточного шляху: 
Він копіює безпосередньо в буфер обміну список елементів шляху, де ми перебуваємо, щоб ми могли вставити його в будь-яке поле для редагування.

* Копіювання в буфер обміну інформації про звукові карти: дозволяє скопіювати безпосередньо в буфер обміну інформацію про всі звукові пристрої, які є в системі.
Таким чином, ми зможемо вставити її в будь-яке поле редагування. 

* Копіювання інформації про всю систему в буфер обміну: дозволяє нам копіювати безпосередньо в буфер обміну інформацію про нашу систему. 
Таким чином, ми можемо вставити її в будь-яке поле редагування. 

* Копіювання шляху: копіює в буфер обміну шлях до папки, у якій ми перебуваємо. 
 Таким чином, ми зможемо вставити його в будь-яке поле редагування. 
 

## Параметри безпеки Windows (Windows Defender).
* Увімкнути контроль облікових записів користувачів (uac): встановлює рівень контролю облікових записів користувачів на 34 (увімкнено).

* Сканування завантаження системи: виконує пряме сканування на віруси та шкідливе програмне забезпечення файлів, які належать до завантажувального сектора Windows (Boot sector).
 
 Windows Defender. 

* Сканування завантаження системи: виконує пряму перевірку файлів, що належать до завантажувального сектора Windows, на наявність вірусів і шкідливого програмного забезпечення.
 
* Повна перевірка: виконує пряму перевірку всієї системи на наявність вірусів. 

* Швидка перевірка: запускає швидку перевірку на віруси та шкідливі програми (основних частин системи) безпосередньо. 
 
* Сканування стиснутих файлів: безпосередньо активовує антивірус Windows для сканування стиснутих файлів (rar, zip, ace, tar тощо).
 
* Не сканувати стиснуті файли: вимикає антивірус Windows від сканування стиснутих файлів (rar, zip, ace, tar тощо).
* Список файлів на карантині в буфер обміну: копіює в буфер обміну список та інформацію про всі файли, які антивірус Windows помістив у карантин. 

* Вимкнути контроль облікових записів користувачів (uac): встановлює рівень контролю облікових записів користувачів на 0 (вимкнено).

## Параметри мультимедіа.

* Активувати веб-камеру: дозволяє за допомогою NVDA активувати веб-камеру, якщо вона у нас є (залишити її готовою до використання).

* Вимкнути веб-камеру: дозволяє нам за допомогою NVDA вимкнути веб-камеру, якщо вона у нас є (вимкнувши її, жодна програма не зможе її використовувати).

* Мікшер гучності: дозволяє нам зручно за допомогою NVDA відкривати мікшер гучності Windows. 
Ми можемо зробити це з меню TCA SystemUtilities, у розділі: "Мовлення і медіа", або призначити комбінацію клавіш.

* Відкрити параметри голосу: швидко відкриває параметри чи властивості перетворення тексту на мовлення (Text to Speech). Тут ми можемо обрати наш основний системний синтезатор мовлення. 
 
 * Відкрити параметри звуку: дозволяє безпосередньо відкрити параметри звуку в панелі керування (Звук, відтворення, Запис, комунікації). 
 


## Швидке відкриття деяких системних функцій:
* Відкрити оптимізацію дисків: дозволяє нам безпосередньо відкрити цю цікаву функцію Windows, щоб поліпшити продуктивність наших жорстких дисків. 
 
* Відкрити таблицю символів: безпосередньо відкриває цю цікаву функцію Windows. Це дозволяє нам вибирати і знати будь-який із знаків, цифр і літер, які існують в системі. 
Дуже корисно знати символи, які рідко зустрічаються або важко вводяться з клавіатури.
 
* Відкрити майстер збереження паролів користувачів: відкриває помічника цієї дуже корисної, але маловідомої утиліти Windows.
Він дозволяє нам зберігати облікові дані (імена, паролі тощо) облікових записів користувачів, які є в нашій системі. 
* Відкрити майстер передавання файлів BlueTooth: дозволяє нам безпосередньо запустити цього майстра для отримання чи надсилання файлів через наші пристрої BlueTooth. 
* Відкрити параметри папок: безпосередньо відкриває  цю часто використовувану функцію для керування провідником Windows, поданням папок, показом розширень файлів тощо. 
* Відкрити папку Roaming: безпосередньо відкриває папку Appdata>Roaming (тут розташована папка конфігурації NVDA і багатьох інших програм).
* Відкрити диспетчер дисків: дозволяє нам безпосередньо відкрити цю цікаву функцію для керування дисками, розділами та іншими пристроями зберігання, встановленими на нашому ПК.
 
* Відкрити майстер для збереження системного пароля: 
Відкриває цей корисний маловідомий майстер, який дозволяє нам зробити резервну копію пароля Windows, щоб мати можливість відновити його із зовнішнього пристрою.
 
* Відкрити монітор ресурсів: ми зможемо безпосередньо відкрити цей потужний, маловідомий інструмент Windows. Це як поліпшений диспетчер завдань, ми можемо керувати всіма службами, застосунками та процесами, запущеними в нашій системі.
Крім того, ми зможемо дізнатися, скільки оперативної пам’яті, сховища, мережі та іншого вони використовують.
 
* Відкрити диспетчер пристроїв: дозволяє відкрити цю корисну функцію Windows для керування обладнанням і драйверами комп’ютера.
 
* Дізнатися версію Windows: відкриється інформація з версією операційної системи. 
* Відкрити офіційний сайт з додатками: відкриває в основному браузері офіційний сайт, на якому можна отримати додатки для NVDA.

## Важлива примітка!

В діалозі «Налаштування» > «Жести вводу» можна призначити будь-які сполучення клавіш, згідно з вашими вподобаннями.

## Зміни у версії 0.10:
* Сумісність з NVDA 2025.1.
* Нова функція: Активувати план високої продуктивності (енергоспоживання Windows).
* Нова функція: Активувати план збалансованої продуктивності (енергоспоживання Windows).
* Нова функція: Запуск консолей.
* Виправлено функцію: Відкрити CMD у поточному шляху.
* Виправлено функцію: Очищення дисків.
* Виправлено функцію: Оптимізація дисків.
* Оптимізовано функції: вимкнення, перезавантаження та скасування вимкнення системи.

## Зміни у версії 0.9:
* Підтримка NVDA 2024.1.
* Нова функція Закриття процесів будь-якої активної програми.
* Оптимізована функція: GetPath, потрібна в Windows 11 23H2.
* Включає dll: pywintypes311.dll, сумісний з Python 3.11.
* Видалено початкові гарячі клавіші : вимкнення, перезавантаження та переривання вимкнення системи.

## Зміни у версії 0.8
* Починаючи з цієї версії TCA SystemUtilities змінює номенклатуру версій (для сумісності з NVDA 2023.3).
Тепер версії матимуть 3 цифри, це буде 0.8.2.
* Нова функція вимкнення контролю облікових записів користувачів (uac).
* Нова функція Увімкнення контролю облікових записів користувачів (uac).
* Функції увімкнення та вимкнення контролю облікових записів користувачів буде розташовано у меню TCA SystemUtilities у категорії: Безпека Windows;
Ви також зможете встановити для них комбінації клавіш за бажанням у розділі Жести вводу.

## Cambios en la versión 06:
* Nueva función interna para tomar la ruta del sistema (path), ahora son 2, en caso que falle una, TCA SystemUtilities intentará usar la otra.
(Una de las funciones ha sido desarrollada por: Héctor Benítez).
* Nueva función: Cerrar todos los procesos activos.
* Cerrar tareas que no están respondiendo en Windows.
* Corregido, el menú de TCA SystemUtilities ya no se repetirá si se recargan los complementos.
(Cortesía de Héctor Benítez).
* Corregido: ya no existen atajos de teclados predefinidos.


## Cambios en la versión 05.

* Nueva función para limpiar complementos y configuraciones en pantallas seguras.
* Nueva función borrar el portapapeles incluyendo el historial en Windows.
* Nueva función abrir el CMD en la ruta actual.
* Nueva función abrir el CMD con privilegios de administrador.
* Nueva función: Desactivar el almacenamiento reservado en Windows.
* Nueva función: activar el almacenamiento reservado en Windows.
* Corregida y optimizada función para obtener el objeto, con esto mejoran varias funciones como: copiar la ruta al portapapeles, copiar listado de archivos al portapapeles, ocultar o mostrar archivos y carpetas.


## Cambios en la versión: 04.

* Nueva función para entrar en la BIOS-UEFI del sistema (en el apartado : "Apagado del sistema").
* Se cambió el menú: "Sonido y voz", a: "Voz y multimedia".
* 2 Nuevas funciones en el apartado: "Voz y multimedia" (Activar/desactivar la webcam).
* Nueva función: "Limpiar caché DNS" (en el apartado Reparación y optimización").
* Restructuración de la documentación del complemento.
* Traducido al italiano.
* Compatible con NVDA 2022.

* Corrección de seguridad (sys.path.remove())


## Cambios en la versión 03:
* En esta versión TCA SystemUtilities es ya totalmente compatible con el nuevo sistema: Windows 11.
* Nuevo Menú: Seguridad de Windows 
con varias opciones referentes al antivirus de Windows.
* Otra opción en el menú: Apagado del sistema, la opción: "suspender el sistema".
* En esta versión el complemento está traducido a los idiomas: árabe, portugués (Portugal, portugués Brasil), y rumano.


## Cambios en la versión: 02.

* En esta versión el complemento cuenta con un cómodo Menú desde donde podemos ejecutar la mayoría de sus funcionalidades (no todas). 
El mismo se encuentra en el Menú: "Herramientas" de NVDA, y tiene el nombre del complemento: "TCA SystemUtilities".
* Se retiraron en esta versión todos los atajos prestablecidos, con lo que ahora deberéis asignar los atajos a cualquiera de las funciones, desde el menú: "Gestos de entrada" de NVDA.
* Mas funciones en los apartados: Apagado del sistema, Explorador de Windows, Sonido y voz, Reparación del sistema.
* Optimización de todo el código del complemento.

***

Código del proyecto en GitHub: 
[https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento](https://github.com/peterrc87/TCA-SystemUtilities-NVDA-Complemento)
