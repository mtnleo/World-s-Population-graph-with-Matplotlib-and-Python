import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    header = next(reader)
    popl_list = []
    for row in reader:
      iterable = zip(header, row)
      popl_dict = {header: row for header, row in iterable}
      popl_list.append(popl_dict)

  return popl_list
  
if __name__ == "__main__":
  population_list = read_csv("./app/data.csv")
  print(population_list)