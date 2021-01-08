import random
import pandas as pd

# this is the list of restaurants
list = ['CAVA', 'Diced', 'Chipotle', "Jasmin's", 'Burger-Fi', 'Shake Shack', 'Tasu', "Enrigo's", 'Gonza', 'Chanticleer']

df = pd.DataFrame(data=list, columns=['Restaurants'])
df['cuisine'] = ['Mediterranean', 'Organic', 'Fast Food', 'Mediterranean', 'Fast Food', 'Fast Food', 'Asian', 'Italian', 'Mexican', 'French']
# df['fast'] = [1, 0, 1, 1, 1, 1, 0, 0, 0, 0]
# df['dine-in'] = [0,0,1,1,1,1,1,1,1,1]
