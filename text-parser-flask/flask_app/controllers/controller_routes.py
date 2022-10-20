from flask_app import app
from flask import render_template, redirect, request
from flask_app.middleware import (
    calculate_jaccard,
    calculate_euclidean,
    calculate_cosine,
)


@app.route("/")
def home():
    return render_template("components/landing.html", result=0)


@app.route("/input", methods=["GET"])
def input_text():
    print(request.args.keys())
    comparator = request.args.get("comparator")
    text1 = request.args.get("text1")
    text2 = request.args.get("text2")
    print(comparator, text1, text2)

    result = 0

    match comparator:
        case "jaccard":
            result = calculate_jaccard.jaccard_similarity(text1, text2)
            print("jaccard: " + str(result))
            return str(result)
        case "euclidean":
            result = calculate_euclidean.euclidean_similarity(text1, text2)
            print("euclidean: " + result)
            return str(result)
        case "cosine":
            visualize = calculate_cosine.find_cosine_similarity(text1, text2)
            # print("cosine: " + result)
            return render_template("components/landing.html", visualize=visualize)
    # if comparator == "jaccard":
    #     result = jaccard_similarity(text1, text2)
    #     # print(result)
    #     return str(result)
    return result

    # for val in request.args:
    #     print(val)

    # result = 0
    # if request.form["similarity_measure"] == "jaccard":
    #     result = jaccard_similarity(
    #         request.form["input_string_1"], request.form["input_string_2"]
    #     )
    #     return redirect(f"/results/{result}")
    return redirect("/")


# @app.route("/input", methods=["POST"])
# def input_text():
#     for val in request.form:
#         print(val + ": " + request.form[val])

#     result = 0
#     if request.form["similarity_measure"] == "jaccard":
#         result = jaccard_similarity(
#             request.form["input_string_1"], request.form["input_string_2"]
#         )
#         return redirect(f"/results/{result}")
#     return redirect(f"/results")


# @app.route("/results/<float(signed=True):result>")
# def results(result):
#     print(result)
#     return render_template("components/home.html", result=result)


# @app.route("/results/<int:result>/")
# def results(result):
#     return render_template("components/home.html", result=result)
