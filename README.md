# About
Player information commands is a server focused datapack that adds the commands `/trigger help`, `rules`, `info` and `news`, as well as a greeting message that is displayed when you join the server. The contents of all the messages/commands is completely customizable. Your messages can contain all the formatting that's possible in minecraft chat (bold text, colors, hyperlinks etc.), they can contain multiple pages and there's support for disabling any of the commands.

The commands sadly have to be prefixed by /trigger, that's just a limitation of datapacks, but the upside is that it works on **all** 1.13+ minecraft servers

# Installation and setup
## GUI
The installation is pretty much like any other datapack.

- Download the file from the *'Releases'* tab
- Place it in the datapacks folder of your world
- And decompress it using a tool like *tar* or *kde ark*

## CLI
On a real server you will likely have to do it using a command line.

First obtain the link of the latest release by going to the *'Releases'* tab, under assets the file should be called **Player-information-commands.tar.gz**, right click on it and click copy link address.
```bash
cd <serverfolder>/world/datapacks
wget <link>
tar -xf Player-information-commands.tar.gz
rm Player-information-commands.tar.gz
```
Now log onto the server and enable it with `/datapack enable "file/Player-information-commands"`

# Setup
The chat content that the players see when logging into the server (the greeting) as well as when using the commands, is completely customizable by you (the server admin). The extracted datapack folder contains 4 **.json** files, this is where you write the custom content, in the json text format used by minecraft.

If you already know the format, great, write whatever you want. If you don't know the format this website: [minecraftjson.com](https://www.minecraftjson.com/) is a great resource for generating the text. Otherwise I've found the [minecraft wikis article](https://minecraft.fandom.com/wiki/Raw_JSON_text_format#Java_Edition) on the subject is a decent way to learn it if you already know a bit about json.

In order to create multiple pages use this symbol: ↡ to seperate the pages. In order to disable a command simply delete all the contents of the file and save it as empty.

Once you have entered all your desired text, run the python script called **script.py** by opening the folder in a terminal, and running the command `python3 script.py`. Now all your custom text will show up in game.

# Contributing
You can contribute with code by making a pull request and adding your name to the CONTRIBUTORS file (remember a \\n after your name)

If you don't code, you can still contribute by telling other people about this datapack, or making feature suggestions and bug reports in the 'Issues' tab on Github

# Roadmap
[See the dedicated document](https://github.com/itzgoldenleonard/Player-information-commands/blob/main/ROADMAP.md)
