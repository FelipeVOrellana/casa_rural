from odoo import models, fields

class Estancia(models.Model):
    _name = 'casa_rural.estancia'
    _description = 'Estancias: Registra cada periodo de estancia de un huésped'

    huesped_id = fields.Many2one('casa_rural.huesped', string='Huésped', required=True)
    fecha_entrada = fields.Date(string='Fecha de Entrada')
    fecha_salida = fields.Date(string='Fecha de Salida')
    precio_total = fields.Float(string='Precio Total')
    habitacion_ids = fields.Many2many(
        'casa_rural.habitacion',
        'casa_rural_estancia_habitacion_rel',
        'estancia_id', 'habitacion_id',
        string='Habitaciones'
    )
    facturacion_ids = fields.One2many('casa_rural.facturacion_clientes', 'estancia_id', string='Facturación')