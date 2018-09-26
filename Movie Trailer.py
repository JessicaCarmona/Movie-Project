import media
import fresh_tomatoes

Life_of_Pi = media.Movie("Life of Pi","A young man and a tiger in a boat at sea","https://upload.wikimedia.org/wikipedia/en/5/57/Life_of_Pi_2012_Poster.jpg","https://www.youtube.com/watch?v=j9Hjrs6WQ8M")

Avatar = media.Movie("Avatar","A marin on an alien planet","https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

Price_and_Prejudice = media.Movie("Price and Prejudice","Story of the game of love among the British upper classes","https://m.media-amazon.com/images/M/MV5BMTA1NDQ3NTcyOTNeQTJeQWpwZ15BbWU3MDA0MzA4MzE@._V1_SY1000_CR0,0,674,1000_AL_.jpg","https://www.youtube.com/watch?v=7Afx8MGg00g")

movies = [Life_of_Pi,Avatar,Price_and_Prejudice]
fresh_tomatoes.open_movies_page(movies)
