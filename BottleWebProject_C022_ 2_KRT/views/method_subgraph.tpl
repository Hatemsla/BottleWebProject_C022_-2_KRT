% rebase('layout.tpl', graph_count=graph_count, year=year, subgraph_count=subgraph_count, graph_data=graph_data, cliques=cliques, num_cliques=num_cliques, main_graph=main_graph, subgraphs=subgraphs, is_valid_graph=is_valid_graph, is_subgraph_draw=is_subgraph_draw, is_build_matrix=is_build_matrix)

<link rel="stylesheet" type="text/css" href="/static/content/method_subgraph.css" />

<div class="background">
  <img class="back_image" src="/static/images/graph_wallpaper1.jpg" />
</div>

<div class="wrapper">
    <div class="info-container">
        <div class="theory-container">
            <h1>Нахождение заданной клики в заданном графе</h1>
            <p>Например, заданная клика представляет собой полный граф из пяти вершин, степень каждой из которых равна четырем. На рисунке 1 представлены диаграмма подграфа и соответствующая ему матрица смежности вершин.</p>
            <div>
                <img class="graph-image" src="/static/images/subgraph_image.png">
            </div>
            <p class="graph-image-text">Рисунок 1 – Заданный фрагмент и его матрица смежности</p>
            <p>Программа выполняет следующие действия:
                <ul>
                    <li class="info-li">Поиск всех имеющихся заданных клик в заданном графе;</li>
                    <li class="info-li">Вывод всех найденных клик в виде списка вершин и построенного графа с выделением найденной клики.</li>
                </ul>
            </p>
            <p><strong>Кликой</strong> неориентированного графа называется подмножество его вершин, любые две из которых соединены ребром.</p>
            <p><strong>Главной диагональю</strong> квадратной матрицы называют элементы, имеющие одинаковые индексы, то есть те элементы, у которых номер строки совпадает с номером столбца.</p>
            <p>В таблице смежности, у неориентированного графа, единицы симметричны относительно главной диагонали.</p>
            <div>
                <img class="graph-image" src="/static/images/main_diagonal.png">
            </div>
            <p class="graph-image-text">Рисунок 2 – Главная диагональ на матрице</p>
        </div>
        <div class="input-info-container">
            <h2>Входные данные</h2>
            <p>Форма ввода в качестве входных значений принимает 3 параметра: 
                <ol>
                    <li class="info-li"><strong>Количество вершин графа;</strong></li>
                    <li class="info-li"><strong>Размер клики;</strong></li>
                    <li class="info-li"><strong>Флаг отрисовки найденных клик в графе.</strong></li>
                </ol>
            </p>
            <p>
                Поля ввода ограничены диапазоном значений от 2 до 20 включительно, в случае ввода некорректных значений, будет выведено соответствующее сообщение.
            </p>
            <p>
                Также на форме присутствуют две кнопки:
                <ul>
                    <li class="info-li"><strong>Кнопка "Построить матрицу"</strong> - отвечает за построение таблицы смежности графа;</li>
                    <li class="info-li"><strong>Кнопка "Случайная матрица"</strong> - отвечает за построение матрицы смежности графа, заполнением ее случайными значениями от 0 до 1 и нахождением клики в графе.</li>
                </ul>
            </p>
            <p>После построения таблицы смежности графа, пользователь может самостоятельно заполнить таблицу данными.</p>
            <p>Поля ввода таблицы смежности ограничены в вводе, можно ввести только 0 или 1, также данные должны быть симметричными относительно главной диагонали, так как граф неориентированный. В случае ввода некорректных значений будет выведено соответствующее сообщение.</p>
        </div>
        <div class="output-info-container">
            <h2>Выходные данные</h2>
            <p>
                В качестве выходных данных, будет выведено:
                <ol>
                    <li class="info-li"><strong>Нарисованный граф;</strong></li>
                    <li class="info-li"><strong>Выделенные найденные клики в графе (если выбран флаг отрисовки);</strong></li>
                    <li class="info-li"><strong>Список с найденными кликами.</strong></li>
                </ol> 
            </p>
        </div>
    </div>
    <div class="info-container">
        <div class="form-container">
            <form action="/method_subgraph" method="post">
                <div class="form-input">
                    <label for="graph_count">Введите количество вершин графа:</label>
                    <input type="number" id="graph_count" value="{{graph_count}}" required min="2" max="20" pattern="[0-9]+" name="graph_count" placeholder="Размер матрицы смежности графа">
                </div>
                <div class="form-input">
                    <label for="subgraph_count">Введите размер клики:</label>
                    <input type="number" id="subgraph_count" value="{{subgraph_count}}" required min="2" max="20" pattern="[0-9]+" name="subgraph_count" placeholder="Размер клики">
                </div>
                <div class="form-input">
                    <label for="subgraph_count">Рисовать найденные клики:</label>
                    %if is_subgraph_draw:
                        <input type="checkbox" id="subgraph_count" name="is_subgraph_draw" checked>
                    %else:
                        <input type="checkbox" id="subgraph_count" name="is_subgraph_draw">
                    %end
                </div>
                <div class="form-buttons">
                    <button class="btn" type="submit" name="form" value="Send1">Построить матрицу</button>
                    <button class="btn" type="submit" name="form" value="Random">Случайная матрица</button>
                </div>
            </form>
        </div>
        %if int(graph_count) > 0:
            <div class="table-container">
                <form action="/method_subgraph" method="post">
                    <table name="graph_data" class="graph-table">
                        <caption>Таблица смежности графа</caption>
                        <thead>
                            <tr>
                                <th></th>
                                %for i in range(int(graph_count)):
                                    <th>{{i+1}}</th>
                                %end
                            </tr>
                        </thead>
                        <tbody>
                            %for i in range(int(graph_count)):
                                <tr>
                                    <th>{{i+1}}</th>
                                    %for j in range(int(graph_count)):
                                        %if graph_data:
                                            %if graph_data[i][j] == 0:
                                                <td style="background-color: #d97676;"><input style="background-color: #d97676;" type="number" name="{{i}}{{j}}g" value="{{graph_data[i][j]}}" required min="0" max="1" pattern="[01]" maxlength="1"></td>
                                            %else:
                                                <td style="background-color: #78d975;"><input style="background-color: #78d975;" type="number" name="{{i}}{{j}}g" value="{{graph_data[i][j]}}" required min="0" max="1" pattern="[01]" maxlength="1"></td>
                                            %end
                                        %else:
                                            <td style="background-color: #d97676;"><input style="background-color: #d97676;" type="number" name="{{i}}{{j}}g" value="0" required min="0" max="1" pattern="[01]" maxlength="1"></td>
                                        %end
                                    %end
                                </tr>
                            %end
                        </tbody>
                    </table>
                    <p class="confirm"><button class="btn" type="submit" name="form" value="Confirm">Посчитать</button></p>
                </form>  
            </div>
        %end
        %if not is_valid_graph and not is_build_matrix:
            <p class="error">Граф заполнен неверно</p>
        %end
    </div>
    %if is_valid_graph:
        <div class="info-container">
            <div class="result-container">
                <div class="graph-container">
                    <div class="main_graph">
                        <img src="data:image/png;base64,{{ main_graph }}"/>
                    </div>
                    <p>Рисунок 3 - Нарисованный граф</p>
                </div>
                %if num_cliques > 0:
                    %if is_subgraph_draw:
                        <div id="myCarousel" class="carousel slide" data-ride="carousel">
                            <div class="carousel-inner" role="listbox">
                                %for i in range(num_cliques):
                                    %if i == 0:
                                        <div class="item active">
                                            <img src="data:image/png;base64,{{ subgraphs[i] }}" alt="{{i+1}} slide">
                                        </div>
                                    %else:
                                        <div class="item">
                                            <img src="data:image/png;base64,{{ subgraphs[i] }}" alt="{{i+1}} slide">
                                        </div>
                                    %end
                                %end
                            </div>
                            <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>
                    %end
                
                    <details>
                        <summary>Найдено подграфов: {{num_cliques}}</summary>
                        %for i, clique in enumerate(cliques):
                            <p>Подграфы в графе {{i+1}}: {{clique}}</p>
                        %end
                    </details>
                %elif num_cliques == 0:
                    <p>Не найдено подграфов в графе</p>
                %end
            </div>
        </div>
    %end
</div>