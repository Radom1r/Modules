from application.salary import *
from application.db.people import *
import datetime
import PyHotKey

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.date.today())