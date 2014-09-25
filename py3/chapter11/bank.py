
import os, pprint, sqlite3
from collections import namedtuple

def open_database(path='bank.db'):
    new = not os.path.exists(path)
    db = sqlite3.connect(path)
    if new:
        c = db.cursor()
        c.execute('CREATE TABLE payment (id INTEGER PRIMARY KEY,'
                  ' debit TEXT, credit TEXT, dollars INTEGER, message TEXT)')
        add_payment(db, '947', '101', 100, 'Paycheck')
        add_payment(db, '101', '330', 25, 'Blah')
        add_payment(db, '101', '330', 25, 'Blah')
        add_payment(db, '101', '205', 15, 'Gas money. Thanks for the ride!')
        db.commit()
    return db

def add_payment(db, debit, credit, dollars, message):
    db.cursor().execute(
        'INSERT INTO payment (debit, credit, dollars, message)'
        ' VALUES (?, ?, ?, ?)', (debit, credit, dollars, message))

def get_payments_of(db, account):
    c = db.cursor()
    c.execute('SELECT * FROM payment WHERE credit = ? or debit = ?',
              (account, account))
    RowTuple = namedtuple('Row', [tup[0] for tup in c.description])
    return [RowTuple(*row) for row in c.fetchall()]

if __name__ == '__main__':
    db = open_database()
    pprint.pprint(get_payments_of(db, '101'))
