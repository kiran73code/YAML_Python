import yaml


with open('anchor.yaml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)