Порівняння результатів та пояснення відмінностей

Алгоритм BFS (пошук у ширину):

Принцип роботи: BFS досліджує граф шар за шаром. Він спочатку відвідує всіх безпосередніх сусідів стартового вузла, потім усіх сусідів цих сусідів і так далі. Використовує чергу (Queue).
Властивості шляху: BFS гарантовано знаходить найкоротший шлях у незваженому графі (тобто шлях з найменшою кількістю ребер).
У нашому випадку: Для шляху City Center → West Outskirts, BFS знаходить шлях ['City Center', 'South District', 'West Outskirts']. Цей шлях має 2 ребра. Оскільки BFS шукає шлях з найменшою кількістю ребер, він знаходить саме цей шлях.

Алгоритм DFS (пошук у глибину):

Принцип роботи: DFS досліджує граф, йдучи якомога глибше по одній гілці, перш ніж повернутися і досліджувати інші гілки. Використовує стек (Stack) (або рекурсію).
Властивості шляху: DFS не гарантує знаходження найкоротшого шляху ні за кількістю ребер, ні за вагою. Він може знайти будь-який шлях до цільового вузла, який зустріне першим під час свого "глибинного" обходу.
У нашому випадку: Для шляху City Center → West Outskirts, порядок обходу сусідів визначає шлях. Якщо City Center спочатку розглядає North District, DFS піде туди, потім до East Outskirts, і лише тоді повернеться до City Center, щоб дослідити South District. Таким чином, шлях, який знайде DFS, може залежати від порядку, в якому networkx повертає сусідів. У нашому прикладі, через порядок додавання ребер, South District швидше за все буде оброблений після North District, але це не гарантовано.

У нашому конкретному прикладі:
Шлях City Center → South District → West Outskirts має лише 2 ребра.
Будь-який інший шлях до West Outskirts через City Center мав би більше ребер (наприклад, City Center → North District → East Outskirts → ... ).
Оскільки шлях з 2 ребер є найкоротшим за кількістю ребер, BFS гарантовано знайде його.
DFS також знайшов його, оскільки за певного порядку обходу сусідів South District виявився доступним і привів до цільового вузла через 2 ребра раніше, ніж будь-який інший, довший шлях.
