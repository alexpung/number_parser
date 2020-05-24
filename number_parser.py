import unicodedata


def parse_number(text):
    """ This function accept a string that starts with a number e.g. 3.9兆円
    It will read until a non-number is encountered, then stops e.g. 3.9兆円 will return 3900000000000.0
    ditching the '円'
    """
    text = text.replace(',', '')  # remove comma from number like 16,460千株
    text = text.replace(' ', '')  # remove space from number like 16 460千株
    leading_cursor = end_cursor = num = 0
    total = []
    while end_cursor < len(text):  # get number at the front until it reach a non-number
        try:
            num = float(text[leading_cursor:end_cursor + 1])
        except ValueError:  # if the digit is not a number check if it is a multiplier e.g. 兆/千
            if num != 0:  # guard against residue 0 stored in total
                total.append(num)
            try:
                multiplier = unicodedata.numeric(text[end_cursor])
                # to handle case like 1億千5百 where 千 without number in front stand for 1000
                if num == 0 and all(i > multiplier for i in total) and multiplier != 0:  # guard against 零 being added
                    total.append(multiplier)
                total = [multiply(x, num, multiplier) for x in total]
                leading_cursor = end_cursor + 1
            except ValueError:  # non value characters immediately end the calculation e.g. 円
                break
            num = 0
        end_cursor += 1
    total.append(num)
    return sum(total)


def multiply(n, numerical, multi):  # numerical is to handle case like 53643千円 which should be multiplied
    if multi > n or n == numerical:
        return n * multi
    else:
        return n
