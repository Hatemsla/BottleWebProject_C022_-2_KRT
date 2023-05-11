% rebase('layout.tpl', title=title, year=year, message=message)
% arr = []

<h1>Требуется найти заданный подграф в данном графе</h1>
<p>Бла-бла-бла</p>
<form action="/method1" method="post">
    <p><input type="number" required min="2" pattern="[0-9]+" name="graph_count" placeholder="Matrix size"></textarea></p>
    <p><input type="submit" value="Send" class="btn btn-default"></p>
</form>

<div>
    <table>
    <caption>Таблица смежности графа</caption>

    <tr>
        <th></th>
        %for i in range(int(message)):
            <th>{{i+1}}</th>
        %end
    </tr>

    %for k in range(int(message)):
        <tr>
            %if k == 0:
                <th>{{k+1}}</th>
            %for j in range(int(message)):
                <th>1</th>   
            %end
        </tr>
    %end

    </table>
</div>