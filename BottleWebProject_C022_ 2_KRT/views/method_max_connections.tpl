% rebase('layout.tpl', year=year, graph_count=graph_count, k_step=k_step, graph_data=graph_data, main_graph=main_graph, is_valid_graph=is_valid_graph, res=res)

<link rel="stylesheet" type="text/css" href="/static/content/method_max_connections.css" />

<h1>Требуется найти в графе вершины с наибольшим окружением</h1>
<p>бубубу</p>
<div>
 <img class="graph-image" src="/static/images/subgraph_image.png">
</div>
<p class="graph-image-text">Рисунок 1 – бебебе</p>
<p>Созданная программа должна выполнять следующие действия:
<ul>
    <li class="info-li">Вывод матрицы ограниченных достижимостей k-шага;</li>
    <li class="info-li">Вывод вершин с наибольшим окружением;</li>
</ul>
</p>
<div class="form-container">
    <form action="/method_max_connections" method="post">
        <div class="form-input">
            <label for="graph_count">Введите размерность графа:</label>
            <input type="number" id="graph_count" value="{{graph_count}}" required min="2" max="20" pattern="[0-9]+" name="graph_count" placeholder="Размер матрицы смежности графа">
        </div>
        <div class="form-input">
            <label for="k_step">Введите количество ярусов:</label>
            <input type="number" id="k_step" value="{{k_step}}" required min="1" max="5" pattern="[0-9]+" name="k_step" placeholder="Глубина шага k">
        </div>
        <div class="form-buttons">
            <button type="submit" name="form" value="Send2">Построить матрицу</button>
            <button type="submit" name="form" value="Random2">Случайная матрица</button>
        </div>
    </form>
</div>
%if int(graph_count) > 0:
    <div class="table-container">
        <form action="/method_max_connections" method="post">
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
            <p class="confirm2"><button type="submit" name="form" value="Confirm2">Посчитать</button></p>
        %if len(res) > 0:
            <p>{{res}}</p>
        %end
        </form>
    </div>
%end
