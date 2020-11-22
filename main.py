import os
import crayons
import math
import time
crayons.enable()
directory_prefix = "/home/ian/Downloads/Avengers_Assemble/"
intro =  ('''      
                       _      __           _       _   
      /\/\   _____   _(_) ___/ _\ ___ _ __(_)_ __ | |_ 
     /    \ / _ \ \ / / |/ _ \ \ / __| '__| | '_ \| __|
    / /\/\ \ (_) \ V /| |  __/\ \ (__| |  | | |_) | |_ 
    \/    \/\___/ \_/ |_|\___\__/\___|_|  |_| .__/ \__|
                                            |_|        
                                    Author : Ian Wright
    ''')
print (f'{crayons.yellow(intro)}')
movie = f"{crayons.white('Avengers Assemble Season 1')}"
entries = os.listdir("/home/ian/Downloads/Avengers_Assemble/")
current_ep = len(entries)

print(f'{crayons.cyan("[ Movie ]")} {movie}\n{crayons.yellow("=====================================")}\n[ * ] Scanning directory for Last Episode Downloaded\n')
p=0
for episode in entries:
	file = f"Avengers.Assemble.S01E0{current_ep}.480p.WEB-DL.x264.TagName.mkv"
	file1 = f"Avengers.Assemble.S01E{current_ep}.480p.WEB-DL.x264.TagName.mkv"
	if file == entries[p] or file1 == entries[p]:
		current_ep += 1
	p+=1
	time.sleep(1)
	long_string = "="*p
	print(f"{crayons.cyan('[ * ]')} {crayons.yellow(long_string)}{crayons.cyan('>')} {crayons.white(math.floor(p*100/len(entries)))} %")
print(f"[ * ] Done scanning...[ Episode {current_ep-1} ] was last downloaded")

if current_ep == len(entries)+1:
	print("[ * ] All episodes were downloaded successfully.") 
else:
    episodes = []
    applications = ["wget", "vlc"]
    for x in range (current_ep,28):
	    episodes.append(x)
    print (f'[ * ] Detected remaining {len(episodes)-1} episodes on this server')

    print(f"[ * ] I'll begin by downloading episode {current_ep}")

    for number in range (current_ep, episodes[len(episodes)-1]):
	    print(f'[ * ] {crayons.yellow("Downloading... Episode")} {crayons.yellow(current_ep)}\n')

	    #asset = f"https://augax.co/Series/Avengers%20Assemble/S01/Avengers.Assemble.S01E0{current_ep}.480p.WEB-DL.x264.TagName.mkv"
	    asset = f"https://augax.co/Series/Avengers%20Assemble/S01/Avengers.Assemble.S01E{current_ep}.480p.WEB-DL.x264.TagName.mkv"
	    command = f"{applications[0]} -P {directory_prefix} {asset}"
	    
	    print(f'{asset}\n')
	    os.system(command)
	    current_ep += 1

    print('done... bye')
    #I am Iron Man, the suit and I are one
