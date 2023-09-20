from PyInquirer import prompt
import csv
import json

choices = []
new_list = []

def get_users():
    with open('users.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for line in f:
            choices.append(line.strip())
    return choices


def convert_list():
    for l in choices:
        elt = {'name': l }
        new_list.append(elt)
    return new_list


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": choices,
    },
]

user_questions = [
    {
        "type":"input",
        "name":"username",
        "message":"New User - Name: ",
    },
]

def new_expense(*args):
    get_users()
    infos = prompt(expense_questions)

    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯

    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([{'amount': infos['amount']}, {'label': infos['label']}, {'spender': infos['spender']}])
        print("Expense Added !")
    return True

def create_user(*args):
    infos = prompt(user_questions)
    print("User created!")
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos['username']])
    return True

