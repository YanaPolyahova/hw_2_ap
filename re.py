import re


def correction_len(contact_list):
    for row in contact_list:
        if len(row) > 7:
            for ind_number in range(7, len(row)):
                if row[ind_number] == '':
                    row.pop(ind_number)
                else:
                    pass


def name_checking(contacts_list=list[0:3]):
    new_list = []
    for element in contacts_list:
        if len(element.split()) == 3:
            for sep_element in element.split():
                new_list.append(sep_element)
        elif len(element.split()) == 2:
            for sep_element in element.split():
                new_list.append(sep_element)
        elif len(element.split()) == 1:
            new_list.append(element)
        elif len(element.split()) == 0:
            new_list.append('None')
    return new_list[:3]


def organization_checking(contact_list):
    if 'ФНС' in contact_list or '@nalog.ru' in contact_list:
        return 'ФНС'
    if 'Минфин' in contact_list or '@minfin.ru' in contact_list:
        return 'Минфин'
    else:
        return 'None'


def position_checking(contact_list):
    for element in contact_list:
        if len(element.split()) > 3 and all(re.match(r'[а-яА-ЯёЁcC –]', i) for i in element):
            return element
        return 'None'


def phone_checking(contact_list):
    pattern = r'(\+7|\b8)(\s*\(\s*|\s)?(\d{3})(\)\s|\-|\))?(\d{3})\-?(\d{2})\-?(\d{2})(\s\(|\s)?(\доб\.)?\s?(\d{4})?\)?'
    substitution = r'+7(\3)\5\6\7 \9\10'
    result = re.sub(pattern, substitution, contact_list)
    if result:
        return result
    return 'None'


def email_checking(contact_list):
    if '@' in contact_list:
        return contact_list
    return 'None'


def values_consolidation(first_value, new_value):
    for element in range(len(first_value)):
        if first_value[element] == 'None':
            first_value[element] = new_value[element]
    return first_value


def filling_new_phonebook(contact_list):
    new_list = {}
    for i in contact_list[1:]:
        filled_row = []
        full_name = name_checking(i[:3])
        filled_row.append(full_name[0])
        filled_row.append(full_name[1])
        filled_row.append(full_name[2])
        filled_row.append(organization_checking(i[3:]))
        filled_row.append(position_checking(i[4:]))
        filled_row.append(phone_checking(i[5]))
        filled_row.append(email_checking(i[6]))
        if full_name[0] not in new_list:
            new_list[full_name[0]] = filled_row
            pass
        elif full_name[0] in new_list:
            new_list[full_name[0]] = values_consolidation(new_list[full_name[0]], filled_row)
    result = [['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']]
    for key, value in new_list.items():
        result.append(value)
    return result
