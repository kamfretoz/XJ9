#######################################
## Customizeable Error Message Quote ##
#######################################

error_quotes = [
    "Values of B will give rise to dom.",
    "FATAL system error #nnnn CAUSE: We should never get here!",
    "OHHHH…. I give up Core dumped",
    "COMPILER UNABLE TO ABORT",
    "AN ATTEMPT WAS MADE TO WRITE BEYOND THE MAXIMUM ASSIGNED SPACE FOR A MASS STORAGE FILE. AN ATTEMPT WAS MADE TO EXPAND A MASS STORAGE FILE BEYOND THE MAXIMUM ASSIGNED SPACE. A READ FUNCTION FOR A MASS STORAGE FILE SPECIFIED AN ADDRESS (WORD 5 OF THE I/O PACKET) THAT IS BEYOND THE MAXIMUM ASSIGNED SPACE. A READ OR WRITE FUNCTION FOR A WORD-ADDRESSABLE MASS STORAG FILE SPECIFIED A MASS STORAGE ADDRESS (WORD 5 OF THE I/O PACKET) AND A TOTAL DATA COUNT. WHEN THE MASS STORAGE ADDRESS IS ADDED TO THE TOTAL DATA COUNT, THE RESULTING ENDING MASS STORAGE ADDRESS IS GREATER THAN 2*/35-1. A READ OR WRITE FUNCTION FOR A SECTOR-FORMATTED MASS STORAGE FILE SPECIFIED A MASS STORAGE ADDRESS (WORD 5 OF THE I/O PACKET) THAT IS GREATER THAN 2*/30-1. ADI ONLY: REFERENCE ATTEMPTED BEYOND THE ASSIGNED FILE WHEN THE FILE IS CONFIGURED AS A FH-432 OR FH-1782 DRUM.",
    "ERROR: A really big FUCK UP has been detected !!",
    "Constantly writing while seeking..",
    "Momentaraly writing while reading..",
    "initstate: not enough state (%d bytes) with which to do jack; ignored.",
    "Keyboard not present, press any key",
    "You lied to me when you told me this was a program",
    "PROGRAMMER GOOFED . . . YOU SHOULD NEVER SEE THIS MESSAGE",
    "YOU CAN’T DO THAT!",
    "Man the Lifeboats! Women and children first!",
    "$ make :== $ sys$system:teco32 make\n$ make love \nNot war?",
    "That makes 100 errors; please try again.",
    "You can now delete more, or insert, or whatever.",
    "Sorry, I don’t know how to help in this situation.",
    "Maybe you should try asking a human?",
    "Sorry, I already gave what help I could…",
    "An error might have occurred before I noticed any problems.",
    "If all else fails, read the instructions.",
    "This can’t happen.",
    "I’m broken. Please show this to someone who can fix can fix",
    "I can’t go on meeting you like this.",
    "One of your faux pas seems to have wounded me deeply.. in fact, I’m barely conscious. Please fix it and try again.",
    "Interruption",
    "You rang?",
    "IMPOSSIBLE.",
    "NONEXISTENT.",
    "ETC.",
    "BAD.",
    "A funny symbol that I can’t read has just been input.  Continue, and I’ll forget that it ever happened.",
    "I suspect you’ve forgotten a `]’, causing me to apply this control sequence to too much text. How can we recover? My plan is to forget the whole thing and hope for the best.",
    "I dddon’t go any higher than filll.",
    "Dimensions can be in units of em, ex, in, pt, pc, cm, mm, dd, cc, bp, or sp; but yours is a new one!",
    "Something Rotten in Denmark, Interp Stack Not ALigned",
    "<Assorted DEC ID fruitcake> ILLEGAL ERROR",
    "bad magic number",
    "very funny",
    "You can’t do that in horizontal mode.",
    "COMPILER THWARTED",
    "Keyboard error or no keyboard present. Press F1 to continue.",
    "Argument is bletchful.",
    "Guru Meditation",
    "lint’s little mind is blown.",
    "Hot Damn! You need more ram!",
    "String literal too long (I let you have 512 characters, that’s 3 more than ANSI said I should)",
    "And the lord said, ‘lo, there shall only be case or default labels inside a switch statement’a typedef name was a complete surprise to me at this point in your program",
    "You can’t modify a constant, float upstream, win an argument with the IRS, or satisfy this compiler",
    "Can’t cast a void type to type void (because the ANSI spec. says so, that’s why)",
    "Huh ?",
    "can’t go mucking with a ‘void *’",
    "This label is the target of a goto from outside of the block containing this label AND this block has an automatic variable with an initializer AND your window wasn’t wide enough to read this whole error message",
    "Call me paranoid but finding ‘/*’ inside this comment makes me suspicious",
    "Symbol table full – fatal heap error; please go buy a RAM upgrade from your local Apple dealer",
    "It seem you are trying to check the output from a word-processor. Not only does this not make sense, but you would probably damage the file",
    "if you tried so I am not going to let you do this!",
    "It looks like the active file is messed up. Contact your news administrator and leave the bogus groups alone, and they may come back to normal. Maybe.",
    "Attention K-Mart shoppers: Blue Light special in out SYSTEM UTILITIES department. for the next 10 days we will be taking requests for the utilities that you think should be here. Thank you again for shopping K-Mart.",
    "Things are not looking good!",
    "I didn’t think this set of error conditions could ever happen",
    "Now deleting all files. Goodbye",
    "WARNING: 54 – PROGRAM NOT RECURSIVE",
    "Help is not available for you.",
    "Masscomp C compiler:Insane structure member list",
    "User Error: An unknown error has occurred in an unidentified program while executing an unimplemented function at an undefined address. Correct error and resubmit.",
    "Liar, Liar! Pants on Fire!",
    "Error: Success",
    "Something Happened but i don't know what",
    "Your expression has defeated me",
    "Unused error message #xxx",
    "You wascal wabbit! Wandering wizards won’t win",
    "F",
    "Who are you ?",
    "Holy PH, Batman, the buffer’s missing!",
    "The impossible has happened!",
    "Somethings amiss — no @ or % in arpafix",
    "~h: no can do!?",
    "Weird magic happens here",
    "Too much sourcing going on.",
    "metoo",
    "$ man fish",
    "$ man overboard\nBUGS: No life raft",
    "Error #1: Power supply not found",
    "ERROR 0: POWER NOT ON",
    "FORTRAN FATAL INTERNAL ERROR FATAL COMPILER DAMAGE REPORT FOLLOWS",
    "?Invalid Character At Terminal — Please Go Away",
    "?Unibus timeout — send in a new quarterback",
    "?Ouch, That HURTS!",
    "You must be joking.",
    "Oops! Error while handling error!",
    "Can’t find wicked faraway objects.",
    "Can’t fit 27″ tape through 25″ door.",
    "minor alarm",
    "major alarm",
    "critical alarm",
    "PROGRAM FILE DESTROYED. THE PROGRAM HAS BEEN ABORTED DUE TO INCONSISTENCIES IN THE INFORMATION GENERATED BY THE VULCANIZER. THE DISC COPY OF THE PROGRAM MAY HAVE BEEN DESTROYED OR THE PROGRAM MAY NOT HAVE BEEN RE-VULCANIZED AFTER A MAJOR SYSTEM RELEASE. IN ANY CASE RE-VULCANIZE THE PROGRAM (RLIBS ALSO).",
    "YOU JUST TRIED TO FAKE-OUT MOTHER NATURE, AND SHE CAUGHT YOU! SUPER-VULCAN NOW HAS YOUR NAME ON HIS ENEMY LIST, AND YOU CAN BE CERTAIN THAT FUTURE ATTEMPTS TO RESOURCE LFN 0,3,OR 6 WILL RESULT IN YOUR BEING ABORTED, SPINDLED, MANGLED, FOLDED, PUNCHED, DELETED, AND DEALLOCATED.",
    "AN ATTEMPT HAS BEEN MADE TO VULCANIZE A REAL-TIME, MONITOR, OR NRH TYPE PROGRAM, OR A PROGRAM WITH HIGH ACCESS, ACCOUNTING FILE ACCESS, OR SUB-SYSTEM ACCESS. THE VULCANIZE REQUEST IS IGNORED BECAUSE THE USER DOES NOT HAVE ACCESS TO GENERATE SUCH A PROGRAM."
    "NO ACCESS FOR $TOAD SERVICE A USER PROGRAM MADE A CALL TO A $TOAD SERVICE AND THE USER DOES NOT HAVE THE PROPER ACCESS TO BIT TO USE THAT SERVICE. ACCESS RESTRICTIONS ARE PLACED ON THE $TOADS SERVICES IN GENERAL, AND $CPRIOR, $PABORT, AND $SUSP FOR INDIVIDUAL RESTRICTIONS.",
    "WARNING: FILE GENERATED THE FILE WHICH WAS SPECIFIED AS THE ‘COPY TO’ OR DESTINATION FILE WAS NOT THERE AND WAS THEREFORE GENERATED BY JOBCONTROL. IF YOU DID NOT MEAN TO COPY TO A NEW FILE ELIMINATE THE FILE.",
    "ERROR 1164 HOW IN THE HELL DID YOU GET HERE",
    "Invalid command. Feel ashamed for yourself and try again.",
    "Hey are you talking to me? Try again!",
    "Shut ‘er down, Clancy, she’s a-pumpin’ mud!",
    "Out of order",
    "file has bad magic.",
    "I didn’t think this set of error conditions could ever happen",
    "Hi Linda! We wondered how long it would take, for you to mess up this bad.",
    "It looks like the active file is messed up. Contact your news administrator and leave the bogus groups alone, and they may come back to normal. Maybe.",
    "if you tried so I am not going to let you do this!",
    "Symbol table full – fatal heap error; please go buy a RAM upgrade from your local Apple dealer",
    "This label is the target of a goto from outside of the block containing this label AND this block has an automatic variable with an initializer AND your window wasn’t wide enough to read this whole error message",
    "Are you lonely?",
    "Tsk tsk? Have I been a bad computer?",
    "line 2706 compiler error: schain botch",
    "Go away. You don’t exist.",
    "This application has violated system integrity and must be terminated.",
    "Where did you learn to type?",
    "Are you on drugs?",
    "stty: unknown mode: doofus",
    "It can only be attributed to human error.",
    "What, what, what, what, what, what, what, what, what, what?",
    "You do that again and see what happens...",
    "Speak English you fool --- there are no subtitles in this scene.",
    "My pet ferret can type better than you!",
    "Maybe if you used more than just two fingers...",
    "I've seen penguins that can type better than that.",
    "Security Alert – Moving cursor is not as safe as you thought.",
    "Out of memory: Kill process, score, or sacrifice child.",
    "Keyboard not found. Press a button on the non-existent keyboard to fix it.",
    "Something happened, but I'm not telling you what.",
    "Error displaying the error message you're looking at right now.",
    "Error: Beats the hell out of me. ",
    "Can't save X for reason Y.",
    "Some unexplained things are happening right now.",
    "*Suspended in Disbelief*",
    "Whoah. WHOAH! Wow-wow-wow-wow-wow",
    "Wubba Lubba dub dub",
    "Don't mind this message, it's designed to annoy you.",
    "Hadouken!",
    "Swiper no swiping",
    "Fatality",
    "Who you gonna call?",
    "I wanna be the very best",
    "Move Along, nothing to see here.",
    "Task failed successfully.",
    "The Operation Failed Successfully.",
    "Error messages are the worst, am I right?",
    "You don't care about me, don't you?",
    "stop reading this message and do something useful like write german haikus in capital letters or idk",
    "Who you gonna catch?",
    "You wanna touch it, don't ya?",
    "NO FUN ALLOWED.",
    "You are trying to do something useful, for this you require a proper computer, and a mouse with more than one button. Ask an adult to help you buy one.",
    "We have detected that you are drunk, beyond the point of responsible posting - and that you •may• regret this post tomorrow. Would you like to save as a draft for the morning?",
    "OOPS: child ded",
    "These haiku circulated 20 years back. Things haven’t changed much.",
    "You ask far too much.",
    "I am the Blue Screen of Death",
    "No one hears your screams.",
    "Yesterday it worked, Today it is not working.",
    "Lame.",
    "E0001",
    "Something happened.",
    "Hell is empty",
    "Catastrophic Failure",
    "This is NOT what i expected!",
    "Stop breaking me! :(",
    "Oyasumi...",
    "I did not succumb.",
    "You think this is funny?!",
    "im scared mom hold my hand",
    "Watch the road, there are kids around here!",
    "Say the magic word!",
    "no... No... NO... NOOOOOOOOOOOOOO!!!!!!!!!!!"
]


# Hackerman jargon stuff
jargonWordPool = [["TCP", "HTTP", "SDD", "RAM", "GB", "CSS", "SSL", "AGP", "SQL", "FTP", "PCI", "AI", "ADP", "RSS", "XML", "EXE", "COM", "HDD", "THX", "SMTP", "SMS", "USB", "PNG", "PHP", "UDP", "TPS", "RX", "ASCII", "CD-ROM", "CGI", "CPU", "DDR", "DHCP", "BIOS", "IDE", "IP", "MAC", "MP3", "AAC", "PPPoE", "SSD", "SDRAM", "VGA", "XHTML", "Y2K", "GUI"],
                ["auxiliary", "primary", "back-end", "digital", "open-source", "virtual", "cross-platform", "redundant", "online", "haptic", "multi-byte", "bluetooth", "wireless", "1080p", "neural", "optical", "solid state", "mobile", "unicode", "backup", "high speed", "56k", "analog", "fiber optic", "central", "visual", "ethernet"],
                ["driver", "protocol", "bandwidth", "panel", "microchip", "program", "port", "card", "array", "interface", "system", "sensor", "firewall", "hard drive", "pixel", "alarm", "feed", "monitor", "application", "transmitter", "bus", "circuit", "capacitor", "matrix", "address", "form factor", "array", "mainframe", "processor", "antenna", "transistor", "virus", "malware", "spyware", "network", "internet"],
                ["back up", "bypass", "hack", "override", "compress", "copy", "navigate", "index", "connect", "generate", "quantify", "calculate", "synthesize", "input", "transmit", "program", "reboot", "parse", "shut down", "inject", "transcode", "encode", "attach", "disconnect", "network"],
                ["backing up", "bypassing", "hacking", "overriding", "compressing", "copying", "navigating", "indexing", "connecting", "generating", "quantifying", "calculating", "synthesizing", "inputting", "transmitting", "programming", "rebooting", "parsing", "shutting down", "injecting", "transcoding", "encoding", "attaching", "disconnecting", "networking"]
            ]
jargonConstructs = ["If we {3} the {2}, we can get to the {0} {2} through the {1} {0} {2}!", "We need to {3} the {1} {0} {2}!", "Try to {3} the {0} {2}, maybe it will {3} the {1} {2}!", "You can't {3} the {2} without {4} the {1} {0} {2}!", "Use the {1} {0} {2}, then you can {3} the {1} {2}!", "The {0} {2} is down, {3} the {1} {2} so we can {3} the {0} {2}!", "{4} the {2} won't do anything, we need to {3} the {1} {0} {2}!", "I'll {3} the {1} {0} {2}, that should {3} the {0} {2}!", "My {0} {2} is down, our only choice is to {3} and {3} the {1} {2}!", "They're inside the {2}, use the {1} {0} {2} to {3} their {2}!", "Send the {1} {2} into the {2}, it will {3} the {2} by {4} its {0} {2}!"]


statuses = ["this Society.",
            "光",
            "your mom",
            "from the distance...",
            "deez giga nuts",
            "𝓻𝓮𝓼𝓸𝓷𝓪𝓷𝓬𝓮 𝓬𝓪𝓼𝓬𝓪𝓭𝓮"
        ]
