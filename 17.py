
from os import read

@dataclass
class point:
    x : int = 0
    y : int = 0

    def move(self, x_mov, y_mov):
        self.x += x_mov
        self.y += y_mov
    
    def update(self):
        if self.x > 0:
            self.x -= 1
        elif self.x < 0 :
            self.x += 1
        if self.y > 0:
            self.y -= 1
        if self.y < 0:
            self.y -= 1


def reader(filename):

    with open("16_input.txt","r") as file:
        line = file.readline().strip()
        line = line.split(" ")
        x_bounds = [int(x[2:-1]) for x in line[2].split("..")]
        y_bounds = [int(x[2:]) for x in line[3].split("..")]
    
    return x_bounds,y_bounds


x_bound,y_bound = reader("16_input.txt")

def highest_point(x_bound, y_bound):

    proj = point()
    traj = point()

    
    if x_bound[0] >= proj.x and x_bound[0] <= proj.x and y_bound[0] >= proj.y and y_bound[0] <= proj.y:


