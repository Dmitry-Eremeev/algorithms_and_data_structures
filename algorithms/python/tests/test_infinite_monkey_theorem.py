from ..infinite_monkey_theorem import Guess

for guess_one_by_one in [True, False]:
    guess = Guess(sample="yes")
    guess.play(guess_one_by_one=guess_one_by_one)



