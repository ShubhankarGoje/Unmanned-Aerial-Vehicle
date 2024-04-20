import csv

# Convert Latitude to X in meters for Carteasian cordinate system
def lat_to_x(input_latitude):
    return 110692.0702932625 * (input_latitude - 19)

# Convert Longitude to Y in meters for Carteasian cordinate system
def long_to_y(input_longitude):
    return -105292.0089353767 * (input_longitude - 72)

deliv =[]
retu = []
with open('/home/prajwal/catkin_ws/src/vitarana_drone/scripts/manifest.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
            	print row
                if row[0]=='DELIVERY':
                    x = row[2].split(';')
                    deliv.append([float(x[0]),float(x[1]),float(x[2])])
                else:
                	x = row[1].split(';')
                	retu.append([float(x[0]),float(x[1]),float(x[2])])
print "\n"
for i in deliv:
    print i
print "\n"
for i in retu:
    print i


print "\n"
for i in range(9):
    deliv[i][0] = lat_to_x(deliv[i][0])
    deliv[i][1] = long_to_y(deliv[i][1])

    retu[i][0] = lat_to_x(retu[i][0])
    retu[i][1] = long_to_y(retu[i][1])

print "\n"


print "\n"
for i in deliv:
    print i
print "\n"
for i in retu:
    print i