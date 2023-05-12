

if __name__ == '__main__':
    reports = []
    for i in range(1, 5):
        with open(f'reports/report_{i}.txt') as report_f:
            reports.append(report_f.read())
    with open(f'reports/report_year.txt') as result_f:
        report_year = result_f.read()
    if ''.join(reports) == report_year or '\n'.join(reports) == report_year:
        print('Отчёт сформирован успешно')
    else:
        print('Отчёт составлен неправильно')
