import os
from time import sleep
from mastodon import Mastodon

mj_token = os.environ["MJ"]





mastodon = Mastodon(
    access_token = mj_token,
    api_base_url = 'https://sb.jeuseweeder.xyz'
)
while True:
    total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    cpu_usage = str(round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()),2))
    status_to_post = "Let's see what we are using hee-hee:\nRAM: " + str(round((used_memory/total_memory) * 100, 2)) + "%\nCPU:" + str(cpu_usage) + "%"
    mastodon.toot(status_to_post)
    sleep(20)
