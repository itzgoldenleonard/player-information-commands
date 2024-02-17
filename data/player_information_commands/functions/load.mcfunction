#Adds a scoreboard objective that increments every time the player leaves
scoreboard objectives add pic.quits minecraft.custom:minecraft.leave_game

#for / commands
scoreboard objectives add help trigger
scoreboard objectives add info trigger
scoreboard objectives add news trigger
scoreboard objectives add rules trigger

tellraw @a "Player information commands has been succesfully setup\nRun /function player_information_commands:uninstall and delete the datapack folder to remove it"
