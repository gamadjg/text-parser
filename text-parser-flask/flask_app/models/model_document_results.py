from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session
import re


class Document_result:
    def __init__(self, data):
        self.id = data["id"]
        self.comparator = data["comparator"]
        self.score = data["score"]
        self.text1 = data["text1"]
        self.text2 = data["text2"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO document_results (comparator, score, text1, text2, user_id) VALUES (%(comparator)s, %(score)s, %(text1)s, %(text2)s, %(user_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
