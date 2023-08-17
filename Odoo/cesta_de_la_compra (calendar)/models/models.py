# -*- coding: utf-8 -*-
from datetime import date

from odoo import api
from odoo import models, fields
from odoo.exceptions import ValidationError


class inventario(models.Model):
    _name = 'cesta_de_la_compra.inventario'
    _description = 'inventario'
    _sql_constraints = [
        ('Name', 'unique(Name)', "Ese nombre ya existe!"),
    ]
    name=fields.Char('Name', required=True)
    cantidad= fields.Integer(string='cantidad')
    tipoPro=fields.Char(string='tipoPro')
    precioUnidad=fields.Integer(string='precioUnidad')
    compra_ids = fields.One2many("cesta_de_la_compra.compra", "inventario_id", string='compras')



class Comprador(models.Model):
    _name = 'cesta_de_la_compra.comprador'
    _description = 'Comprador'
    name = fields.Char('Nombre', required=True)
    dinero_gastado = fields.Float(string='Dinero gastado', compute='_compute_dinero_gastado')
    apellido1 = fields.Char(string='Apellido 1')
    apellido2 = fields.Char(string='Apellido 2')
    direccion = fields.Char(string='Dirección')
    country_id = fields.Many2one('res.country', string='Country')
    dinero_a_cuenta = fields.Float(string='Dinero a cuenta')
    nif = fields.Char(string='NIF', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    tutor_nif = fields.Char(string='NIF del tutor')
    mayor_de_edad = fields.Boolean(string='Mayor de edad', compute='_compute_mayor_de_edad')
    edad = fields.Integer(string='Edad', compute='_compute_edad')

    compra_ids = fields.One2many("cesta_de_la_compra.compra", "comprador_id", string='Compras')

    _sql_constraints = [
        ('nif', 'unique(nif)', "Ese nif ya existe!"),
    ]
    @api.depends('fecha_nacimiento','edad')
    def _compute_edad(self):
        if self.fecha_nacimiento:
            today = date.today()
            self.edad = today.year - self.fecha_nacimiento.year

    @api.depends('edad')
    def _compute_mayor_de_edad(self):
        self.mayor_de_edad = self.edad >= 18

    @api.constrains('edad')
    def check_edad(self):
        if self.edad < 18 and not self.tutor_nif:
            raise ValidationError("Es necesario ingresar el NIF del tutor para clientes menores de edad")

    @api.constrains('dinero_a_cuenta')
    def _check_dinero_a_cuenta(self):
            if self.dinero_a_cuenta > 50:
                raise ValidationError("El dinero en cuenta no puede ser mayor a 50")

    @api.depends('dinero_a_cuenta', 'compra_ids')
    def _compute_dinero_gastado(self):
        for record in self:
            gastado = 0.0
            gastado += self.compra_ids.cantidad_comprada * self.compra_ids.inventario_id.precioUnidad
            record.dinero_gastado = gastado

class compra(models.Model):
    class Compra(models.Model):
        _name = 'cesta_de_la_compra.compra'
        _description = 'Compra'
        name = fields.Char('Nombre', required=True)
        cantidad_comprada = fields.Integer(string='Cantidad comprada')
        fecha_compra = fields.Date(string='Fecha')
        inventario_id = fields.Many2one("cesta_de_la_compra.inventario", string='Inventario')
        comprador_id = fields.Many2one("cesta_de_la_compra.comprador", string='Comprador')
        forma_pago = fields.Selection([
            ('cuenta', 'A cuenta'),
            ('tarjeta', 'Con tarjeta de crédito'),
        ], string='Forma de pago', default='cuenta')
        dinero_disponible = fields.Float(string='Dinero disponible', compute='_compute_dinero_disponible')

        @api.constrains('cantidad_comprada', 'inventario_id')
        def update_inventory(self):
            if self.inventario_id.cantidad < self.cantidad_comprada:
                raise ValidationError("No hay suficiente cantidad en el inventario")
            self.inventario_id.cantidad -= self.cantidad_comprada

        @api.constrains('cantidad_comprada', 'inventario_id')
        def _check_inventory(self):
            if self.inventario_id.cantidad < self.cantidad_comprada:
                raise ValidationError("No hay suficiente stock en el inventario")

        @api.depends('comprador_id', 'dinero_disponible', 'inventario_id')
        def _compute_dinero_disponible(self):
                self.dinero_disponible= self.comprador_id.dinero_a_cuenta - (self.cantidad_comprada * self.inventario_id.precioUnidad)


# class cesta_de_la_compra(models.Model):
#     _name = 'cesta_de_la_compra.cesta_de_la_compra'
#     _description = 'cesta_de_la_compra.cesta_de_la_compra'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
# raise ValidationError("No tienes suficiente dinero")
# country_id = fields.Many2one('res.country', string='País')
