import movies

toy_story = movies.Movie("Toy Story","A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=vwyZH85NQC4")

print(toy_story.storyline)
toy_story.show_trailer()