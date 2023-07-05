from application.db.people import get_employees
from application.salary import calculate_salary
import datetime
import PyHotKey

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.date.today())