from configparser import ConfigParser

config = ConfigParser()
config['DEFAULT'] = {'a': '1'}
config['SEC1'] = {'a': '2', 'b': '3'}
config['SEC2'] = {'a': '4'}
config['SEC3'] = {}

print(config['SEC1']['a'])
print(config['SEC2']['a'])
print(config['SEC3']['a'])
