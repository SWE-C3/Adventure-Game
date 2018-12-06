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
            file.write("Ebene:\n" + player.Player.position[2] + "\n\n")

            file.write("Position:\n" + player.Player.position[0] + "\n" +
                       player.Player.position[1] + "\n\n")

            file.write("Lebenspunkte:\n" + str(player.Player.health) + "\n\n")

            file.write("Items:\n")
            for i in player.Player.items:
                file.write(i + "\n")
            file.write("\n")

            file.write("Cookies:\n")
            for i in player.Player.cookies:
                file.write(i + "\n")

    @staticmethod
    def read_file():
        """
        Transfers relevant lines from a given textfile into
        player attribute values
        """
        with open("save_file.txt", "r") as file:
            stats = file.readlines()

            for i in range(0, 21):
                stats[i] = stats[i].rstrip('\n')

            player.Player.position[2] = stats[1]

            player.Player.position[0] = stats[4]
            player.Player.position[1] = stats[5]

            player.Player.health = stats[8]

            for i in range(0, 5):
                player.Player.items[i] = stats[i+11]

            for i in range(0, 3):
                player.Player.cookies[i] = stats[i+18]
