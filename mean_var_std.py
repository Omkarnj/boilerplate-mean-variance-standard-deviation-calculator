import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")

  nplist=np.array(list, dtype=float)
# reshaping it into a 3x3 matrix
  nplist=nplist.reshape(3,3)

  #Calculating mean 
  mean_columns = np.mean(nplist, axis=1)
  mean_rows = np.mean(nplist, axis=0)
  mean_flatt = np.mean(nplist.flatten())

  #Calculating variance
  var_columns = np.var(nplist, axis=1)
  var_rows = np.var(nplist, axis=0)
  var_flatt = np.var(nplist.flatten())

  #Calculating standard deviation
  std_columns = np.std(nplist, axis=1)
  std_rows = np.std(nplist, axis=0)
  std_flatt = np.std(nplist.flatten())

  #Calculating max
  max_columns = np.max(nplist, axis=1)
  max_rows = np.max(nplist, axis=0)
  max_flatt = np.max(nplist.flatten())

  #calculating min
  min_columns = np.min(nplist, axis=1)
  min_rows = np.min(nplist, axis=0)
  min_flatt = np.min(nplist.flatten())

  #calculating sum
  sum_columns = np.sum(nplist, axis=1)
  sum_rows = np.sum(nplist, axis=0)
  sum_flatt = np.sum(nplist.flatten())
  
  #creating calculations dictionary
  calculations = {
      'mean': [mean_rows.tolist(), mean_columns.tolist(), mean_flatt.tolist()],
      'variance': [var_rows.tolist(), var_columns.tolist(), var_flatt.tolist()],
      'standard deviation': [std_rows.tolist(), std_columns.tolist(), std_flatt.tolist()],
      'max': [max_rows.tolist(), max_columns.tolist(), max_flatt.tolist()],
      'min': [min_rows.tolist(), min_columns.tolist(), min_flatt.tolist()],
      'sum': [sum_rows.tolist(), sum_columns.tolist(), sum_flatt.tolist()]
  }


  return calculations 