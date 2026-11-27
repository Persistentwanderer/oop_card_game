import yaml
import os


games_directory = os.fsencode(str("./")) 

for file in games_directory: 
    print(file)
#     with open('./consfig.yaml') as file:
#         prime_service = yaml.safe_load(file)

# prime_service