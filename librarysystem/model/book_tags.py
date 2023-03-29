from odoo import models,fields

class Book_tags(models.Model):
    _name = "book.tags"
    _description = "estate application"

    name = fields.Char()

    _sql_constraints = [
        ('check_name', 'unique(name)',
         'The Book tag name must be unique'),
    ]