import fresh_tomatoes  # import the module. This is template of this project
import media           # To call my 'class Movie():' definition module

# Create our own instances(bfg,avator,mummy,trolls,zootopia,jurassic)
# of their class 'Movie'.

bfg = media.Movie("Revenue",
                  "Ten-year-old Sophie is in for the adventure of a lifetime when she meets the Big Friendly Giant",
                  "https://upload.wikimedia.org/wikipedia/en/a/af/The_BFG_poster.jpg",
                  "https://www.youtube.com/watch?v=JfGOdP8zOyw")

avator = media.Movie("Profit_Margin",
                     "Jack is drawn into a battle for the survival of Marine's World",
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/Avatar-video-game-cover.jpg",
                     "https://www.youtube.com/watch?v=uQgZ1RklwQs")
mummy = media.Movie("Earning Per Share",
                    "Welcome to a new world of Gods and Monsters",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/The_Mummy_(2017)_teaser_poster.jpg/220px-The_Mummy_(2017)_teaser_poster.jpg",
                    "https://www.youtube.com/watch?v=J5mREOYHUNU")
trolls = media.Movie("PE_Ratio",
                     "The Trolls are small creatures who live in an almost perpetual state of happiness, singing, dancing, and hugging all day long",
                     "https://upload.wikimedia.org/wikipedia/en/a/ad/Trolls_(film)_logo.png",
                     "https://www.youtube.com/watch?v=pwHY0Vdm4BU")
zootopia = media.Movie("Capex",
                       "Judy gets at the opportunity to solve a mysterious case",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=PtdOqFPMWe4")
jurassic = media.Movie("Operating_Margin",
                       "When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok",
                       "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                       "https://www.youtube.com/watch?v=EPcwRo6uvW4")
# Array list of input
movies = [bfg,avator,mummy,trolls,zootopia,jurassic]

# open_movies_page receives this input array and to create HTML Webpage.
fresh_tomatoes.open_movies_page(movies)


                       
                       
