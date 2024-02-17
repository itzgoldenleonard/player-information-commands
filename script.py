"""This is the script that takes the contents of the json files, parses it and throws it correctly into the mcfunction files so that everything works as expected"""
import os.path
import argparse

# this makes the help message as well as handles the command line arguments
parser = argparse.ArgumentParser(description='Generates the greeting and the command messages from the .json files')
parser.add_argument('-o', '--omit-page-controls', action='store_false', help='Include to avoid generating page controls')
generate_page_controls: bool = parser.parse_args().omit_page_controls
if not generate_page_controls:
    print("detected -o flag, disabling page headers and footers")


greeting = {  # dictionaries are awesome
    "path": "greeting.json",
    "function_path": "data/player_information_commands/functions/greeting.mcfunction",
    "objective": "pic.quits",
    "raw_string": "",
    "parsed_string": [],
    "function_content": ""
}

help = {
    "path": "help.json",
    "function_path": "data/player_information_commands/functions/help.mcfunction",
    "objective": "help",
    "raw_string": "",
    "parsed_string": [],
    "function_content": ""
}

info = {
    "path": "info.json",
    "function_path": "data/player_information_commands/functions/info.mcfunction",
    "objective": "info",
    "raw_string": "",
    "parsed_string": [],
    "function_content": ""
}

news = {
    "path": "news.json",
    "function_path": "data/player_information_commands/functions/news.mcfunction",
    "objective": "news",
    "raw_string": "",
    "parsed_string": [],
    "function_content": ""
}

rules = {
    "path": "rules.json",
    "function_path": "data/player_information_commands/functions/rules.mcfunction",
    "objective": "rules",
    "raw_string": "",
    "parsed_string": [],
    "function_content": ""
}

def fix_line_endings(string):
    """Remove the line break and tab characters."""
    fixed_string = string.replace("\n", "")
    fixed_string = fixed_string.replace("\t", "")
    return fixed_string

LINK_TO_SOURCE: str = 'https://github.com/itzgoldenleonard/Player-information-commands'
AUTHORS: str
with open('CONTRIBUTORS') as file:
    AUTHORS = fix_line_endings(file.read()) # insert the names of the contributors into a string for later use

file.close()

def load_raw_string(dict):
    """Insert the content of a file into its dictionary."""
    if not os.path.isfile(dict["path"]): #throws an error message if the path doesnt lead to a file
        print('Error: ' + dict["path"] + ' does not exist')

    else:
        with open(dict["path"]) as file:
            dict["raw_string"] = file.read() #opens the file and loads the whole thing into the raw_string string

        file.close() #I dont know if this is neccecary
        dict["raw_string"] = fix_line_endings(dict["raw_string"])
        #print(dict["raw_string"]) #for debugging


def generate_command_footer(dict, max_pages, current_page):
    """Generate the footer with page controls and credits."""
    if max_pages == 1:
        #the page footer if theres only one page (doesnt have next page buttons)
        dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '{"text":"--------------------------------------------","bold":true,"color":"#F6DE41"}\n'
    else:
        if current_page == 0:
            #on the first page where the prev button is greyed out
            dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '["",{"text":"-------------=== ","bold":true,"color":"#F6DE41"},{"text":"[Prev]","underlined":true,"color":"gray"},{"text":" | ","bold":true,"color":"#F6DE41"},{"text":"[Next]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger ' + dict["objective"] + ' set ' + str(current_page + 2) + '"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the next page"]}},{"text":" ===-------------","bold":true,"color":"#F6DE41"}]\n'
        elif current_page+1 == max_pages:
            #on the last page where the next button is greyed out
            dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '["",{"text":"-------------=== ","bold":true,"color":"#F6DE41"},{"text":"[Prev]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger ' + dict["objective"] + ' set ' + str(current_page) + '"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the previous page"]}},{"text":" | ","bold":true,"color":"#F6DE41"},{"text":"[Next]","underlined":true,"color":"gray"},{"text":" ===-------------","bold":true,"color":"#F6DE41"}]\n'
        else:
            #on normal pages
            dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '["",{"text":"-------------=== ","bold":true,"color":"#F6DE41"},{"text":"[Prev]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger ' + dict["objective"] + ' set ' + str(current_page) + '"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the previous page"]}},{"text":" | ","bold":true,"color":"#F6DE41"},{"text":"[Next]","underlined":true,"color":"green","clickEvent":{"action":"run_command","value":"/trigger ' + dict["objective"] + ' set ' + str(current_page + 2) + '"},"hoverEvent":{"action":"show_text","contents":["Click to scroll to the next page"]}},{"text":" ===-------------","bold":true,"color":"#F6DE41"}]\n'

    if current_page+1 == max_pages: #link to the source (has to be there because of the license) it only appears on the last page
        dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '["",{"text":"Generated by the ","italic":true,"color":"gray"},{"text":"Player-information-commands","italic":true,"underlined":true,"color":"gray","clickEvent":{"action":"open_url","value":"' + LINK_TO_SOURCE + '"},"hoverEvent":{"action":"show_text","contents":["Click to view the source code (it\'s free software)"]}},{"text":" datapack\\nMade by ","italic":true,"color":"gray"}, {"text": "these people", "italic":true, "color":"gray", "underlined":true, "hoverEvent":{"action":"show_text","contents":["' + AUTHORS + '"]}}]'



def generate_command_header(dict, max_pages, current_page):
    """Generate the header where it says what command you just executed."""
    if max_pages == 1:
        dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '{"text":"----------------=== ' + dict["objective"] + ' ===----------------","bold":true,"color":"#F6DE41"}\n'
    else:
        dict["function_content"] += '\n#page ' + str(current_page + 1) + '\ntellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + '{"text":"-------------=== ' + dict["objective"] + ' page ' + str(current_page + 1) + ' ===-------------","bold":true,"color":"#F6DE41"}\n'



def generate_command(dict):
    """Combine everything into the final commands and insert those into the mcfunction files."""
    load_raw_string(dict)
    dict["parsed_string"] = dict["raw_string"].split("↡") #splits the different pages into different entries in the parsed_string list

    max_pages = len(dict["parsed_string"])

    #this part actually generates the file contents
    dict["function_content"] = 'scoreboard players enable * ' + dict["objective"] + '\n'

    for current_page in range(max_pages):
        #page header
        if generate_page_controls == True:
            generate_command_header(dict, max_pages, current_page)

        #this is the user inputted pages
        dict["function_content"] += 'tellraw @a[scores={' + dict["objective"] + '=' + str(current_page + 1) + '}] ' + dict["parsed_string"][current_page] + '\n'

        #page footer
        if generate_page_controls:
            generate_command_footer(dict, max_pages, current_page)

    dict["function_content"] += '\n\nscoreboard players set @a ' + dict["objective"] + ' 0'
    #now we're not generating file content anymore

    file = open(dict["function_path"], "w") #writes the function_content to the actual file
    if dict["parsed_string"] != ['']:
        file.write(dict["function_content"])
    else:
        print(dict["path"] + " is empty, disabling the command")
        file.write("")
    file.close()


def generate_greeting():
    """Generate the greeting message and insert into the mcfunction file."""
    load_raw_string(greeting)

    greeting["function_content"] = '''
    tellraw @a[scores={pic.quits=1..}] ''' + greeting["raw_string"] + '''
    scoreboard players set @a[scores={pic.quits=1..}] pic.quits 0
    ''' #the function_content is what will end up in the mcfunction file, its just the code but with the parsed_string injected into the tellraw command

    file = open(greeting["function_path"], "w") #writes the function_content to the actual file
    file.write(greeting["function_content"])
    file.close()


#actually runs the code
generate_greeting()
generate_command(help)
generate_command(info)
generate_command(news)
generate_command(rules)
