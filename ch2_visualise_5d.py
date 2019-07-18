import ut
import csv
import urllib.request

###################
# Reading in Data #
###################

# Read iris.csv from file repository
url_str = 'http://blender.chrisconlan.com/iris.csv'
iris_csv = urllib.request.urlopen(url_str)
iris_ob = csv.reader(iris_csv.read().decode('utf-8').splitlines())

# Store header as a list
iris_header = []
iris_data = []

for v in iris_ob:
    if not iris_header:
        iris_header = v
    else:
        v = [float(v[0]), float(v[1]), float(v[2]), float(v[3]), str(v[4])]
        iris_data.append(v)
        
# Clear scene
ut.delete_all()

# Place data
for i in range(0, len(iris_data)):
#    ut.create.sphere('row-' + str(i))
    v = iris_data[i]
    if v[4] == 'versicolor':
        ut.create.cube('versicolor-' + str(i))
    if v[4] == 'setosa':
        ut.create.sphere('setosa-' + str(i))
    if v[4] == 'virginica':
        ut.create.cone('virginica-' + str(i))
        
    scale_factor = 0.2
    ut.act.scale((v[3] * scale_factor,) * 3)
    ut.act.location((v[0], v[1], v[2]))