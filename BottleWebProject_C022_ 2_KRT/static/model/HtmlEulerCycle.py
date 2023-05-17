import random
from bottle import request
from static.classes.EulerGraph import EulerGraph
from datetime import date



class HtmlEulerCycle:
    """Класс формирующий html страницу для поиска цикла Эйлера"""


    site_header = '''
    % rebase('layout.tpl', year=%s)\n''' 

    beginning_body = '''
    <h1>Матрица смежности</h1>
    <form action="/matrix" method="post">
        <p><input type="number" size="50" name="VERTEX" value=%s min=1 max=15 step=1 placeholder="Количество вершин" 
        required></p>
        <p><input type="submit" value="Создать матрицу"></p>
    </form>\n''' 

    random_form = '''<form action="/random" method="post">
        <input type="hidden" name="SHARED_TEXT" value=%s>
        <p><input type="submit" value="Заполнить случайно"></p>
    </form>\n'''

    find_form = '''<form action="/result" method="post">
        <input type="hidden" name="SHARED_TEXT" value=%s>
        <p><input type="submit" value="Найти Эйлеров цикл"></p>
        %s
    </form>\n'''

    method_description = '''<h1>Описание метода</h1>\n'''

    result_form = '''<div">
        <p>%s</p>
        <p>%s</p>
    </div>\n'''

    end_site = ''''''
    
    # Метод формирования новой страницы 
    @staticmethod
    def new_page_command():
        return HtmlEulerCycle.site_header + \
            HtmlEulerCycle.method_description + \
            HtmlEulerCycle.beginning_body % 1 + HtmlEulerCycle.random_form % 1 + \
            HtmlEulerCycle.find_form % (1, '') + HtmlEulerCycle.end_site

    # Метод формирования страницы и создание матрицы смежности
    @staticmethod
    def create_matrix_command(vertex_count, random_value):
        return HtmlEulerCycle.site_header + HtmlEulerCycle.method_description + \
            HtmlEulerCycle.beginning_body % vertex_count + HtmlEulerCycle.random_form % vertex_count + \
            HtmlEulerCycle.find_form % (vertex_count, HtmlEulerCycle.create_matrix(vertex_count, random_value)) + \
            HtmlEulerCycle.end_site

    # Метод формирования страницы и выполнение поиска цикла эйлера
    @staticmethod
    def find_euler_cycle_command(vertex_count):
        return HtmlEulerCycle.site_header + HtmlEulerCycle.method_description + \
            HtmlEulerCycle.beginning_body % vertex_count + HtmlEulerCycle.random_form % vertex_count + \
            HtmlEulerCycle.create_result(vertex_count) + \
            HtmlEulerCycle.end_site
    
    # Метод формирования результато поиска цикла эйлера
    @staticmethod
    def create_result(vertex_count):
        checkbox_values = EulerGraph.make_adjacency_matrix_symmetric(HtmlEulerCycle.read_matrix_from_page(vertex_count))

        page = HtmlEulerCycle.find_form % (vertex_count,
                                           HtmlEulerCycle.adjacency_matrix_to_html_table(vertex_count,
                                                                                         checkbox_values))

        existence, euler_cycle = EulerGraph.find_euler_cycle(checkbox_values)

        if existence:
            return page + HtmlEulerCycle.result_form % ('Цикл существует', euler_cycle)
        else:
            return page + HtmlEulerCycle.result_form % ('Цикл отсутствует', euler_cycle)

    # Метод получения матрицы смежности со страницы HTML
    @staticmethod
    def read_matrix_from_page(vertex_count):
        checkbox_values = []
        for i in range(1, vertex_count + 1):
            row = []
            for j in range(1, vertex_count + 1):
                if i == j:
                    row.append(0)
                    continue
                check_name = f'cell-{i}-{j}'
                if check_name in request.forms:
                    row.append(1)
                else:
                    row.append(0)
            checkbox_values.append(row)
        return checkbox_values

    # Создание html разметки новой матрицы смежности
    @staticmethod
    def create_matrix(vertex_count, random_value):
        # Создание заголовка таблицы
        header_row = "<tr><th></th>"
        for i in range(1, vertex_count + 1):
            header_row += f"<th>{i}</th>"
        header_row += "</tr>"

        table = "<table name='adjacency-table'>" + header_row

        # Создание строк таблицы
        for i in range(1, vertex_count + 1):
            # Ячейка с номером вершины
            row = "<tr>" + f"<th>{i}</th>"

            # Ячейки с флажками
            for j in range(1, vertex_count + 1):
                if i == j:
                    row += "<td></td>"
                else:
                    if random_value == 1:
                        if random.choice([0, 1]) == 1:
                            row += f"<td><input name='cell-{i}-{j}' type='checkbox' checked></td>"
                        else:
                            row += f"<td><input name='cell-{i}-{j}' type='checkbox'></td>"
                    else:
                        row += f"<td><input name='cell-{i}-{j}' type='checkbox'></td>"
            table += row + "</tr>"
        return table + "</table>"

    # Создание html разметки существующей матрицы смежности
    @staticmethod
    def adjacency_matrix_to_html_table(vertex_count, adj_matrix):
        header_row = "<tr><th></th>"
        for i in range(1, vertex_count + 1):
            header_row += f"<th>{i}</th>"
        header_row += "</tr>"

        table = "<table name='adjacency-table'>" + header_row

        # Создание строк таблицы
        for i in range(1, vertex_count + 1):
            row = "<tr>"

            # Ячейка с номером вершины
            row += f"<th>{i}</th>"

            # Ячейки с флажками
            for j in range(1, vertex_count + 1):
                if i == j:
                    row += "<td></td>"
                else:
                    if adj_matrix[i - 1][j - 1] == 1:
                        row += f"<td><input name='cell-{i}-{j}' type='checkbox' checked></td>"
                    else:
                        row += f"<td><input name='cell-{i}-{j}' type='checkbox'></td>"

            table += row + "</tr>"
        return table + "</table>"

