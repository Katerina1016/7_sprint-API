class OrderData:
    data = {
        'firstname': "Олег",
        'lastname': 'Антонов',
        'address': 'г. Москва, ул. Главная, 8',
        'metroStation': 2,
        'phone': '+7 922 222 22 00',
        'rentTime': 3,
        'deliveryDate': '2024-07-10',
        'comment': 'Быстрей!'
    }


class TextResponse:
    response_successful_operation = '{"ok":true}'
    reusing_the_login = 'Этот логин уже используется'
    response_insufficient_data = 'Недостаточно данных для создания учетной записи'
    response_not_courier_id = 'Курьера с таким id нет'
    null_id_deletion = 'invalid input syntax'
    track_in_order_list = "track"
    profile_not_found_response = 'Учетная запись не найдена'
    insufficient_login_data_response = 'Недостаточно данных для входа'