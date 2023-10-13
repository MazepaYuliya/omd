"""Модуль для работы с данными департаментов"""
import csv
import datetime
import os
from typing import Dict, List, Set, Tuple, Union
from rich.console import Console
from rich.table import Table
from rich.tree import Tree


DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = f'{DIR_PATH}/Corp_Summary.csv'
REPORT_PATH = f'{DIR_PATH}/reports/'


def get_department_hierarchy() -> List[Tuple[str, Set[str]]]:
    """
    Функция для получения иерархии департаментов
    :return: список кортежей вида ('Департамент', {'Отдел 1', 'Отдел 2', ...})
    """
    departments_structure = {}
    with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        for row in csvreader:
            data_list = row[0].split(';')
            department = data_list[1]
            team = data_list[2]
            departments_structure.setdefault(department, set())
            departments_structure[department].add(team)

    return sorted(departments_structure.items())


def print_department_hierarchy() -> None:
    """Функция для вывода иерахии департаментов в консоль"""
    departments_set = get_department_hierarchy()

    console = Console()
    tree = Tree('[green][bold]Структура департаментов[/bold][/green]')
    for department_data in departments_set:
        subtree = tree.add(f'[blue]{department_data[0]}[/blue]')
        for subdepartment in sorted(department_data[1]):
            subtree.add(f'[purple]{subdepartment}[/purple]')
    console.print(tree)


def get_report() -> List[Dict[str, Union[str, int]]]:
    """
    Функция для получения сводного отчета по департаментам
    :return: список словарей со сводными данными каждого департамента
    """
    departments = {}
    with open(DATA_PATH, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        for row in csvreader:
            data_list = row[0].split(';')
            department = data_list[1]
            salary = int(data_list[5])
            departments.setdefault(department, {'count': 0, 'salaries': []})
            departments[department]['count'] += 1
            departments[department]['salaries'].append(salary)

    report = [
        {
            'department': department,
            'count': data['count'],
            'min_salary': min(data['salaries']),
            'max_salary': max(data['salaries']),
            'mean_salary': int(sum(data['salaries'])/len(data['salaries'])),
        }
        for department, data
        in departments.items()
    ]

    return sorted(report, key=lambda x: x['department'])


def print_report() -> None:
    """Функция для вывода сводного отчета в консоль"""
    report = get_report()

    table = Table(title='Сводный отчет')
    for fieldname in report[0].keys():
        table.add_column(fieldname, style='bold')

    for row in report:
        table.add_row(*[str(value) for value in row.values()])

    console = Console()
    console.print(table)


def save_report() -> None:
    """Функция для сохранения сводного отчета в файл"""
    report = get_report()
    current_date = datetime.datetime.now()
    current_date_str = datetime.datetime.strftime(current_date, '%Y-%m-%d')
    file_name = f'report {current_date_str}.csv'
    file_path = f'{REPORT_PATH}/{file_name}'
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=report[0].keys())
        csvwriter.writeheader()
        csvwriter.writerows(report)

    print(f'Сохранен файл {file_name}')


if __name__ == '__main__':
    cases = {
        '1': 'Вывести иерархию команд',
        '2': 'Вывести сводный отчёт по департаментам',
        '3': 'Сохранить сводный отчёт'
    }
    option = None
    while option not in cases:
        option_list = ['. '.join(item) for item in cases.items()]
        print(f'Выберите пункт меню:\n{" ".join(option_list)}')
        option = input()
    if option == '1':
        print_department_hierarchy()
    elif option == '2':
        print_report()
    else:
        save_report()
