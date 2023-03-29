from odoo import models,fields


class Students(models.Model):
    _name = "students"
    _description = "librarysystem application"

    name = fields.Char(required=True)
    contact_no = fields.Integer()
    address = fields.Char()
    Email = fields.Char()