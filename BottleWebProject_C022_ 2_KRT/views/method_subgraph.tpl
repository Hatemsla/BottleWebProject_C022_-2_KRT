% rebase('layout.tpl', graph_count=graph_count, year=year, subgraph_count=subgraph_count, graph_data=graph_data, cliques=cliques, num_cliques=num_cliques, main_graph=main_graph, subgraphs=subgraphs)

<link rel="stylesheet" type="text/css" href="/static/content/method_subgraph.css" />

<h1>Требуется найти заданный подграф в данном графе</h1>
<p>Например, заданный подграф представляет собой полный граф из пяти вершин, степень каждой из которых равна четырем. На рисунке 1 представлены диаграмма подграфа и соответствующая ему матрица смежности вершин.</p>
<div>
 <img class="graph-image" src="/static/images/subgraph_image.png">
</div>
<p class="graph-image-text">Рисунок 1 – Заданный фрагмент и его матрица смежности</p>
<p>Созданная программа должна выполнять следующие действия:
<ul>
    <li class="info-li">Поиск всех имеющихся заданных подграфов в исходном графе;</li>
    <li class="info-li">Вывод всех найденных подграфов в виде списка вершин.</li>
</ul>
</p>
<div class="form-container">
    <form action="/method_subgraph" method="post">
        <div class="form-input">
            <label for="graph_count">Введите количество графов:</label>
            <input type="number" id="graph_count" value="{{graph_count}}" required min="2" max="20" pattern="[0-9]+" name="graph_count" placeholder="Размер матрицы смежности графа">
        </div>
        <div class="form-input">
            <label for="subgraph_count">Введите размер клики:</label>
            <input type="number" id="subgraph_count" value="{{subgraph_count}}" required min="2" max="20" pattern="[0-9]+" name="subgraph_count" placeholder="Размер клики">
        </div>
        <div class="form-buttons">
            <button type="submit" name="form" value="Send1">Построить матрицу</button>
            <button type="submit" name="form" value="Random">Случайная матрица</button>
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
            <p class="confirm"><button type="submit" name="form" value="Confirm">Посчитать</button></p>
        </form>  
    </div>
%end
<div class="result-container">
    <div class="graph-container">
        %if main_graph:
            <img src="data:image/png;base64,{{ main_graph }}"/>
            <p>Рисунок 2 - Граф</p>
        %end
    </div>
    %if num_cliques > 0:
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