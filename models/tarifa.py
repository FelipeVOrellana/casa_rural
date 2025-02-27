from odoo import models, fields

class Tarifa(models.Model):
    _name = 'casa_rural.tarifa'
    _description = 'Tarifas de la Casa Rural'

    tipo_habitacion = fields.Selection([
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite')
    ], string="Tipo de Habitación", required=True)
    precio_noche = fields.Float(string="Precio por Noche", required=True)
    temporada = fields.Selection([
        ('alta', 'Temporada Alta'),
        ('baja', 'Temporada Baja')
    ], string="Temporada", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)
    habitacion_ids = fields.Many2many(
        'casa_rural.habitacion',
        'casa_rural_tarifa_habitacion_rel',
        'tarifa_id', 'habitacion_id',
        string='Habitaciones'
    )