from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

def normalize(vector):
    return vector / np.linalg.norm(vector)

def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis

def sphere_intersect(center, radius, ray_origin, ray_direction):
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:
        t1 = (-b + np.sqrt(delta)) / 2
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2)
    return None

def nearest_intersected_object(objects, ray_origin, ray_direction):
    distances = [sphere_intersect(obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
    nearest_object = None
    min_distance = np.inf
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance

def ray_tracing(x, y):
	# screen is on origin 
	pixel = np.array([x, y, 0]) 
	origin = camera 
	direction = normalize(pixel - origin) 
	color = np.zeros((3)) 
	reflection = 1 
	for k in range(max_depth): 
		# check for intersections 
		nearest_object, min_distance = nearest_intersected_object(objects, origin, direction) 
		if nearest_object is None: 
			break 
		intersection = origin + min_distance * direction 
		normal_to_surface = normalize(intersection - nearest_object['center']) 
		shifted_point = intersection + 1e-5 * normal_to_surface 
		intersection_to_light = normalize(light['position'] - shifted_point) 
		_, min_distance = nearest_intersected_object(objects, shifted_point, intersection_to_light) 
		intersection_to_light_distance = np.linalg.norm(light['position'] - intersection) 
		is_shadowed = min_distance < intersection_to_light_distance 
		if is_shadowed: 
			break 
		illumination = np.zeros((3)) 
		# ambiant 
		illumination += nearest_object['ambient'] * light['ambient'] 
		# diffuse 
		illumination += nearest_object['diffuse'] * light['diffuse'] * np.dot(intersection_to_light, normal_to_surface) 
		# specular 
		intersection_to_camera = normalize(camera - intersection) 
		H = normalize(intersection_to_light + intersection_to_camera) 
		illumination += nearest_object['specular'] * light['specular'] * np.dot(normal_to_surface, H) ** (nearest_object['shininess'] / 4) 
		# reflection 
		color += reflection * illumination 
		reflection *= nearest_object['reflection'] 
		origin = shifted_point 
		direction = reflected(direction, normal_to_surface)
	return color

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

start_time = MPI.Wtime()

max_depth = 3

#### parameters
width = 1920
height = 1080
camera = np.array([0,-0.2,1])   
light = {'position': np.array([5, 2, 5]), 'ambient': np.array([1, 1, 1]), 'diffuse': np.array([1, 1, 1]),
         'specular': np.array([1, 1, 1])}
#@@구의 중심 좌표@@#
coo=[(0,-0.07,0),(0,-0.1,0),(0,0.1,0),(0.1,-0.1,0.1),(0.1,-0.1,-0.1),(-0.1,-0.1,0.1),(-0.1,-0.1,-0.1),(0.2,-0.1,0.1),(0.1,-0.1,-0.2),(-0.1,-0.1,0.2),(0.1,-0.1,0.1),(-0.2,-0.1,0.2),(0.2,0.05,0.2),(0.2,0.05,-0.2),(-0.2,0.05,0.2),(-0.2,0.05,-0.2),(0.3,0.1,0),(-0.3,0.1,0),(0.25,0.1,0.2),(0,0.1,0.3),(0,0.1,-0.3),(-0.2,0.1,0.25),(0.25,0.1,0.2),(-0.25,0.1,-0.2),(-0.1,0.1,-0.1),(0.1,0.1,-0.1),(-0.1,0.1,0.1),(0.1,0.1,0.1),(0,0.2,0.15),(0.2,0.2,0.1),(-0.1,0.2,0),(0,0.22,0.06),(-0.1,-0.2,-0.1),(0.1,-0.2,-0.1),(-0.1,-0.2,0.1),(0.1,-0.2,0.1),(-0.05,-0.3,-0.05),(0.05,-0.3,-0.05),(-0.05,-0.3,0.05),(0.05,-0.3,0.05)]
#@@리스트 크기 만큼 빈 리스트 만들기@@#
objects = [{} for i in range(len(coo))]
#@@다채로운 색깔을 위한 색깔 값들-조금씩만 다르게 해서 전체적으로는 같은 색이지만 자세히 보면 공 하나하나가 다른 색이 됨@@#
d1=[0.5854726347078507,0.5731032272632454,0.5819635882103538,0.5091763435982246,0.5797142940244396,0.5514448759105501,0.48625675890704867,0.4408258984688753,0.4241784116275192,0.5550050113834619,0.5238679388364699,0.5188004018756625,0.48518796791192076,0.4479491227143067,0.5246951904902761,0.5789484600617734,0.40633616183568383,0.5113057355458723,0.5056785880545078,0.4688518565185215,0.5,0.6,0.4,0.6,0.5,0.4,0.6,0.6,0.5,0.55,0.5,0.6,0.5,0.4,0.5,0.6,0.4,0.6,0.5,0.4,0.6,0.6,0.5,0.55,0.5,0.6,0.5,0.4,0.5]
d2=[0.5032566537214404,0.41944216449266813,0.5406673622852147,0.5644886667694781,0.4857125331567208,0.47403140608124983,0.568214990328141,0.5402275796927661,0.48363761948090034,0.4959796817385568,0.5397359387865952,0.44018520843763165,0.41494144970538177,0.5929556315257192,0.5635367385465402,0.5482199944160612,0.4325535252403566,0.5672153534727087,0.41863615595957043,0.45578470226558204,0.4,0.52,0.4,0.54,0.5,0.6,0.6,0.4,0.6,0.5,0.5,0.6,0.5,0.4,0.6,0.4,0.6,0.5,0.4,0.6,0.6,0.5,0.55,0.5,0.6,0.5,0.4,0.5]
#@@포도알에 관한 objects@@#
for a,(x,y ,z) in enumerate(coo):
    objects[a] = {'center': np.array([x, y, z]), 'radius': 0.1, 'ambient': np.array([0.1, 0, 0]),'diffuse': np.array([d1[a],0,d2[a]]), 'specular': np.array([1, 1, 1]), 'shininess': 80, 'reflection': 0.1}
#@@배경, 포도 줄기, 포도 잎에 관한 objects@@#
objects.append({'center': np.array([0, -9000, 0]), 'radius': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5})
objects.append({'center': np.array([0, 0.40, 0]), 'radius': 0.07, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0, 0.5, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})
objects.append({'center': np.array([0, 0.53, 0]), 'radius': 0.07, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})
objects.append({'center': np.array([0.07, 0.53, 0]), 'radius': 0.07, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})
objects.append({'center': np.array([-0.07, 0.53, 0]), 'radius': 0.07, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})
objects.append({'center': np.array([0.05, 0.35, 0.05]), 'radius': 0.05, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0.5, 0.7, 0.5]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})
objects.append({'center': np.array([0.07, 0.36, 0.07]), 'radius': 0.05, 'ambient': np.array([0.1, 0.1, 0.1]),'diffuse': np.array([0.5, 0.7, 0.5]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0})

ratio = float(width) / height
screen = (-1, 1 / ratio, 1, -1 / ratio)  

image = np.zeros((height, width, 3))
Y = np.linspace(screen[1], screen[3], height)
X = np.linspace(screen[0], screen[2], width)

local_image = np.zeros((height, width, 3))

for i, y in enumerate(Y):
    for j, x in enumerate(X):
        if i % size == rank:               #이 식을 통하여 Y(Height)를 size 만큼 나눔->병렬 컴퓨팅#
            color = ray_tracing(x, y) 
            local_image[i, j] = np.clip(color, 0, 1)

result_image = None

#병렬로 계산된 사진들을 합침
if rank == 0:
    result_image = np.zeros((height, width, 3))

comm.Reduce(local_image, result_image, op=MPI.SUM, root=0)

#이미지 저장
if rank == 0:
    plt.imsave('image.png', result_image)

#종료
end_time = MPI.Wtime()
if rank == 0:
    print("Overall elapsed time: " + str(end_time - start_time))
