'''
	3D Vector Math Library
	Author: Jesse Buhagiar
	Date 10-4-2019

	Data is stored in the format <x, y, z>, indexed from 0
'''
import math

'''
	Vector Length

	Returns the length of a given vector, <x, y, z>
'''
def vec3_length(v):
	return math.sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))

'''
	Dot product of two vectors

	Defined as (v1x * v2x) + (v1y * v2y) + (v1z * v2z) 
'''
def vec3_dot(v1, v2):
	return ((v1[0] * v2[0]) + (v1[1] * v2[1]) + (v1[2] * v2[2]))

'''
	Angle between two vectors, v1 and v2
'''
def vec3_angle(v1, v2):
	dot = vec3_dot(v1, v2) # Get the dot product between v1 and v2
	v1_len = vec3_length(v1)
	v2_len = vev3_length(v2)
	costheta = dot / (v1_len * v2_len)
	return math.acos(costheta)

	
