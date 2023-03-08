from .die import Die, roll
from .utils import value_error

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        if not hasattr(self, 'round'):
            self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value #Fixed sum of values
        return total

    @classmethod
    def run(cls):
        # No need for a variable that counts wins when the info is in the runner
        runner = cls()

        while True:
            
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            try:
                guess = int(guess)
            except:
                value_error('int')
                continue

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            runner.round += 1

            if runner.wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")
            
            prompt = prompt.lower() #Make it a bit more foolproof

            if prompt == 'y' or prompt == 'yes' or prompt == '':
                roll(runner.dice)
                runner.answer() #Re-run values instead of creating a new runner
                continue
            elif prompt == 'n' or prompt == 'no':
                break
            else:
                value_error('str', prompt)
                #i_just_throw_an_exception()
