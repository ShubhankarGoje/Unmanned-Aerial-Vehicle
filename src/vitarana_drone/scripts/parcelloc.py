start_loc = [18.99988879, 72.00021844, 16.75798088]

A1 = [18.9998103,  72.00014271, 16.75797003] # x+1.5, y-1.5

X1 = [18.99993663, 72.00014303, 16.75798078]



def lat_to_x(input_latitude):
    return 110692.0702932625 * (input_latitude - 19)

# Convert Longitude to Y in meters for Carteasian cordinate system
def long_to_y(input_longitude):
    return -105292.0089353767 * (input_longitude - 72)

# Convert X in meters to Latitude for Geographic cordinate system
def x_to_lat(input_x):
    return ((input_x/110692.0702932625) + 19)

# Convert Y in meters to Longitude for Geographic cordinate system
def y_to_long(input_y):
    return ((-input_y/105292.0089353767) + 72)

a=[18.99993663, 72.00014303, 16.75798078]
ax=[lat_to_x(a[0]),long_to_y(a[1])]

l = []

for i in range(3):
	for j in range(3):
		x = ax[0] + j*1.5
		y = ax[1] - i*1.5
		l.append([x_to_lat(x),y_to_long(y),a[2]])
		print(x,y)
print ""
print l