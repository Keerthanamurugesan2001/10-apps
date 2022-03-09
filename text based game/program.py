#print header
#create actor
#play a game
import random
import time

from actors import wizard, smallanimal, dragon, creators


def main():
    print_header()
    run_loop()


def print_header():
    print("------------------------------------")
    print("           Text based game")
    print("------------------------------------")


def run_loop():
    actor=[
        smallanimal('Toad', 1),
        creators('Tiger', 12),
        smallanimal('bat', 4),
        dragon('Dragon', 50, 45, True),
        wizard('Evil wizard', 1000)
    ]
    hero = wizard('wizard', 75)

    while True:
        enemy = random.choice(actor)
        print(f"{enemy.name} has level {enemy.level} has ready to attack you")

        cho = input("Did you want [R]unaway or [A]ttack or [L]ookaround").lower().strip()
        print("-----------------------------------------------")
        if cho == 'a':
            if hero.attack(enemy):
                print("wizard win the race")
                actor.remove(enemy)
            else:
                print("wizard Defeated")
        elif cho == 'r':
            print("The wizard is runaway")
            time.sleep(5)
        elif cho == 'l':
            hero.look_around(actor)
            print("look around")
        else:
            print("gameover")
            break


if __name__ == '__main__':
    main()