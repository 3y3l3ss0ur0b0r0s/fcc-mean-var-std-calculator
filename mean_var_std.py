import numpy as np

def calculate(list):
  
  print(list)
  
  # Check for 9 elements
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  # Create a dictionary called 'calculations'
  calculations = {}
    
  # Turn list into a NumPy array
  n_array = np.array(list).reshape(3,3)
  # Retain flattened array
  flat_array = np.array(list).flatten()
  print(n_array)
  
  # Calculate mean and add to dicitonary
  mean = [ np.mean(n_array, axis=0).tolist(), np.mean(n_array, axis=1).tolist(), np.mean(flat_array) ]
  calculations['mean'] = mean
  
  # Calculate variance and add to dictionary
  variance = [ np.var(n_array, axis=0).tolist(), np.var(n_array, axis=1).tolist(), np.var(flat_array).tolist() ]
  calculations['variance'] = variance
  
  # Calculate standard deviation and add to dictionary
  std = [ np.std(n_array, axis=0).tolist(), np.std(n_array, axis=1).tolist(), np.std(flat_array) ]
  calculations['standard deviation'] = std
  
  # Calculate max and add to dictionary
  max = [ np.max(n_array, axis=0).tolist(), np.max(n_array, axis=1).tolist(), np.max(flat_array) ]
  calculations['max'] = max
  
  # Calculate min and add to dictionary
  min = [ np.min(n_array, axis=0).tolist(), np.min(n_array, axis=1).tolist(), np.min(flat_array) ]
  calculations['min'] = min
  
  # Calculate sum and add to dictionary
  sum = [ np.sum(n_array, axis=0).tolist(), np.sum(n_array, axis=1).tolist(), np.sum(flat_array) ]
  calculations['sum'] = sum

  return calculations