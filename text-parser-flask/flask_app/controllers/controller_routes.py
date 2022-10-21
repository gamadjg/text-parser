from flask_app import app
from flask import render_template, redirect, request, Response, session
from flask_app.models.model_document_results import Document_result
from flask_app.middleware import (
    calculate_jaccard,
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
    match comparator:
        case "jaccard":
            result = calculate_jaccard.jaccard_similarity_prep(text1, text2)
            if "uuid" in session:
                Document_result.create(
                    {
                        "comparator": "jaccard",
                        "score": result,
                        "text1": text1,
                        "text2": text2,
                        "user_id": session["uuid"],
                    }
                )
            print("jaccard: " + str(result))
            return str(result)
        case "cosine":
            result = calculate_cosine.cosine_prep(text1, text2)
            if "uuid" in session:
                Document_result.create(
                    {
                        "comparator": "cosine",
                        "score": result,
                        "text1": text1,
                        "text2": text2,
                        "user_id": session["uuid"],
                    }
                )
            print("cosine: " + str(result))
            return str(result)
        case _:
            return "Error"
