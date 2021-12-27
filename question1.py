""" This problem was inspired from a youtube video by ben Abramov
    link : https://www.youtube.com/watch?v=XEt09iK8IXs  30:00
    watch the video and complete the ans solution
    This the class creates the Game and you are supposed to only change the ans function(You can also add variables into __init__).
    This Class will be simulated for 25 times and if it passes all the times in given moves or less you win
"""
import random
GAME_SIZE = 10
MAX_MOVES = 500
TRIALS_COUNT = 25

class RabbitGame:
    def __init__(self):
        self.move_counter = 0
        self.cur_pos = random.randint(0, GAME_SIZE)
        self.player = -1

    def rabbitmovement(self):
        if self.cur_pos == 0:
            self.cur_pos += 1
        elif self.cur_pos == GAME_SIZE - 1:
            self.cur_pos -= 1
        else:
            if random.random() > 0.5:
                self.cur_pos += 1
            else:
                self.cur_pos -= 1

    def run(self):
        while self.player != self.cur_pos and self.move_counter < MAX_MOVES:
            self.move_counter += 1
            self.rabbitmovement()
            self.ans()
            print(f"rabbit pos  = {self.cur_pos}  your pos was  = {self.player}")
        if self.move_counter >= MAX_MOVES:
            print("You Failed")
            return False
        print(f"It took you {self.move_counter} times to find the Rabbit")
        return True

    def ans(self):
        pass
if __name__ == "__main__":
    for i in range(TRIALS_COUNT):
        x = RabbitGame()
        if not x.run():
            print("FAILED")
    print("PASSED")
