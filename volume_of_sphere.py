import math
def calc_vol_of_sphere(radius):
	volume= (4/3) * math.pi * math.pow(radius,3)
	return volume

radius1 = 30
volume1 = calc_vol_of_sphere(radius1)
print(f"The volume of a sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calc_vol_of_sphere(radius2)
print(f"The volume of a sphere with radius {radius2} is: {volume2}")