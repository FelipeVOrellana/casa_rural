from odoo import models, fields

class Huesped(models.Model):
    _name = 'casa_rural.huesped'
    _description = 'Huéspedes de la Casa Rural'
    
    nombre = fields.Char(required=True)
    apellidos = fields.Char(required=True)
    dni = fields.Char(required=True)
    email = fields.Char()
    telefono = fields.Char()
    fecha_nacimiento = fields.Date()
    direccion = fields.Text()
    estancias_ids = fields.One2many('casa_rural.estancia', 'huesped_id', string='Estancias')