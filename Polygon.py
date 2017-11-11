import mathutils


class Polygon():

    @staticmethod
    def centroid(vertexes):
        # returns the coordinates of the polygon center by coordinates if its vertexes
        # vertexes format ((0, 0), (1, 0), (1, 1), (0, 1))
        x_list = [vertex[0] for vertex in vertexes]
        y_list = [vertex[1] for vertex in vertexes]
        length = len(vertexes)
        x = sum(x_list) / length
        y = sum(y_list) / length
        return (mathutils.Vector((x, y)))
