import pyexcel
from collections import OrderedDict

data = [
    OrderedDict({
        'name': 'quan',
        'age':'22',
        'city':'hanoi'
    }),

    OrderedDict({
        'name': 'Hong',
        'age':'19',
        'city':'campuchia'
    }),

    OrderedDict({
        'name': 'an',
        'age':'18',
        'city':'laos'
    })
]

pyexcel.save_as(records=data, dest_file_name="asdfgh.xlsx")