from odoo import api, models,fields
from odoo.exceptions import ValidationError,UserError
from dateutil.relativedelta import relativedelta

class Book_issue(models.Model):
    _name = "book.issue"
    _description = "librarysystem application"

    name = fields.Char()
    issue_books = fields.Many2many("books",'book_name')
    issue_date = fields.Date(default=lambda self: fields.Date.today(),readonly=True)
    returned_date=fields.Date(default=lambda self: fields.Date.today()+ relativedelta (months=3),readonly=True)
    student_id=fields.Many2one("students",create="0",store=True)
    sutdent_name = fields.Char(related="student_id.name")
    book_name = fields.Char(related="issue_books.name")
