from project_06.player import Player  # need to set the correct folder as resource root

class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for cur_player in self.players:
            if cur_player.name == player_name:
                cur_player.guild = 'Unaffiliated'
                self.players.remove(cur_player)
                return f"Player {cur_player.name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {self.name}\n" + "\n".join([cur_player.player_info() for cur_player in self.players])


if __name__ == '__main__':
    player = Player("George", 50, 100)
    print(player.add_skill("Shield Break", 20))
    print(player.player_info())
    guild = Guild("UGT")
    print(guild.assign_player(player))
    print(guild.guild_info())

