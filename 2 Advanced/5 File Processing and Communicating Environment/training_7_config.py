"""
https://edube.org/learn/pcpp1-5/lab-interpolating-values-lab-1
"""
from configparser import ConfigParser

cp_mess = ConfigParser()
cp_mess.read('mess.ini')

cp_prod = ConfigParser()
file_prod = open('prod_config.ini', mode='w')
cp_dev = ConfigParser()
file_dev = open('dev_config.ini', mode='w')


try:
    for section_name in cp_mess.sections():
        section_tmp = dict()
        prod = True
        section_tmp[section_name] = {}
        for prop,val in cp_mess[section_name].items():
            if prop=='env':
                prod = val=='prod'
            else:
                section_tmp[section_name][prop] = val
        if prod:
            cp_prod.update(section_tmp)
        else:
            cp_dev.update(section_tmp)
        del section_tmp

except BaseException as e:
    print(e)
finally:
    cp_prod.write(file_prod)
    cp_dev.write(file_dev)
    file_prod.close()
    file_dev.close()