import click

def print_red(text='''text'''):
     click.secho(text,fg='red')

def print_green(text='''text'''):
     click.secho(text,fg='green')
     
def print_yellow(text='''text'''):
     click.secho(text,fg='yellow')
def startup() :
          click.secho("""\n\n\t\t\t\t\t\t\t\t\t#####    #####   #####   #   #   #       #####   #####   #####   #####   #   #
\t\t\t\t\t\t\t\t\t#   #    #   #   #   #   #   #   #       #   #     #       #     #   #   ##  #
\t\t\t\t\t\t\t\t\t#####    #   #   #####   #   #   #       #####     #       #     #   #   # # #
\t\t\t\t\t\t\t\t\t#        #   #   #       #   #   #       #   #     #       #     #   #   #  ##
\t\t\t\t\t\t\t\t\t#        #####   #       #####   #####   #   #     #     #####   #####   #   #
           """,fg="cyan")
          click.secho("""\t\t\t\t\t\t\t\t\t***********************  Analytics and Monitoring Program  *******************\n""",fg="blue", bold=True)
          click.secho("This is a Free program, made for the purpose of Anaysing and studying the Population and related data of the different parts of the world.\nIt is free to distribute and modifying.")
          click.secho("Data Collected from :",fg="yellow")
          click.secho("""World Population Data(Live)\t https://www.worldometers.info/world-population/population-by-country/
INDIA States Population (2019)\t http://statisticstimes.com/demographics/india/indian-states-population.php
INDIA States Area \t\t https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area""",fg='blue')
           
          click.secho("""\n** The following program is case sesitive. **\n""",fg="bright_red")
