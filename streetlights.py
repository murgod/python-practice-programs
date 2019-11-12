#street has length n
#we have lights list depicting [position_of_light(0-n), radius_it_covers]
#find the number of lights required to light up the street.
#Ex: n = 10
#lights = [[0,5], [1,3], [5,4], [8, 3]]
# ans = 2
# Explaination : [0,5] & [8, 3] together can light up entire street hence the ans is 2

n = 10
lights = [[2,10],[0,5], [1,3], [5,4], [8, 3]]

def streetlights(n, lights):
    print(n)
    print(len(lights))

    print(lights)
    #sorted(lights, key=lambda l:l[0], reverse=False)
    lights.sort(key = lambda x: x[0])
    print(lights)


streetlights(n, lights)
