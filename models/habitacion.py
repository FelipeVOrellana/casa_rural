from odoo import models, fields

class Habitacion(models.Model):
    _name = 'casa_rural.habitacion'
    _description = 'Habitaciones de la Casa Rural'

    numero = fields.Char(string="Número de Habitación", required=True)
    tipo = fields.Selection([
        ('individual', 'Individual'),
        ('doble', 'Doble'),
        ('suite', 'Suite')
    ], string="Tipo de Habitación", required=True)
    estado = fields.Selection([
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'En Mantenimiento')
    ], string="Estado", default='disponible')
    estancias_ids = fields.Many2many('casa_rural.estancia', string="Estancias")