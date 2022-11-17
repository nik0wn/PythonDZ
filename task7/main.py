from os.path import exists
from txtandcsv import txt_fail
from txtandcsv import csv_fail
from Person_cvs import csv_new
fail = 'person.csv'
temp = exists(fail)
if not temp:
    csv_new()
csv_fail()
txt_fail()