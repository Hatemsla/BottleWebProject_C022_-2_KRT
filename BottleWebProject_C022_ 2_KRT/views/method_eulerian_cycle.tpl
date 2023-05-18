% rebase('layout.tpl', year=year, vertex_count=vertex_count, random=random, new_page=new_page, random_value=random_value)

<link rel="stylesheet" type="text/css" href="/static/content/euler_graph.css" />

<div class="background">
  <img class="back_image" src="/static/images/graph_wallpaper1.jpg" />
</div>

<div class="wrapper">
    <div class="info-container">
        <div class="theory-container">
            <h1>Поиск цикла Эйлера в Эйлеровом графе.</h1>
            <p>Например, заданный граф имеет эйлеров цикл, так как каждая вершина имеет четную степень. Граф является Эйлеровым и содержит следующий цикл Эйлера: 1 - 4 - 5 - 2 - 4 -3 - 2 - 1</p>
            <div>
                <img class="graph-image" src="/static/images/euler_graph_example.png">
            </div>
            <p class="graph-image-text">Рисунок 1 – Заданный граф.</p>
            <p>Программа выполняет следующие действия:
                <ul>
                    <li class="info-li">Определение является ли граф Эйлеровым;</li>
                    <li class="info-li">Поиск цикла Эйлера в заданном графе.</li>
                </ul>
            </p>
            <p><strong>Эйлеров граф</strong> - граф, в котором есть Эйлеров цикл.</p>
            <p><strong>Цикл Эйлера</strong>  - цикл, проходящий по каждому ребру ровно один раз. Эйлер доказал, что такой цикл существует тогда, и только тогда, когда все вершины в связанном графе имеют чётную степень.</p>
            <div>
                <img class="graph-image" width="600" src="/static/images/euler_graph_example2.png">
            </div>
            <p class="graph-image-text">Рисунок 2 – Цикл эйлера</p>
        </div>
        <div class="input-info-container">
            <h2>Входные данные</h2>
            <p>Форма ввода в качестве входных значений принимает 1 аргумент:
                <ol>
                    <li class="info-li"><strong>Количество вершин графа.</strong></li>
                </ol>
            </p>
            <p>
                Поля ввода ограничены диапазоном значений от 2 до 15 включительно, в случае ввода некорректных значений, будет выведено соответствующее сообщение.
            </p>
            <p>
                Также на форме присутствуют две кнопки:
                <ul>
                    <li class="info-li"><strong>Кнопка "Построить матрицу"</strong> - отвечает за построение таблицы смежности графа;</li>
                    <li class="info-li"><strong>Кнопка "Случайная матрица"</strong> - отвечает за построение матрицы смежности графа, заполнением ее случайными значениями, после чего матрицу смежности можно отредактировать.</li>
                </ul>
            </p>
            <p>После построения таблицы смежности графа, пользователь может самостоятельно заполнить таблицу данными.</p>
            <p>Поля матрицы представлены в виде элементов checkbox, которые могут быть в двух положениях. Нажаты - условное обозначение 1 в матрице. Отжаты - условное обозначение 0 в матрице. Допускается не симметричный ввод данных относительно главной диагонали.</p>
        </div>
        <div class="output-info-container">
            <h2>Выходные данные</h2>
            <p>
                В качестве выходных данных, будет выведено:
                <ol>
                    <li class="info-li"><strong>Нарисованный граф по введённой таблице смежности;</strong></li>
                    <li class="info-li"><strong>Сообщение о причастия графа к Эйлеровым;</strong></li>
                    <li class="info-li"><strong>Найденый цикл Эйлера (при наличии).</strong></li>
                </ol>
            </p>
        </div>
    </div>
    <div class="info-container">
        <div class="form-container">
            <form action="/euler_graph" method="post">
                <div class="form-input">
                    <label for="VERTEX">Введите количество вершин графа:</label>
                    <input type="number" name="VERTEX" id="VERTEX" value="{{vertex_count}}" required min="2" max="15" step=1 placeholder="Размер матрицы смежности графа" required>
                </div>
                <div class="form-buttons">
                    <button type="submit" name="form" value="matrix">Построить матрицу</button>
                    <button type="submit" name="form" value="random">Случайная матрица</button>
                </div>
            </form>
        </div>
        %if not new_page:
            <form action="/euler_graph_result" method="post">
                <div class="table-container">
                    <table name='adjacency-table' class="graph-table">
                        <caption>Таблица смежности графа</caption>
                        <thead>
                            <tr>
                                <th></th>
                                %for i in range(1, vertex_count + 1):
                                    <th>{{i}}</th>
                                %end
                            </tr>
                        </thead>
                        <tbody>
                            %for i in range(1, vertex_count + 1):
                                <tr>
                                    <th>{{i}}</th>
                                    %for j in range(1, vertex_count + 1):
                                        %if i == j:
                                            <td></td>
                                        %else:
                                            %if random_value:
                                                %if random.choice([0, 1]) == 1:
                                                    <td><input name='cell-{i}-{j}' class="checkbox-table" type='checkbox' checked></td>
                                                %else:
                                                    <td><input name='cell-{i}-{j}' class="checkbox-table" type='checkbox'></td>
                                                %end
                                            %else:
                                                <td><input name='cell-{i}-{j}' class="checkbox-table" type='checkbox'></td>
                                            %end
                                        %end
                                    %end
                                <tr>
                            %end
                        </tbody>
                    </table>
                    <div class="form-buttons">
                        <button type="submit" name="form" value="result">Найти цикл Эйлера</button>
                    </div>
                </div>
            </form>
        %end
    </div>
</div>