% rebase('layout.tpl', graph_count=graph_count, year=year, subgraph_count=subgraph_count, graph_data=graph_data, subgraph_data=subgraph_data)

<link rel="stylesheet" type="text/css" href="/static/content/method_subgraph.css" />

<h1>Требуется найти заданный подграф в данном графе</h1>
<p>Бла-бла-бла</p>
<form action="/method_subgraph" method="post">
    <p><input type="number" value="{{graph_count}}" required min="2" required max="20" pattern="[0-9]+" name="graph_count" placeholder="Размер матрицы смежности графа"></p>
    <p><input type="number" value="{{subgraph_count}}" required min="2" required max="20" pattern="[0-9]+" name="subgraph_count" placeholder="Размер матрицы смежности для подграфа"></p>
    <p><input type="submit" name="form" value="Send1" class="btn btn-default"></p>
</form>

<div>
    %if int(graph_count) > 0:
        <form action="/method_subgraph" method="post">
            <table name="graph_data">
    
            <caption>Таблица смежности графа</caption>

            <tr>
                <th></th>
                %for i in range(int(graph_count)):
                    <th>{{i+1}}</th>
                %end
            </tr>

            %for i in range(int(graph_count)):
                <tr>
                    <th>{{i+1}}</th>
                    %for j in range(int(graph_count)):
                        %if graph_data:
                            <td><input type="number" name="{{i}}{{j}}g" value="{{graph_data[i][j]}}" required min="0" required max="1" pattern="[01]" maxlength="1"></td>
                        %else:
                            <td><input type="number" name="{{i}}{{j}}g" value="0" required min="0" required max="1" pattern="[01]" maxlength="1"></td>
                        %end
                    %end
                </tr>
            %end

            </table>
        
    %end

    %if int(subgraph_count) > 0:
            <table name="subgraph_data">
    
            <caption>Таблица смежности подграфа</caption>

            <tr>
                <th></th>
                %for i in range(int(subgraph_count)):
                    <th>{{i+1}}</th>
                %end
            </tr>

            %for i in range(int(subgraph_count)):
                <tr>
                    <th>{{i+1}}</th>
                    %for j in range(int(subgraph_count)):
                        %if subgraph_data:
                            <td><input type="number" name="{{i}}{{j}}sg" value="{{subgraph_data[i][j]}}" required min="0" required max="1" pattern="[01]" maxlength="1"></td>
                        %else:
                            <td><input type="number" name="{{i}}{{j}}sg" value="0" required min="0" required max="1" pattern="[01]" maxlength="1"></td>
                        %end
                    %end
                </tr>
            %end

            </table>
            <p><input type="submit" name="form" value="Confirm" class="btn btn-default"></p>
        </form>
    %end
</div>