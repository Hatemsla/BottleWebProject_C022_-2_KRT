% rebase('layout.tpl', title='Home Page', year=year)

<link rel="stylesheet" type="text/css" href="/static/content/main_page.css" />

<div class="background">
  <img class="back_image" src="/static/images/graph_wallpaper4.jpg" />
</div>

<div class="wrapper">
    <div class="info-container">
        <h1>Элементы теории графов. Неориентированные графы. Эйлеровы графы.</h1>
        <p class="lead">
            Данный сайт предоставляет доступ к решению математических задач, связанных с теорией графов.
        </p>
        <p class="lead">
            Вы сможете воспользоваться одним из трех методов, указанных:
        </p>
        <ul class="lead">
            <li class="info-li">Поиск подграфов в заданном графе;</li>
            <li class="info-li">Поиск вершин с наибольшей достижимостью в k-ярусах в заданном графе;</li>
            <li class="info-li">Поиск Эйлерова цикла (цепи) в заданном графе;</li>
        </ul>
    </div>

    <div class="marketing container">
        <div>
            <div class="card col-lg-4">
                <div class="inside">
                    <h2>Поиск подграфов в графе</h2>
                    <img src="/static/images/small_graph1.png" class="card-image"/>
                    <p class="method-info">
                        Найти все подграфы в заданном графе, а также посмотреть их графическое отображение.
                    </p>
                    <p>
                        <a class="button-30" role="button" href="/method_subgraph">Перейти &raquo;</a>
                    </p>
                </div>
            </div>
            <div class="card col-lg-4">
                <div class="inside">
                    <h2>Поиск вершин с наибольшим окружением</h2>

                    <img src="/static/images/small_graph2.png" class="card-image"/>
                    <p class="method-info">
                        Найти вершины с наибольшим окружением в заданном графе, а также посмотреть матрицу ограниченных достижимостей k-шага.
                    </p>
                    <p>
                        <a class="button-30" role="button" href="/method_max_connections">Перейти &raquo;</a>
                    </p>
                </div>
            </div>
            <div class="card col-lg-4">
                <div class="inside">
                    <h2>Поиск Эйлерова цикла</h2>
                    <img src="/static/images/small_graph3.png" class="card-image"/>
                    <p class="method-info">
                        Найти Эйлеров цикл в заданном Эйлеровом графе. Проверить, что он существует.
                    </p>
                    <p>
                        <a class="button-30" role="button" href="/method_eulerian_cycle">Перейти &raquo;</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
    <p>&shy;</p>
</div>

