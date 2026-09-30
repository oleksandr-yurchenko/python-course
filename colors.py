from rich.console import Console
from rich.table import Table

table = Table(title="Мови програмування")
table.add_column("Мова")
table.add_column("Рік")
table.add_column("Автор")
table.add_row("Python","1991",'Oleksandr')
table.add_row("JavaScript","1995","Brendan Eich")
table.add_row("Go","2001","Robert Griesemer")
Console().print(table)