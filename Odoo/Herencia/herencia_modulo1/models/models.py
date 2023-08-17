# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo import api
from odoo import models, fields
from odoo.exceptions import ValidationError
# from odoo import models, fields, api
class Profesor(models.Model):
    _name = 'herencia_modulo2.profesor'
    _description = 'Profe'
    name = fields.Char('Denomination', size=64, required=True)
    #-uno a muchos -profesor-----asignatura
    asignatura_id = fields.Many2one(
        comodel_name='herencia_modulo1.asignatura',
        string='Asignatura'
    )
# class herencia_modulo1(models.Model):
#     _name = 'herencia_modulo1.herencia_modulo1'
#     _description = 'herencia_modulo1.herencia_modulo1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
