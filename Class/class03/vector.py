#coding:utf-8
import math

def vector_plus(v1, v2):
    if v1.dimension == v2.dimension:
        vector = []
        for i in range(v1.dimension):
                vector.append(v1.coordinates[i] + v2.coordinates[i])
        return vector


def vector_minus(v1, v2):
    if v1.dimension == v2.dimension:
        vector = []
        for i in range(v1.dimension):
            vector.append(v1.coordinates[i] - v2.coordinates[i])
        return vector

def vector_scalar_multiply(s, v):
    vector = []
    for i in range(v.dimension):
        vector.append(s * v.coordinates[i])
    return vector

def magnitude(v):
    sum = 0
    for i in range(v.dimension):
        sum += pow(v.coordinates[i],2)
    # 只适用于正数
    return sum ** 0.5

def vector_dot_product(v1, v2):
    sum = 0
    if v1.dimension == v2.dimension:
        for i in range(v1.dimension):
            print v1.dimension
            sum += v1.coordinates[i] * v2.coordinates[i]
            print 'sum is :', sum

        return sum

#rad(幅度)and度
def vector_angle(v1, v2, unit):
    if v1.dimension == v2.dimension:
        dot_product = vector_dot_product(v1, v2)
        v1_magitude = magnitude(v1)
        v2_magitude = magnitude(v2)
        x = dot_product / (v1_magitude * v2_magitude)
        if unit == "rad":
            return math.acos(x)
        elif unit == "°":
            return math.acos(x) * 180 / math.pi

def is_parallel_vector(v1, v2):
    if v1.dimension == v2.dimension:
            if int(v1.get_magnitude()) == 0 or int(v2.get_magnitude()) == 0:
                return True
            else:

                multiply = float(v1.coordinates[0]) / float(v2.coordinates[0])
                # print multiply
                for i in range(1, v1.dimension):

                    if int(float(v1.coordinates[i]) - float(multiply * v2.coordinates[i])):
                        # print float(v1.coordinates[i])
                        # print float(multiply * v2.coordinates[i])
                        return False
                return True

def is_orthogonality_vector(v1, v2):
    if v1.dimension == v2.dimension:
        if int(v1.get_magnitude()) == 0 or int(v2.get_magnitude()) == 0 or int(vector_dot_product(v1, v2)) == 0:
            return True
        else:
            return False

def vector_projection(v1, v2):
    normalization_of_v2 = Vector(v2.get_direction())
    dot_product_of_v1_and_normalization_of_v2 = vector_dot_product(v1, normalization_of_v2)

    projection_of_v1_to_v2 = vector_scalar_multiply(dot_product_of_v1_and_normalization_of_v2, normalization_of_v2)
    return projection_of_v1_to_v2

# 只适用于三维
def vetor_cross_product(v1, v2):
    if v1.dimension == v2.dimension == 3:
        cross_product = [v1.coordinates[1]*v2.coordinates[2]-v2.coordinates[1]*v1.coordinates[2], -(v1.coordinates[0]*v2.coordinates[2] - v2.coordinates[0]*v1.coordinates[2]), v1.coordinates[0]*v2.coordinates[1] - v2.coordinates[0]*v1.coordinates[1]]
        # print cross_product
        # print vector_dot_product(v1, Vector(cross_product))
        # print vector_dot_product(v2, Vector(cross_product))
        # if  vector_dot_product  == 0 and int(vector_dot_product(v2, Vector(cross_product))) == 0):
        return cross_product
        # else:
        #     print 'error cross product'
    else:
        print "不是三维向量"

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def get_magnitude(self):
        return magnitude(self)

    def get_direction(self):
        multiply = 0
        if isinstance(magnitude(self), int):
            multiply = 1 / float(magnitude(self))
        else:
            multiply = 1 / magnitude(self)
        return vector_scalar_multiply(multiply, self)

vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
# print vector_plus(vector1, vector2)

vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.233, 0.878])
# print vector_minus(vector3, vector4)

vector5 = Vector([1.671, -1.012, -0.318])
# print vector_scalar_multiply(7.41, vector5)

vector6 = Vector([-0.221, 7.437])
# print vector6.get_magnitude()

vector7 = Vector([8.813, -1.331, -6.247])
# print vector7.get_magnitude()

vector8 = Vector([5.581, -2.136])
# print vector8.get_direction()

vector9 = Vector([1.996, 3.108, -4.554])
# print vector9.get_direction()

vector10 = Vector([7.887, 4.138])
vector11 = Vector([-8.802, 6.776])
# print vector_dot_product(vector10, vector11)

vector12 = Vector([-5.955, -4.904, -1.874])
vector13 = Vector([-4.496, -8.755, 7.103])
# print vector_dot_product(vector12, vector13)

vector14 = Vector([3.183, -7.627])
vector15 = Vector([-2.668, 5.319])
# print vector_angle(vector14, vector15, "rad")

vector16 = Vector([7.35, 0.221, 5.188])
vector17 = Vector([2.751, 8.259, 3.985])
# print vector_angle(vector16, vector17, "°")

vector18 = Vector([-7.579, -7.88])
vector19 = Vector([22.737, 23.64])
# print is_parallel_vector(vector18, vector19)
# print is_orthogonality_vector(vector18, vector19)


vector20 = Vector([-2.029, 9.97, 4.172])
vector21 = Vector([-9.231, -6.639, -7.245])
# print is_parallel_vector(vector20, vector21)
# print is_orthogonality_vector(vector20, vector21)


vector22 = Vector([-2.328, -7.284, -1.24])
vector23 = Vector([-1.821, 1.072, -2.94])
# print is_parallel_vector(vector22, vector23)
# print is_orthogonality_vector(vector22, vector23)

vector24 = Vector([2.118, 4.827])
vector25 = Vector([0, 0])
# print is_parallel_vector(vector24, vector25)
# print is_orthogonality_vector(vector24, vector25)

vector26 = Vector([3.039, 1.879])
vector27 = Vector([0.825, 2.036])
# print vector_projection(vector26, vector27)

vector28 = Vector([-9.88, -3.264, -8.159])
vector29 = Vector([-2.155, -9.353, -9.473])
# print vector_projection(vector28, vector29)
# print vector_minus(vector28, Vector(vector_projection(vector28, vector29)))

vector30 = Vector([3.009, -6.172, 3.692, -2.51])
vector31 = Vector([6.404, -9.144, 2.759, 8.718])
# print vector_projection(vector30, vector31)
# print vector_minus(vector30, Vector(vector_projection(vector30, vector31)))


vector32 = Vector([8.462, 7.893, -8.187])
vector33 = Vector([6.984, -5.975, 4.778])
print '向量积：', vetor_cross_product(vector32, vector33)


vector34 = Vector([-8.987, -9.838, 5.031])
vector35 = Vector([-4.268, -1.861, -8.866])
vector = Vector(vetor_cross_product(vector34, vector35))
print vector_dot_product(vector34, vector)
print 'area of parallelogram:', vector.get_magnitude()


vector36 = Vector([1.5, 9.547, 3.691])
vector37 = Vector([-6.007, 0.124, 5.772])
vector2 = Vector(vetor_cross_product(vector36, vector37))
print vector2

print 'area of triangle:', vector2.get_magnitude() / 2
