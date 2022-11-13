import time
from colorama import Fore, Back, Style
animation = [
"[        ]",
"[g       ]",
"[ng      ]",
"[ing     ]",
"[ling    ]",
"[lling   ]",
"[illing  ]",
"[billing ]",
"[ billing]",
"[  billin]",
"[   billi]",
"[    bill]",
"[     bil]",
"[      bi]",
"[       b]",
"[        ]",
"[        ]"
]

notcomplete = True

i = 0

while notcomplete:
    print(Fore.CYAN +animation[i % len(animation)], end='\r')
    time.sleep(0.1)
    i += 1