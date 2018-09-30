import webbrowser


class Movie():
    """This class stores movies information

      Atributes:
          title (str): Title of the movie
          storyline (str): Short Storyline of the movie
          poster_image (str): Link to the Poster Image of the movie
          trailer_url(str): Link to Trailer of the movie (e.g. youtube url)
    """

    def __init__(self, title, storyline, poster_image, trailer_url):
        # This part of the code is to store data for each movie:
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        # This code will execute the trailer:
        webbrowser.open(self.trailer_youtube_url)
