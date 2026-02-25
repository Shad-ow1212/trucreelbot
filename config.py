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
    "stat" : "commands.stat",
    "edit" : "commands.edit",
    "bissap" : "commands.bissap",
    "sixseven" : "commands.sixseven",
    "67" : "commands.sixseven",
    "admin" : "admincommands.admin"
}
ADMINCOMMANDS = {
    "test": "admincommands.test",
    "crève" : "admincommands.shutdown",
    "kys" : "admincommands.shutdown",
    "sleep" : "admincommands.shutdown",
    "reboot" : "admincommands.reboot",
    "reload" : "admincommands.reload",
}

SALUTATIONS = ["salut", "bonjour", "coucou", "bonsoir", "enchanté", "hewo", "bonjoir", "bonjoouj"]
REPONSES = ["salut", "bonjour", "coucou", "bonsoir", "re", "hey", "enchanté", "bonjoir", "bonjoouj"]

MOTSREACTIONS = {"npac": "npac",
                 "prout": "prout",
                 "femboy": "femboy"}