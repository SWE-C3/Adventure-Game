"""
Methods for handling a save file of the player's current progress
"""

from src import player


class SaveFile:
    """
    Defines methods for transferring information between
    player class attributes and a textfile
    """

    @staticmethod
    def write_file():
        """
        Transfers relevant player attribute values into a textfile
        """
        with open("save_file.txt", "w") as file:
            file.write("Ebene:\n" + str(player.level) + "\n\n")

            file.write("Position:\n")
            for i in player.position:
                file.write(str(i) + "\n")
            file.write("\n")

            file.write("Lebenspunkte:\n" + str(player.health) + "\n\n")

            file.write("Items:\n")
            for i in player.items:
                file.write(i + "\n")
            file.write("\n")

            file.write("Cookies:\n")
            for i in player.cookies:
                file.write(i + "\n")

    @staticmethod
    def read_file():
        """
        Transfers relevant lines from a given textfile into player attribute values
        """
        with open("save_file.txt", "r") as file:
            stats = file.readlines()

            for i in range(0, 21):
                stats[i] = stats[i].rstrip('\n')

            player.level = stats[1]

            player.position[0] = stats[4]
            player.position[1] = stats[5]

            player.health = stats[8]

            for i in range(0, 5):
                player.items[i] = stats[i+11]

            for i in range(0, 3):
                player.cookies[i] = stats[i+18]
