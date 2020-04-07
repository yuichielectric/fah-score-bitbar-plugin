#!/usr/bin/env python3


# <bitbar.title>Folding@Home score</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>Yuichi Tanaka</bitbar.author>
# <bitbar.author.github>yuichielectric</bitbar.author.github>
# <bitbar.desc>Displays the score of your Folding@Home account</bitbar.desc>
# <bitbar.image>https://raw.githubusercontent.com/jakevossen5/apodbitbar/master/example.png</bitbar.image>
# <bitbar.dependencies>python3</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/jakevossen5/apodbitbar/tree/master</bitbar.abouturl>

import json
import urllib.request


user_account = 'yuichielectric'


def separator(num):
    return "{:,}".format(num)


url = 'https://stats.foldingathome.org/api/donor/' + user_account
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = json.load(res)
    print("F@h " + separator(body["credit"]))
    print('---')
    top = body["rank"] / body["total_users"] * 100
    print("Rank: " + separator(body["rank"]) +
          " / " + separator(body["total_users"]))
    print("Top %.02f %%" % top)
