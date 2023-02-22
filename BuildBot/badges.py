import discum, time 
token = "da_webhook" #  Your account token
guild_id = 'sunucuid'
channel_id = 'kanalid'
bot = discum.Client(token= token, log=None)




bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' members fetched')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()

def __get_badgess(flagss) -> list[str]:
    
        BADGESS = {
          #  1 << 0:  'Discord Employee',
          #  1 << 1:  'Partnered Server Owner',
           # 1 << 2:  'HypeSquad Events',
          #  1 << 3:  'Bug Hunter Level 1',
            #1 << 9:  'Early Supporter',
          #  1 << 10: 'Team User',
           # 1 << 12: 'System',
            #1 << 14: 'Bug Hunter Level 2',
            1 << 17: 'Early Verified Bot Developer',
            #1 << 18: 'Discord Certified Moderator'
        }

        badgess = []

        for badge_flag, badge_name in BADGESS.items():
            if flagss & badge_flag == badge_flag:
                badgess.append(badge_name)

        return badgess

with open('randomnamesa1.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badgess(temp)
            if len(z) != 0:
                badgess = ', '.join(z)
                file.write(f'ID: {id} | Username: {username} | Badges: {badgess} \n')
            


def __get_badgesss(flagsss) -> list[str]:
    
        BADGESSS = {
           # 1 << 0:  'Discord Employee',
          #  1 << 1:  'Partnered Server Owner',
            1 << 2:  'HypeSquad Events',
        #    1 << 3:  'Bug Hunter Level 1',
          #  1 << 9:  'Early Supporter',
       #     1 << 10: 'Team User',
           # 1 << 12: 'System',
          #  1 << 14: 'Bug Hunter Level 2',
         #   1 << 17: 'Early Verified Bot Developer',
           # 1 << 18: 'Discord Certified Moderator'
        }

        badgesss = []

        for badge_flag, badge_name in BADGESSS.items():
            if flagsss & badge_flag == badge_flag:
                badgesss.append(badge_name)

        return badgesss

with open('randomnamesa2.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badgesss(temp)
            if len(z) != 0:
                badgesss = ', '.join(z)
                file.write(f'ID: {id} | Username: {username} | Badges: {badgesss} \n')
            





def __get_badges(flags) -> list[str]:
    
        BADGES = {
           # 1 << 0:  'Discord Employee',
          #  1 << 1:  'Partnered Server Owner',
         #   1 << 2:  'HypeSquad Events',
        #    1 << 3:  'Bug Hunter Level 1',
            1 << 9:  'Early Supporter',
       #     1 << 10: 'Team User',
           # 1 << 12: 'System',
          #  1 << 14: 'Bug Hunter Level 2',
         #   1 << 17: 'Early Verified Bot Developer',
           # 1 << 18: 'Discord Certified Moderator'
        }

        badges = []

        for badge_flag, badge_name in BADGES.items():
            if flags & badge_flag == badge_flag:
                badges.append(badge_name)

        return badges

with open('randomnamesa.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badges(temp)
            if len(z) != 0:
                badges = ', '.join(z)
                file.write(f'ID: {id} | Username: {username} | Badges: {badges} \n')
            
            
            
            
            
def __get_badgessz(flagssz) -> list[str]:
    
        BADGESSZ = {
            1 << 0:  'Discord Employee',
            1 << 1:  'Partnered Server Owner',
         #   1 << 2:  'HypeSquad Events',
            1 << 3:  'Bug Hunter Level 1',
       #     1 << 9:  'Early Supporter',
       #     1 << 10: 'Team User',
           # 1 << 12: 'System',
            1 << 14: 'Bug Hunter Level 2',
         #   1 << 17: 'Early Verified Bot Developer',
            1 << 18: 'Discord Certified Moderator'
        }

        badgessz = []

        for badge_flag, badge_name in BADGESSZ.items():
            if flagssz & badge_flag == badge_flag:
                badgessz.append(badge_name)

        return badgessz

with open('randomnamesa4.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badgessz(temp)
            if len(z) != 0:
                badgessz = ', '.join(z)
                file.write(f'ID: {id} | Username: {username} | Badges: {badgessz} \n')
            