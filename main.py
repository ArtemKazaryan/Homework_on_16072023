import os

from preform import all_items, sales_by_salesman, max_value, min_value, max_sale_by_salesman, min_sale_by_salesman, \
    max_sale_by_customers, min_sale_by_customers, max_sale_by_all_salesmen, min_sale_by_all_salesmen, \
    max_sale_by_all_customers, avg_sale_by_customers, avg_sale_by_salesman, key_request, update_sale, update_customers,\
    update_salesman, insert_table, delete_entry
from models.database import DATABASE_NAME
import create_database as db_creator

from models.models import Sales, Salesmen, Customers


def main():
    while (query := input('Выберите команду для выполнения\n'
                          '1. Примеры запросов\n'
                          '2. CREATE, INSERT, DELETE\n'
                          '0. Выход\n: ')) != '0':
        match query:
            case '1':
                while (request := input('Выберите команду для выполнения\n'
                                        '1. Отображение всех сделок\n'
                                        '2. Отображение сделок конкретного продавца\n'
                                        '3. Отображение максимальной по сумме сделки\n'
                                        '4. Отображение минимальной по сумме сделки\n'
                                        '5. Отображение максимальной по сумме сделки для конкретного продавца\n'
                                        '6. Отображение минимальной по сумме сделки для конкретного продавца\n'
                                        '7. Отображение максимальной по сумме сделки для конкретного покупателя\n'
                                        '8. Отображение минимальной по сумме сделки для конкретного покупателя\n'
                                        '9. Отображение продавца, у которого максимальная сумма продаж по всем сделкам\n'
                                        '10. Отображение продавца, у которого минимальная сумма продаж по всем сделкам\n'
                                        '11. Отображение покупателя, у которого максимальная сумма покупок по всем сделкам\n'
                                        '12. Отображение средней суммы покупки для конкретного покупателя\n'
                                        '13. Отображение средней суммы покупки для конкретного продавца\n'
                                        '0. Выход\n: ')) != '0':
                    match request:
                        case '1':
                            db_query = all_items(Sales)
                            [print(i) for i in db_query]
                        case '2':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Выберите id продавца\n: ')
                            db_query = sales_by_salesman(int(id_inp))
                            for row in db_query:
                                date, amount, customer_name, salesman_name = row
                                print(
                                    f"Дата: {date.strftime('%d.%m.%Y')}, Сумма: {amount}, Покупатель: {customer_name},"
                                    f" Продавец: {salesman_name}")
                        case '3':
                            db_query = max_value()[0]
                            print(f'id: {db_query[0]}, максимальная сумма: {db_query[1]}')
                        case '4':
                            db_query = min_value()[0]
                            print(f'id: {db_query[0]}, минимальная сумма: {db_query[1]}')
                        case '5':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Выберите id продавца\n: ')
                            query = max_sale_by_salesman(id_inp)
                            print(query)
                        case '6':
                            all_seller = all_items(Salesmen)
                            [print(i.id, i.name) for i in all_seller]
                            id_inp = input('Выберите id продавца\n: ')
                            query = min_sale_by_salesman(id_inp)
                            print(query)
                        case '7':
                            all_bayer = all_items(Customers)
                            [print(i.id, i.name) for i in all_bayer]
                            id_inp = input('Выберите id покупателя\n: ')
                            query = max_sale_by_customers(id_inp)
                            print(query)
                        case '8':
                            all_bayer = all_items(Customers)
                            [print(i.id, i.name) for i in all_bayer]
                            id_inp = input('Выберите id покупателя\n: ')
                            query = min_sale_by_customers(id_inp)
                            print(query)
                        case '9':
                            print(max_sale_by_all_salesmen())
                        case '10':
                            print(min_sale_by_all_salesmen())
                        case '11':
                            print(max_sale_by_all_customers())
                        case '12':
                            print(avg_sale_by_customers())
                        case '13':
                            print(avg_sale_by_salesman())

                        case _:
                            print('Такой команды не существует.')
                else:
                    print('Выход в главное меню')
            case '2':
                while (request := input('Выберите команду для выполнения\n'
                                        '1. Обновить запись в таблице Sales\n'
                                        '2. Обновить запись в таблице Customers\n'
                                        '3. Обновить запись в таблице Salesmen\n'
                                        '4. Добавьте новую запись в таблицу Sales\n'
                                        '4. Добавьте новую запись в таблицу Customers\n'
                                        '6. Добавьте новую запись в таблицу Salesmen\n'
                                        '7. Удалить запись из таблицы Sales\n'
                                        '8. Удалить запись из таблицы Customers\n'
                                        '9. Удалить запись из таблицы Salesmen\n'
                                        '0. Выход\n: ')) != '0':
                    match request:
                        case '1':
                            sale_query = all_items(Sales)
                            [print(i) for i in sale_query]
                            sale_id = int(input("Введите id продажи, который необходимо обновить: "))
                            sale = key_request(Sales, sale_id)
                            if sale:
                                salesmen_query = all_items(Salesmen)
                                [print(i) for i in salesmen_query]
                                salesman_id = int(input("Введите новый id продавца: "))
                                customer_query = all_items(Customers)
                                [print(i) for i in customer_query]
                                customer_id = int(input("Введите новый id покупателя: "))
                                amount = int(input("Введите новую сумму продаж: "))
                                update_sale(sale_id, salesman_id, customer_id, amount)

                            else:
                                print("Продажа с этим id не найдена")
                        case '2':
                            customer_query = all_items(Customers)
                            [print(i) for i in customer_query]
                            customers_id = int(input("Введите id клиентов, которые будут обновлены: "))
                            customer = key_request(Customers, customers_id)
                            if customer:
                                name = input('Введите новое имя покупателя')
                                update_customers(customers_id, name)
                            else:
                                print("Продажа с этим id не найдена")

                        case '3':
                            salesmen_query = all_items(Salesmen)
                            [print(i) for i in salesmen_query]
                            salesmen_id = int(input("Введите идентификатор продавца, который необходимо обновить: "))
                            salesmen = key_request(Salesmen, salesmen_id)
                            if salesmen:
                                name = int(input("Введите новый id продавца: "))
                                update_salesman(salesmen_id, name)
                            else:
                                print("Продажа с этим id не найдена")
                        case '4':
                            date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
                            salesman_id = input("Введите id продавца: ")
                            customer_id = input("Введите id покупателя: ")
                            amount = input("Введите сумму продажи: ")
                            sale = Sales(date=date, salesman_id=salesman_id,
                                         customer_id=customer_id, amount=amount)
                            insert_table(sale)
                        case '5':
                            name = input("Введите имя покупателя: ")
                            buyer = Customers(name=name)
                            insert_table(buyer)
                        case '6':
                            name = input("Введите имя продавца: ")
                            salesmen = Salesmen(name=name)
                            insert_table(salesmen)
                        case '7':
                            sale_id = int(input("Введите id продавца: "))
                            sale = key_request(Sales, sale_id)
                            if sale:
                                delete_entry(sale)
                            else:
                                print("Продажа с этим id не найдена")

                        case '8':
                            buyer_id = int(input("Продажа с этим id не найдена: "))
                            buyer = key_request(Customers, buyer_id)
                            if buyer:
                                delete_entry(buyer_id)
                            else:
                                print("Продажа с этим id не найдена")
                        case '9':
                            seller_id = int(input("Введите id продавца: "))
                            buyer = key_request(Salesmen, seller_id)
                            if buyer:
                                delete_entry(seller_id)
                            else:
                                print("Продажа с этим id не найдена")
                        case _:
                            print('Такой команды не существует.')
                else:
                    print('Выход в главное меню')
            case _:
                print('Такой команды не существует.')
    else:
        print('Завершение программы')


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
        print('CREATE:', DATABASE_NAME)
    else:
        print(DATABASE_NAME, 'exists')

    main()