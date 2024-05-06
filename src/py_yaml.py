import yaml
data = {
    'version': 1.0,
    'services': {
        'age': 25,
        'city': 'Bangalore',
        'name': 'kiran', 'skils': ['python', 'Rust', 'R']
        }
    }


with open('config.yaml', 'w') as file:
    yaml.dump(data,file)
