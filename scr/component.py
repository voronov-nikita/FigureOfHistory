class Standartindivid():

    def move_right(self, cord_x, size_individ):
        if cord_x < 500 - size_individ - 5:
            return True
        return False
    
    def move_left(self, cord_x):
        if cord_x > 0:
            return True
        return False
    
    def move_up(self, cord_y):
        if cord_y > 1:
            return True
        return False

    def move_down(self, cord_y, size_individ):
        if cord_y < 500 - size_individ - 5:
            return True
        return False
    


