import requests
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, '../gmm/astrox_gmm6_allvar_0.csv')
my_file_out = os.path.join(THIS_FOLDER, 'results.csv')

r = requests.post(
         'http://cdsxmatch.u-strasbg.fr/xmatch/api/v1/sync',
         data={'request': 'xmatch', 'distMaxArcsec': 3, 'RESPONSEFORMAT': 'csv',
         'cat2': 'simbad', 'colRA1': 'ra', 'colDec1': 'dec', 'selection':'best'},
         files={'cat1': open(my_file, 'r')})

#print(r.text)
h = open(my_file_out, 'w')
h.write(r.text)
h.close()