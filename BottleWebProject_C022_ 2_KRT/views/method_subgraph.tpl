% rebase('layout.tpl', title=title, year=year, message=message)

<link rel="stylesheet" type="text/css" href="/static/content/method_subgraph.css" />

<h1>Требуется найти заданный подграф в данном графе</h1>
<p>Бла-бла-бла</p>
<form action="/method_subgraph" method="post">
    <p><input type="number" required min="2" pattern="[0-9]+" name="graph_count" placeholder="Matrix size"></textarea></p>
    <p><input type="submit" value="Send" class="btn btn-default"></p>
</form>

<div>
    <table name="graph_data">
    %if int(message) > 0:
    <caption>Таблица смежности графа</caption>
    %end
    <tr>
        <th></th>
        %for i in range(int(message)):
            <th>{{i+1}}</th>
        %end
    </tr>

    %for k in range(int(message)):
        <tr>
            <th>{{k+1}}</th>
            %for j in range(int(message)):
                <td><input type="number" size="5"></td>
            %end
        </tr>
    %end

    </table>
</div>