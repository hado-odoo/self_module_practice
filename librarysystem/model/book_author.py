from odoo import models,fields


class Book_author(models.Model):
    _name = "book.author"
    _description = "librarysystem application"


    author_name = fields.Char()
    book_name = fields.Char(required=True)
    publishe_date = fields.Date()
    


