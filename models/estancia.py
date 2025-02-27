from odoo import models, fields

class Estancia(models.Model):
    _name = 'casa_rural.estancia'
    _description = 'Registro de Estancias'
    
    huesped_id = fields.Many2one('casa_rural.huesped', string='Huésped', required=True)
    habitacion_ids = fields.Many2many('casa_rural.habitacion', string='Habitaciones')
    fecha_entrada = fields.Date(required=True)
    fecha_salida = fields.Date(required=True)
    precio_total = fields.Float()
    factura_ids = fields.One2many('casa_rural.factura', 'estancia_id', string='Facturas')