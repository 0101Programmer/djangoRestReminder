<h1>djangoRestReminder - приложение для напоминаний на фреймворке Django</h1>
<h1>Стек разработки:</h1>
<ul>
  <li>Django</li>
  <li>Django REST Framework</li>
  <li>HTML</li>
  <li>PostgreSQL</li>
  <li>Redis</li>
  <li>Docker</li>
</ul>
<h1>Описание проекта:</h1>
<p>Приложение представляет собой веб-интерфейс для создания заметок и напоминаний с возможностью прикреплять фотографии. Также присутствует страница личного кабинета, где можно обновить данные профиля, сменить аватар и продлить токен текущей сессии (авторизация в приложении основана на токенах). Через API можно осуществлять взаимодействие с базой данных напрямую: создавать, читать, обновлять и удалять из неё как заметки, так и пользователей.</p>

<h1>1. Процесс регистрации, создания пользователя</h1>

<p>
  Создать пользователя можно как через страницу регистрации,
  
  ![Снимок экрана 2025-02-10 185707](https://github.com/user-attachments/assets/f3106c17-a260-4d7c-92a4-a20468f1c2c1)

  так и через API
  
  ![Снимок экрана 2025-02-10 185749](https://github.com/user-attachments/assets/70a7086b-20ce-49ad-8e93-87c4ef97bbcd)
  
</p>

<h2>Создание пользователя через форму регистрации.</h2>

![Снимок экрана 2025-02-10 190146](https://github.com/user-attachments/assets/b95ca591-67c4-4e1f-a398-f4fe78e88762)

<p>Валидация также присутствует:</p>

<hr>

![Снимок экрана 2025-02-10 190152](https://github.com/user-attachments/assets/c4ef7552-d8b3-4418-a71e-0bd30b7566d2)

![Снимок экрана 2025-02-10 190201](https://github.com/user-attachments/assets/d672cc44-fac2-42c3-9244-829f1b34002d)

![Снимок экрана 2025-02-10 190214](https://github.com/user-attachments/assets/a055a129-1ad6-4376-ad3f-d3c6e3861456)

![Снимок экрана 2025-02-10 193629](https://github.com/user-attachments/assets/f7fba7e9-0bbb-4d2f-9911-5e9d4eb704bf)

![Снимок экрана 2025-02-10 193639](https://github.com/user-attachments/assets/e2ed92b3-f806-4d19-ab1b-7c20d18253f7)

![Снимок экрана 2025-02-10 193647](https://github.com/user-attachments/assets/ffd95d81-d7af-4a36-a193-9528346f19cc)

<hr>

<p>После заполнения формы без ошибок идёт переадресация на главную страницу (но уже для авторизованных пользователей).</p>

![Снимок экрана 2025-02-10 193657](https://github.com/user-attachments/assets/cbdb3bce-6e72-43da-8bce-78760abdfca7)

<p>В БД новый пользователь также появился</p>

![Снимок экрана 2025-02-10 193737](https://github.com/user-attachments/assets/fd4077cc-e049-44de-be5d-30366962214f)


<h2>Создание пользователя через API интерфейс</h2>

<p>Заполнение формы</p>

![Снимок экрана 2025-02-10 200027](https://github.com/user-attachments/assets/5671366e-8954-49e7-abe4-e068baa7ddc5)

<p>Пользователь создан</p>

![Снимок экрана 2025-02-10 200052](https://github.com/user-attachments/assets/b4cb1389-3ae7-4822-ab43-006a8e166bee)

<p>И теперь в базе данных два пользователя</p>

![Снимок экрана 2025-02-10 200447](https://github.com/user-attachments/assets/be0a61ea-605a-471f-99da-100c8b6d59a4)

<h1>2. Личный кабинет пользователя</h1>

<p>С главной страницы можно перейти в личный кабинет через навигационное меню.</p>

![Снимок экрана 2025-02-10 193712](https://github.com/user-attachments/assets/c7f93f80-f2f5-4512-97e4-e85d806c06a6)

![Снимок экрана 2025-02-10 193719](https://github.com/user-attachments/assets/6571f74f-6214-4e40-bc32-3de2a4e67835)

<p>Здесь можно изменить свои данные и «продлить жизнь токена», потому что если время выйдет — доступ будет запрещён.</p>

![Снимок экрана 2025-02-10 194146](https://github.com/user-attachments/assets/9bf21771-64cf-46cf-a695-9a82fbc067aa)

![Снимок экрана 2025-02-10 194254](https://github.com/user-attachments/assets/ecd6b4c0-0a07-40f5-8a0c-9d2124bbaa95)


<p>Работают токены через джанго-кеширование, для этого используется связка Docker-Redis.</p>

![capture_250210_210153](https://github.com/user-attachments/assets/ab30eb98-2efd-415a-a8ed-72572bf218b6)

![capture_250210_210234](https://github.com/user-attachments/assets/73083010-c05e-4ebf-87f0-2848bce86b27)


<p>К слову, теперь можно протестировать авторизацию.</p>

![Снимок экрана 2025-02-10 194330](https://github.com/user-attachments/assets/6389583a-4151-475a-847b-add976558cd6)

![Снимок экрана 2025-02-10 194352](https://github.com/user-attachments/assets/b5ef06a2-11bd-496f-ad29-6554e83dcb25)

<p>После возвращения в личный кабинет обновим срок истечения токена</p>

![Снимок экрана 2025-02-10 194404](https://github.com/user-attachments/assets/4fbdf4cc-a68f-405e-861a-f43384edc1e3)

<p>Теперь можно не опасаться, что доступ к странице будет внезапно прерван.</p>

![Снимок экрана 2025-02-10 194414](https://github.com/user-attachments/assets/e55159a4-e239-472a-a052-22a9a3dfb75a)

<p>
  
  Теперь можно обновить, например, имя
  <br><br>
  ![Снимок экрана 2025-02-10 202430](https://github.com/user-attachments/assets/d0118b74-722e-4a37-bb37-471965cb0a5a)
  ![Снимок экрана 2025-02-10 202447](https://github.com/user-attachments/assets/efd51c4c-1198-4a90-bae6-236f476ac7ed)
  ![Снимок экрана 2025-02-10 202453](https://github.com/user-attachments/assets/b89d8bc3-0878-4bab-832a-80498a1b1d0c)
  <br>
  Или фото профиля
  <br><br>
  ![Снимок экрана 2025-02-10 202756](https://github.com/user-attachments/assets/e98ce8e7-ce58-4f1b-8a1a-3a24ba191163)
  ![Снимок экрана 2025-02-10 202806](https://github.com/user-attachments/assets/966ece0a-35ac-4c64-a5ff-c5cb4c7f597b)
  ![Снимок экрана 2025-02-10 202818](https://github.com/user-attachments/assets/5396bf42-0796-4697-9be2-da7ee9f5e828)  
</p>


<h2>Изменение данных пользователя через API.</h2>

![Снимок экрана 2025-02-10 203220](https://github.com/user-attachments/assets/94c7e355-297e-47e8-aecd-8a35874213b8)

![Снимок экрана 2025-02-10 203227](https://github.com/user-attachments/assets/dd128e0d-ccc3-4b7f-a69a-c3492311682c)

![Снимок экрана 2025-02-10 203258](https://github.com/user-attachments/assets/e91aa640-df3e-4859-a716-87e782122add)

![Снимок экрана 2025-02-10 203307](https://github.com/user-attachments/assets/2a360b96-ceec-4d16-a4b1-b6ded9b6dad8)

![Снимок экрана 2025-02-10 203318](https://github.com/user-attachments/assets/604234c5-6f16-43cc-8596-b7c6824cac1d)

![Снимок экрана 2025-02-10 203330](https://github.com/user-attachments/assets/6f4ec6c9-3cc1-4bad-aecf-b14fb8a3cf0c)


<h1>3. Дашборд</h1>

<p>На этой странице представляется возможным поставить напоминание.</p>

![Снимок экрана 2025-02-10 204047](https://github.com/user-attachments/assets/cdc99e71-3960-4bbb-88b8-b607bd22fbd2)

![Снимок экрана 2025-02-10 204201](https://github.com/user-attachments/assets/ff37c337-c45b-462f-b24e-319422f02671)

![Снимок экрана 2025-02-10 204218](https://github.com/user-attachments/assets/e35db1cb-5623-42d7-b636-d9d4d4d919ba)

<p>Которое при наступлении даты, указанной в самом напоминании, отобразится на главной странице.</p>

![Снимок экрана 2025-02-10 204210](https://github.com/user-attachments/assets/40eee7b6-032b-466b-973c-73b43b999aed)

![Снимок экрана 2025-02-10 204224](https://github.com/user-attachments/assets/641ec890-9a3d-4898-951b-dc17a67af497)

<p>Если сменить статус на «выполнено», напоминание пропадёт с главной.</p>

![Снимок экрана 2025-02-10 204234](https://github.com/user-attachments/assets/e7fd67f7-49f2-45ab-8635-ab1d31e92929)

![Снимок экрана 2025-02-10 204238](https://github.com/user-attachments/assets/1722c7bd-6cf6-4cd1-bf73-b3e701cfbe57)

<p>Дашборд имеет фильтр по «выполненным» и «невыполненным» напоминаниям, постраничную пагинацию, возможность удаления заметок (и смены их статуса соответственно). Создадим ещё несколько напоминаний для демонстрации.</p>

<hr>

<p>Пагинация</p>

![Снимок экрана 2025-02-10 205148](https://github.com/user-attachments/assets/69b9d77c-d881-4620-89fe-00292bbaeede)

![Снимок экрана 2025-02-10 205155](https://github.com/user-attachments/assets/bfe9da3a-cadc-4008-80a7-5ec41a50744c)

<hr>

<p>Фильтрация</p>

![Снимок экрана 2025-02-10 205302](https://github.com/user-attachments/assets/b7d61a13-64c0-4a11-ad6b-01b2bd777e87)

![Снимок экрана 2025-02-10 205307](https://github.com/user-attachments/assets/fd550962-0210-494f-a717-e797a0b5dde6)

![Снимок экрана 2025-02-10 205313](https://github.com/user-attachments/assets/124a3d1c-304e-48cb-8b00-6239bd3fe046)

<hr>

<p>Смена статуса</p>

![Снимок экрана 2025-02-10 205409](https://github.com/user-attachments/assets/52653ddb-ecb2-4407-b03d-3c0109c029ed)

![Снимок экрана 2025-02-10 205418](https://github.com/user-attachments/assets/1c848d4a-c475-40c0-b328-da19ad86d246)

![Снимок экрана 2025-02-10 205425](https://github.com/user-attachments/assets/3b610e17-08b3-4ead-9cf5-6eb8fb8902ac)

<hr>

<p>Удаление</p>

![capture_250210_205553](https://github.com/user-attachments/assets/2abade5a-6370-410b-98c6-8ea6eb096267)

![capture_250210_205622](https://github.com/user-attachments/assets/45fbb2ee-e17d-4708-bd2d-aac114add897)

![Снимок экрана 2025-02-10 205636](https://github.com/user-attachments/assets/d9a46c6e-4710-4d07-95fb-6300577cd850)


<h2>Получение напоминаний через API.</h2>

<p>Кстати, привязываются заметки к пользователю через его forein key — UserID.</p>

![Снимок экрана 2025-02-10 210027](https://github.com/user-attachments/assets/a86c0ce9-233c-4f4b-b916-e9b33686c01d)

![Снимок экрана 2025-02-10 205855](https://github.com/user-attachments/assets/2d69315d-76cb-437a-9c4e-4f2424384185)

![Снимок экрана 2025-02-10 205903](https://github.com/user-attachments/assets/e036a76c-8a2c-4cd7-982b-23dd30d17f4c)

![Снимок экрана 2025-02-10 205910](https://github.com/user-attachments/assets/669f03bf-308a-437b-8a5d-0f799e3ce956)




