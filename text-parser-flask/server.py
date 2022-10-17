from flask_app import app
from flask_app.controllers import controller_routes
from jaccard_distances import jaccard_similarity

str1 = "I went downstairs, then left the house."
str2 = "I descended upon the first floor, and ejected myself from the inside of the house D:"

jaccard_result = jaccard_similarity(str1, str2)
print(jaccard_result)

if __name__ == "__main__":
    app.run(debug=True)
