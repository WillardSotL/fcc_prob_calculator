import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        contents = []
        for color, number in kwargs.items():
            for i in range(number):
                contents.append(color)
        self.contents = contents
        self.draws = []

    def draw(self, number_drawn):
        content = self.contents
        drawn = self.draws
        if number_drawn >= len(content):
            content += drawn
            drawn.clear()
            return content
        else:
            for i in range(number_drawn):
                index = random.randrange(len(content))
                num = content[index]
                drawn.append(num)
                del content[index]
            return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    number_match = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        hat_drawn = hat_copy.draw(num_balls_drawn)
        drawn_balls = {}

        for color in hat_drawn:
            if color not in drawn_balls:
                drawn_balls[color] = 1
            else:
                drawn_balls[color] += 1

        match = 0
        for k in expected_balls:
            if k in drawn_balls and expected_balls[k] <= drawn_balls[k]:
                match +=1
        if match == len(expected_balls):
            number_match += 1
    return number_match / num_experiments
