import matplotlib.pyplot as plt
import read_csv as rcsv


def get_values_labels(countries_list):

  labels = list(filter(lambda count: int(count["Rank"]) < 10, countries_list))
  labels = list(map(lambda count: count["Country/Territory"], labels))

  values = list(filter(lambda count: int(count["Rank"]) < 10, countries_list))
  values = list(map(lambda count: count["2022 Population"], values))

  return labels, values


def show_population_countries_bars(countries_list):
  fig, ax = plt.subplots()

  values = []
  labels = []

  labels, values = get_values_labels(countries_list)

  ax.bar(labels, values)
  plt.show()


def show_population_countries_pie(countries_list):
  fig, ax = plt.subplots()

  values = []
  labels = []
  
  labels, values = get_values_labels(countries_list)

  ax.pie(values, labels=labels)
  ax.axis("equal")
  plt.show()


if __name__ == "__main__":
  popl_list = rcsv.read_csv("./app/data.csv")
  # Graph by area
  choice = 0
  while choice != 1 and choice != 2:
    choice = int(
      input("What do you want to see?\n| 1 |  Bar Chart\n| 2 |  Pie Chart\n"))
    if (choice != 1 and choice != 2):
      print("| X | SELECT A VALID OPTION | X |")

  if choice == 1:
    show_population_countries_bars(popl_list)
  else:
    show_population_countries_pie(popl_list)
