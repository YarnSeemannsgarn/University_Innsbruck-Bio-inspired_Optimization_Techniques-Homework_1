def parse(tsp_string):
    cities = []
    city_part = False
    for line in tsp_string.readlines():
        if city_part:
            if line.find("EOF") is not -1:
                break
            city = tuple([int(i) for i in line.strip().split()[1:]])
            cities.append(city)
        elif line.find("NODE_COORD_SECTION") is not -1:
            city_part = True
    return tuple(cities)
