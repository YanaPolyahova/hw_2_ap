from hw_ap2.re import correction_len, filling_new_phonebook
import csv

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    correction_len(contacts_list)  # Приведение входящего массива к единому виду.
    updated_contacts_list = filling_new_phonebook(contacts_list)  # создание нового массива из входящего с
                                                                  # учетом требований

    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      datawriter.writerows(updated_contacts_list)
