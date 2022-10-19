from xml.etree.ElementTree import tostring
from flask_app import app, jaccard_similarity
from flask import render_template, redirect, request


@app.route("/")
def home():
    return render_template("components/home.html", result=0)


@app.route("/input", methods=["GET"])
def input_text():
    print(request.args.keys())
    comparator = request.args.get("comparator")
    text1 = request.args.get("text1")
    text2 = request.args.get("text2")
    print(comparator, text1, text2)

    result = 0
    if comparator == "jaccard":
        result = jaccard_similarity(text1, text2)
        print(result)
        return str(result)
    return result


@app.route("/login")
def login():
    return render_template("components/login.html")

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
