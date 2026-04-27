import math
from .shape import Shape

from .shape_color import ShapeColor


class Parallelogram(Shape):
    __name = "Parallelogram"

    def __init__(self, d1: float, d2: float, angle: float, color: ShapeColor):
        self.d1 = d1
        self.d2 = d2
        self.angle = angle
        self.color = color

    def area(self):
        return self.d1 * self.d2 * math.sin(self.angle) / 2

    def points(self):
        sid_sq_sum = self.d1**2 + self.d2**2
        ang_mu = 2 * self.d1 * self.d2 * math.cos(self.angle)

        side_1 = math.sqrt(sid_sq_sum + ang_mu) / 2
        side_2 = math.sqrt(sid_sq_sum - ang_mu) / 2

        side_2_x = math.cos(self.angle) * side_2
        side_2_y = math.sin(self.angle) * side_2

        return [
            (0, 0),
            (side_1, 0),
            (side_2_x + side_1, side_2_y),
            (side_2_x, side_2_y),
        ]

    def __repr__(self):
        return f"<Parallelogram d1={self.d1}, d2={self.d2}, angle={self.angle}, color={self.color}>"

    @classmethod
    def name(cls):
        return cls.__name


if __name__ == "__main__":
    assert Parallelogram.name() == "Parallelogram"

    p = Parallelogram(10, 20, 1.0472, ShapeColor("red"))
    assert isinstance(p, Shape), "Not a shape"

    print(f"{p}")

    import matplotlib.pyplot as plt

    points = p.points()
    print(points)
    plt.fill([pp[0] for pp in points], [pp[1] for pp in points])
    plt.fill([0, 1, 1, 0], [0, 0, 1, 1])
    plt.gca().set_aspect("equal")
    plt.show()
