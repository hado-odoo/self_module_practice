from odoo import models,fields


class Books(models.Model):
    _name = "books"
    _description = "librarysystem application"

    name = fields.Char(required=True)
    selling_price = fields.Float()
    tags = fields.Many2one('book.tags',string='tags')
    author_name = fields.Char()
    book_stock = fields.Integer()


    _sql_constraints = [
        ('check_name', 'unique(name)',
         'The Book name must be unique'),
    ]


