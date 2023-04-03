from odoo import models,fields,api


class Books(models.Model):
    _name = "books"
    _description = "librarysystem application"

    name = fields.Char()
    book_name = fields.Many2one("book.issue")
    selling_price = fields.Float()
    tag_ids = fields.Many2many("book.tags")
    author_ids = fields.Many2many("book.author")
    book_stock = fields.Integer()

    _sql_constraints = [
        ('check_name', 'unique(book_name)',
         'The Book name must be unique'),
    ]