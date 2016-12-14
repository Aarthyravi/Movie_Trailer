import fresh_tomatoes  # import the module. This module is template of this project
import media           # To call my 'class Movie():' definition module

# Create own instances(bfg,avator,mummy,trolls,zootopia,jurassic)
# of their class 'Movie'.

bfg = media.Movie("The BFG",
                  "Ten-year-old Sophie is in for the adventure of a lifetime when she meets the Big Friendly Giant",
                  "https://upload.wikimedia.org/wikipedia/en/a/af/The_BFG_poster.jpg",
                  "https://www.youtube.com/watch?v=VG5MtenlP-A")

avator = media.Movie("Avator",
                     "Jack is drawn into a battle for the survival of Marine's World",
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/Avatar-video-game-cover.jpg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
mummy = media.Movie("The Mummy(2017)",
                    "Welcome to a new world of Gods and Monsters",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/2/2e/The_Mummy_(2017)_teaser_poster.jpg/220px-The_Mummy_(2017)_teaser_poster.jpg",
                    "https://www.youtube.com/watch?v=LAWo9_V2qOg")
trolls = media.Movie("Trolls",
                     "The Trolls are small creatures who live in an almost perpetual state of happiness, singing, dancing, and hugging all day long",
                     "https://upload.wikimedia.org/wikipedia/en/a/ad/Trolls_(film)_logo.png",
                     "https://www.youtube.com/watch?v=xyjm5VQ11TQ")
zootopia = media.Movie("Zootopia",
                       "Judy gets at the opportunity to solve a mysterious case",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")
jurassic = media.Movie("Jurassic World",
                       "When the massive creature escapes, it sets off a chain reaction that causes the other dinos to run amok",
                       "https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg",
                       "https://www.youtube.com/watch?v=h-IxwI6m_s0")
# Array list of input
movies = [bfg,avator,mummy,trolls,zootopia,jurassic]

# open_movies_page receives this input array and to create HTML Webpage.
fresh_tomatoes.open_movies_page(movies)

                       
                       
