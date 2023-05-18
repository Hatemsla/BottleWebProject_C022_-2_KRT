% rebase('layout.tpl', title='Home Page', year=year)

<link rel="stylesheet" type="text/css" href="/static/content/main_page.css" />

<div class="background">
  <img class="back_image" src="/static/images/graph_wallpaper1.jpg" />
</div>

<div class="wrapper">
    <div class="info-container">
        <h1>Элементы теории графов. Неориентированные графы. Эйлеровы графы.</h1>
        <p class="lead">
        </p>
    </div>

    <div class="marketing container-card">
        <div class="card col-md-4">
            <h2>Поиск клик в графе</h2>
            <p>Требуется найти заданную клику в заданном графе. Например, заданная клика представляет собой полный граф из пяти вершин, степень каждой из которых равна четырем.</p>
            <p><a class="btn btn-default" href="/method_subgraph">Перейти &raquo;</a></p>
        </div>
        <div class="card col-md-4">
            <h2>Поиск вершин с наибольшим окружением</h2>
            <p>Требуется найти в графе вершины с наибольшим окружением. Реализация алгоритма поиска в графе вершин, имеющих наибольшее окружение. Вычисляются последовательно степени матрицы смежности A2, А3, …, Ak и соответствующие им матрицы ограниченных достижимостей R2, R3, …, Rk.</p>
            <p><a class="btn btn-default" href="/method_max_connections">Перейти &raquo;</a></p>
        </div>
        <div class="card col-md-4">
            <h2>Поиск Эйлерова цикла</h2>
            <p></p>
            <p><a class="btn btn-default" href="/method_eulerian_cycle">Перейти &raquo;</a></p>
        </div>
    </div>
</div>

