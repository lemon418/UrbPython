def get_multiplied_digits(number):
        str_number = str(number)
        if len(str_number) > 1:
                first = str_number[0]
                a = (int(first))
                return a * get_multiplied_digits(int(str_number[1:]))
        else:
                if number == 0:
                        return 1
                else:
                        return number
result1 = get_multiplied_digits(402030)
result2 = get_multiplied_digits(40203)
print(result1)
print(result2)