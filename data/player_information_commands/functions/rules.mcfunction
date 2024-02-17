scoreboard players enable * rules

#page 1
tellraw @a[scores={rules=1}] {"text":"-------------=== rules page 1 ===-------------","bold":true,"color":"#F6DE41"}
tellraw @a[scores={rules=1}] ["",  {    "text":"Breaking these rules could get you punished",    "bold":true,    "color":"green"  },  "\n",  {    "text":"Rule 1:",    "bold":true,    "color":"aqua"  },  {    "text":" Don't break the rules",    "color":"aqua"  },  "\n",  {    "text":"Rule 2: ",    "bold":true,    "color":"aqua"  },  {    "text":"Griefing isnt cool, it might be allowed, but it probably isnt because that would be kinda weird",    "color":"aqua"  }]
tellraw @a[scores={rules=1}] ["",{"text":"-------------=== ","bold":true,"color":"#F6DE41"},{"text":"[Prev]","underlined":true,"color":"gray"},{"text":" | ","bold":true,"color":"#F6DE41"},{"text":"[Next]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger rules set 2"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the next page"]}},{"text":" ===-------------","bold":true,"color":"#F6DE41"}]

#page 2
tellraw @a[scores={rules=2}] {"text":"-------------=== rules page 2 ===-------------","bold":true,"color":"#F6DE41"}
tellraw @a[scores={rules=2}] ["",  {    "text":"Rule 3: ",    "bold":true,    "color":"aqua"  },  {    "text":"These aren't real rules",    "color":"aqua"  },  "\n",  {    "text":"Rule 4: ",    "bold":true,    "color":"aqua"  },  {    "selector":"@a[scores={rules=2}]",    "color":"blue"  },  {    "text":" should probably change these",    "color":"blue"  }]
tellraw @a[scores={rules=2}] ["",{"text":"-------------=== ","bold":true,"color":"#F6DE41"},{"text":"[Prev]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger rules set 1"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the previous page"]}},{"text":" | ","bold":true,"color":"#F6DE41"},{"text":"[Next]","underlined":true,"color":"gray"},{"text":" ===-------------","bold":true,"color":"#F6DE41"}]
tellraw @a[scores={rules=2}] ["",{"text":"Generated by the ","italic":true,"color":"gray"},{"text":"Player-information-commands","italic":true,"underlined":true,"color":"gray","clickEvent":{"action":"open_url","value":"https://github.com/itzgoldenleonard/Player-information-commands"},"hoverEvent":{"action":"show_text","contents":["Click to view the source code (it's free software)"]}},{"text":" datapack\nMade by ","italic":true,"color":"gray"}, {"text": "these people", "italic":true, "color":"gray", "underlined":true, "hoverEvent":{"action":"show_text","contents":["Ava Drumm\n"]}}]

scoreboard players set @a rules 0