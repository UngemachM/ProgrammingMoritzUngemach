import re

transactions=[]
def addToList(list,dic):
    list.append(dic)

def createDic(type,amount,date):
    return  dict( Type=type ,Amount=amount, Date=date)

def newTransaction(type,amount,date):
    addToList(transactions,createDic(type,amount,date))
    
newTransaction("sale",2000, "2024-01-14")
newTransaction("sale",3000, "2024-01-15")
#
#
#Alle Werte einer art ausgeben(bsp Amount)
#
#
transaction_type = transactions[0]["Type"]
transaction_amount = transactions[0]["Amount"]
transaction_date = transactions[0]["Date"]

def list_of(my_key):
    key_values = [transaction[my_key] for transaction in transactions]
    return key_values

# Beispielaufruf alle amounts ausgeben
print("Alle Amounts:")
print(list_of("Amount"))

#
#
#Date Validation
#
#


def is_valid_date_format(date):
    date_pattern = re.compile(r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$')
    return bool(date_pattern.match(date))

def validate_all_dates(lst):
    invalid_dates = []
    for transaction in lst:
        if "Date" in transaction and not is_valid_date_format(transaction["Date"]):
            invalid_dates.append(transaction["Date"])
    return invalid_dates
print("Datums mit RegEx Uberprüfen:")
print("Ungültige Datumsangaben:", validate_all_dates(transactions))





