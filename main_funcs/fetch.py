import re, os
from subprocess import Popen, PIPE

import pbfetch.main_funcs.horizontal_formatter as hf
from pbfetch.main_funcs.stats import stats

# init stats using keywords for configuration in .conf
file = os.path.join("src", "pbfetch", "config", "config.txt")
stats_dict = stats()


def get_console_width():
    console_width = Popen(["tput", "cols"], stdout=PIPE)
    console_width = int(float(console_width.communicate()[0].strip()))

    return console_width


def fetch():
    # read config and exit if empty
    with open(file, "r") as config:
        content = config.read()
        if content:
            fetch_data = content
        else:
            print("You must insert something in the config! Try some ascii art UwU")
            exit()

    # omit comments from output
    for line in fetch_data.split("\n"):
        # catch and release comments using # notation
        regex_match = re.search("#.*$", line)
        if not regex_match:
            continue
        fetch_data = fetch_data.replace(regex_match.group(), "")

        # # replace stat keywords with stat data
        # for keyword in stats_dict.keys():
        #     # associate stat keyword with its respective value
        #     stat = stats_dict[keyword]
        #     if stat is None:
        #         continue
        #     stat = str(stat)

        # format char differences for keyword and respective value
    fetch_data = hf.replace_dictionary(fetch_data, stats_dict, get_console_width())

    # # TODO: make this optional from the config.txt
    # # clear the terminal
    # os.system("cls" if os.name == "nt" else "clear")

    # finally print fetch to terminal, format only from the right
    return fetch_data.rstrip()
