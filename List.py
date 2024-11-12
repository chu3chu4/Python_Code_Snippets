favorite_movie = ["batman", "iron man", "avengers", "Wu Kong"]

print(favorite_movie[0])
print(favorite_movie)

favorite_movie.insert(3, "Blue Green")

print(favorite_movie)

length = len(favorite_movie)

while length > 1:
    del (favorite_movie[length - 1])
    length = length - 1

print(favorite_movie)