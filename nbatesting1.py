import pandas
import nbaapi
from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamgamelog
from nbaapi import nba_teamgame
from nbaapi import nba_gamestats
from nba_api.stats.endpoints import boxscoresummaryv2

if __name__ == "__main__":
    
     
    ##nbag = nba_teamgame(nbateam, nbaseason)
    ##nbag.team_id()
    ##print(nbag.team_gamelist())
    
    ##nbatwo = nba_gamestats(nbagameid)
    ##print(nbatwo.nbagame_info())
    ##print(nbatwo.nbagame_summary())
    nbateam1="Chicago Bulls"
    nbaseason1="2010"
    nbagameid1="0021001174"
    nbag2 = nba_teamgame(nbateam1, nbaseason1)
    nbag2.team_id()
    print(nbag2.team_gamelist())
    
    nbatwo1 = nba_gamestats(nbagameid1)
    print(nbatwo1.nbagame_info())
    print(nbatwo1.nbagame_summary()) 


    nbateam2="Boston Celtics"
    nbaseason2="2017"
    nbagameid2="0021700001"
    nbag3 = nba_teamgame(nbateam2, nbaseason2)
    nbag3.team_id()
    print(nbag3.team_gamelist())
    nbatwo3 = nba_gamestats(nbagameid2)
    print(nbatwo3.nbagame_info())
    print(nbatwo3.nbagame_summary()) 

    nbateam4="Golden State Warriors"
    nbaseason4="2012"
    nbagameid4="0021200010"
    nbag4 = nba_teamgame(nbateam4, nbaseason4)
    nbag4.team_id()
    print(nbag4.team_gamelist())
    nbatwo4 = nba_gamestats(nbagameid4)
    print(nbatwo4.nbagame_info())
    print(nbatwo4.nbagame_summary()) 
