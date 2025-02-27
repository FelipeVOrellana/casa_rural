from odoo import models, fields

class Reserva(models.Model):
    _name = 'casa_rural.reserva'
    _description = 'Reservas de la Casa Rural'

    cliente_id = fields.Many2one('casa_rural.huesped', string="Cliente", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Date(string="Fecha de Fin", required=True)
    cantidad_personas = fields.Integer(string="Cantidad de Personas", required=True)
    extras_reserva_ids = fields.One2many('casa_rural.extras_reservas', 'reserva_id', string='Extras Agregados')
