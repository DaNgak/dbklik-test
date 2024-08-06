def is_first_come_first_serve(take_out_orders, dine_in_orders, served_orders):
    take_out_index = 0
    dine_in_index = 0
    take_out_length = len(take_out_orders)
    dine_in_length = len(dine_in_orders)

    for order in served_orders:
        if take_out_index < take_out_length and order == take_out_orders[take_out_index]:
            take_out_index += 1
        elif dine_in_index < dine_in_length and order == dine_in_orders[dine_in_index]:
            dine_in_index += 1
        else:
            return False

    if take_out_index != take_out_length or dine_in_index != dine_in_length:
        return False

    return True

# Contoh penggunaan case 1
take_out_orders1 = [1, 3, 5]
dine_in_orders1 = [2, 4, 6]
served_orders1 = [1, 2, 4, 6, 5, 3]
result_case1 = is_first_come_first_serve(take_out_orders1, dine_in_orders1, served_orders1)
print("Benar" if result_case1 else "Salah") 

# Contoh penggunaan case 2
take_out_orders2 = [17, 8, 24]
dine_in_orders2 = [12, 19, 2]
served_orders2 = [17, 8, 12, 19, 24, 2]
result_case2 = is_first_come_first_serve(take_out_orders2, dine_in_orders2, served_orders2)
print("Benar" if result_case2 else "Salah") 
