from autocommands.timer import Timer
TIMERS = [Timer(50, "J'ai perdu")]

PREFIX = "+"
OWNER_ID = 712600626223120478

#colors :
ERROR = 0xFFA596
CONFIRMATION = 0x98FF96
INFO = 0x96E3FF

#dico de toutes les commandes dispo
COMMANDS = {
    "test": "commands.test",
    "crève" : "commands.shutdown",
    "kys" : "commands.shutdown",
    "sleep" : "commands.shutdown",
    "reboot" : "commands.reboot",
    "stat" : "commands.stat",
    "edit" : "commands.edit",
    "reload" : "commands.reload",
    "bissap" : "commands.bissap",
    "sixseven" : "commands.sixseven",
    "67" : "commands.sixseven"
}

SALUTATIONS = ["salut", "bonjour", "coucou", "bonsoir", "enchanté", "hewo", "bonjoir", "bonjoouj"]
REPONSES = ["salut", "bonjour", "coucou", "bonsoir", "re", "hey", "enchanté", "bonjoir", "bonjoouj"]

MOTSREACTIONS = {"npac": "npac",
                 "prout": "prout",
                 "femboy": "femboy"}