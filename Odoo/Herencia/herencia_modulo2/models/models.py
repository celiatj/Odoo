# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo import api
from odoo import models, fields
from odoo.exceptions import ValidationError



# from odoo import models, fields, api



class estudiante(models.Model):
        _name = 'herencia_modulo2.estudiante'
        _description = 'estudiante'

        name = fields.Char('Name', required=True)
        last_name = fields.Char(String="Last name", required=True)



asignatura_ids = fields.Many2many(
    'school.asignatura',
    'muchos_muchos_estudiante_asignatura_rel',
    'asignatura_id',
    'estudiante_id',
    string='Asignaturas'
)
class asignatura(models.Model):
    _name = 'herencia_modulo2.asignatura'
    _description = 'asignatura'
    name = fields.Char('Denomination', size=64, required=True)
    grade = fields.Selection([('first','First grade'),('second','Second grade'),('third','Third grade'),('fourth','Fourth grade')], default='First')
    estudiantes_ids = fields.Many2many(
      'school_estudiante',
      'muchos_muchos_estudiante_asignatura_rel'
      'asignatura_id',
      'estudiante_id',
      string='Estudiantes'
    )
    profesor_id = fields.Many2one(
        comodel_name='herencia_modulo1.profesor',
        string='Profesor'
    )
#     _name = 'herencia_modulo2.herencia_modulo2'
#     _description = 'herencia_modulo2.herencia_modulo2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
