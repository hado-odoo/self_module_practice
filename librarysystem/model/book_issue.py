from odoo import models,fields


class Book_issue(models.Model):
    _name = "book.issue"
    _description = "librarysystem application"

    sutdent_name = fields.Char()
    book_name = fields.Char(required=True)
    issue_date = fields.Date()
    


