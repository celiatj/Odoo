# -*- coding: utf-8 -*-
from odoo import models, fields, api


class parquebombero(models.Model):
     _name = 'parquebombero.parquebombero'
     _description = 'parquebombero.parquebombero'

     name = fields.Char()
     nombre = fields.Char()
     telefono = fields.Integer()
     direccion = fields.Text()
     numero = fields.Integer()

bombero_id=fields.Many2one("bombero.bombero",string='bombero')

camion_id=fields.Many2one("camion.camion",string='camion')

class bombero(models.Model):
     _name = '.bombero'
     _description = 'bombero.bombero'

     name = fields.Char()

     edad= fields.Integer()
     nombre = fields.Char()
     numero = fields.Integer()

     tipo=fields.One2many("parquebombero.parquebombero", "numero", string='tipo')
class camion(models.Model):
         _name = 'camion.camion'
         _description = 'camion.camion'


         name = fields.Char()
         numero = fields.Integer()
         tipo = fields.One2many("parquebombero.parquebombero", "numero", string='tipo')