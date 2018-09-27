import webbrowser

class Movie():
    """This class stores movies information"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube): 
    #This part of the code is to store data for each movie:
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = trailer_youtube
    #This code will execute the trailer:
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
