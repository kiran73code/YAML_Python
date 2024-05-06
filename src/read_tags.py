import yaml

with open('tags.yaml', 'r') as file:
    data = yaml.safe_load(file)
    print(data)