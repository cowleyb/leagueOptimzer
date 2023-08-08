import requests


def get_game_versions():
      response = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")

      if response.status_code == 200:
            return response.json()
      else: 
            print("Failed to get version")

def main():
    game_versions = get_game_versions()

    print(game_versions)
  

if __name__ == "__main__":
    main()