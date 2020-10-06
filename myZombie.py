#! python3

# myZombie.py - Runs a custom bot for playing Zombie Dice by Steve Jackson Games. The simulator is built by Al Sweigart and this is based off of a section of automate the boring stuff

import zombiedice

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0

        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            print(gameState)

            if shotguns == 2:
                break

            diceRollResults = zombiedice.roll()

zombies = (
        zombiedice.examples.RandomCoinFlipZombie(name='Random'),
        zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='2 shotguns', minShotguns=2),
        zombiedice.examples.MinNumShotgunsThenStopsZombie(name='1 shotguns', minShotguns=1),
        MyZombie(name='me') 
    )


# zombiedice.runWebGui(zombies=zombies, numGames=1000)
zombiedice.runTournament(zombies=zombies, numGames=1000)
