from odoo import models,fields,api
from odoo.exceptions import UserError,ValidationError


class Students(models.Model):
    _name = "students"
    _description = "librarysystem application"
    _rec_name="id"


    id =fields.Integer(readonly=True)
    name = fields.Char()
    contact_no = fields.Integer()
    address = fields.Char()
    email = fields.Char()

    book_ids = fields.One2many("book.issue", "student_id")

    _sql_constraints = [('Email_unique','unique(email)','The Email must be unique')]
