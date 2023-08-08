import numpy as np
import requests

def get_all_champ_data():
    response = requests.get("http://ddragon.leagueoflegends.com/cdn/13.5.1/data/en_US/champion.json")
    if response.status_code != 200: #200 means success
        raise Exception("Error getting champion data")
    return response.json()


class Champion:
    def __init__(self, name):
        self.name = name

        self.champ_armor_base = 0
        self.champ_armor_plvl = 0

        self.champ_mr_base = 0
        self.champ_mr_plvl = 0

        self.champ_hp_base = 0
        self.champ_hp_plvl = 0

        self.champ_atk_spd_base = 0
        self.champ_atk_spd_plvl = 0

        self.champ_dmg_base = 0
        self.champ_dmg_plvl = 0

    def set_champ_level(self, level):
        self.champ_armor_at_lvl = self.champ_armor_base + self.champ_armor_plvl * (level - 1)
        self.champ_mr_at_lvl = self.champ_mr_base + self.champ_mr_plvl * (level - 1)
        self.champ_hp_at_lvl = self.champ_hp_base + self.champ_hp_plvl * (level - 1)
        self.champ_atk_spd_at_lvl = self.champ_atk_spd_base + (self.champ_atk_spd_base * (self.champ_atk_spd_plvl/100 * (level - 1)))
        self.champ_ad_at_lvl = self.champ_dmg_base + self.champ_dmg_plvl * (level - 1)

    def __str__(self):
        return f"{self.name}:\n\tArmor: {self.champ_armor_at_lvl}\n\tMR: {self.champ_mr_at_lvl}\n\tHP: {self.champ_hp_at_lvl}\n\tAtk Spd: {self.champ_atk_spd_at_lvl}\n\tAD: {self.champ_ad_at_lvl}"


def get_specific_champ_data(champ_data):
    # champion_name = input("Enter Enemy Champion name: ")
    #TODO: remove this
    champion_name = "Aatrox"
    if champion_name in champ_data["data"]:
        champion_info = champ_data["data"][champion_name]
        champion = Champion(champion_name)
        champion.champ_armor_base = champion_info["stats"]["armor"]
        champion.champ_armor_plvl = champion_info["stats"]["armorperlevel"]
        champion.champ_mr_base = champion_info["stats"]["spellblock"]
        champion.champ_mr_plvl = champion_info["stats"]["spellblockperlevel"]
        champion.champ_hp_base = champion_info["stats"]["hp"]
        champion.champ_hp_plvl = champion_info["stats"]["hpperlevel"]
        champion.champ_atk_spd_base = champion_info["stats"]["attackspeed"]
        champion.champ_atk_spd_plvl = champion_info["stats"]["attackspeedperlevel"]
        champion.champ_dmg_base = champion_info["stats"]["attackdamage"]
        champion.champ_dmg_plvl = champion_info["stats"]["attackdamageperlevel"]
        # champion_level = int(input("Enter Enemy Champion level: "))
        champion.set_champ_level(18)
        return champion
    return None

def stuff(champ_data):
    # champion_name = input("Enter Enemy Champion name: ")
    #TODO: remove this
    champions = [] 
    for champion_name in champ_data["data"].keys():
        champion_info = champ_data["data"][champion_name]
        champion = Champion(champion_name)
        champion.champ_armor_base = champion_info["stats"]["armor"]
        champion.champ_armor_plvl = champion_info["stats"]["armorperlevel"]
        champion.champ_mr_base = champion_info["stats"]["spellblock"]
        champion.champ_mr_plvl = champion_info["stats"]["spellblockperlevel"]
        champion.champ_hp_base = champion_info["stats"]["hp"]
        champion.champ_hp_plvl = champion_info["stats"]["hpperlevel"]
        champion.champ_atk_spd_base = champion_info["stats"]["attackspeed"]
        champion.champ_atk_spd_plvl = champion_info["stats"]["attackspeedperlevel"]
        champion.champ_dmg_base = champion_info["stats"]["attackdamage"]
        champion.champ_dmg_plvl = champion_info["stats"]["attackdamageperlevel"]
        champion.set_champ_level(18)
        champions.append(champion)

    # print champion where champion name is Azir
    for champion in champions:
        if champion.name == "Azir":
            print(champion)

    sorted_champions = sorted(champions, key=lambda x: x.champ_atk_spd_at_lvl, reverse=False)
    print(sorted_champions[1])
    # for champion in champions:
    #     championdmg.append(champion.champ_ad_at_lvl)
    #     # if champion.champ_ad_at_lvl > highest_ad:
    #     #     highest_ad = champion.champ_ad_at_lvl
    #     #     highest_ad_champ = champion

    
    # # print(highest_ad_champ)
    # # print(highest_ad)
    
    # max_dmg = max(championdmg)

    # champmaxdmg = championdmg.index(max_dmg)    

    # print(champmaxdmg)
    # print(max_dmg)
    # print(champions[champmaxdmg])

def main():
    champ_data = get_all_champ_data()
    
    enemy_champs = []
    

    stuff(champ_data)

    # for i in range(1):
    #     enemy_champs.append(get_specific_champ_data(champ_data))

    # for champion in enemy_champs:
    #     print(champion)
    #     print(champion.champ_atk_spd_plvl)
    #     # print(champion.name)

if __name__ == "__main__":
    main()



#     ChampArmor[i] = ChampArmorBase + ChampArmorpLvl*(EnemyLvl-1)
#     ChampMR[i] = ChampMRBase + ChampMRpLvl*(EnemyLvl-1)
#     ChampHP[i] = ChampHPBase + ChampHPpLvl*(EnemyLvl-1)
#     ChampAtkSpd[i] = ChampAtkSpdBase + ChampAtkSpdpLvl*(EnemyLvl-1)
#     ChampAD[i] = ChampDmgBase + ChampDmgpLvl*(EnemyLvl-1)