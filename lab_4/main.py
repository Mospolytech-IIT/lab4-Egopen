'Основной блок'
from zd_4_1 import checkemail,checkpassword
from zd_4_2 import login
from zd_4_3 import get_flower_price
from zd_4_4 import get_flowers_price,add_to_stock, calculate_order_cost
from zd_4_5 import place_order
from zd_4_6n7 import plc_order
def call_all_func():
    '''Вызывает все функции'''
    try:
        checkemail("eg@gmial.com")
    except Exception as ex:
        print(ex)
    try:
        checkpassword("1244567")
    except Exception as ex:
        print(ex)
    if login("eg@gmail.com", "12345678"):
        print("вы успешно зашли")
    get_flower_price("rose",10)
    get_flowers_price("Fdsf",12312)
    add_to_stock(10,500)
    print(calculate_order_cost({"rose":1}))
    place_order("rose",40)
    plc_order("ewf","sdf")

if __name__=="__main__":
    call_all_func()
