import matplotlib.pyplot as plt
import read_csv as rcsv

def show_area_countries(countries_list):
  fig, ax = plt.subplots()

  labels = [name["Country/Territory"] for name in countries_list if int(name["Rank"]) < 10]
  values = [int(area["2022 Population"]) for area in countries_list if int(area["Rank"]) < 10]

  ax.bar(labels, values)
  plt.show()

if __name__ == "__main__":
  popl_list = rcsv.read_csv("./app/data.csv")
  # Graph by area
  show_area_countries(popl_list)

