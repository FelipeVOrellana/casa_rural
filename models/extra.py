from odoo import models, fields

class Extra(models.Model):
    _name = 'casa_rural.extra'
    _description = 'Extras de la Casa Rural'

    nombre_extra = fields.Char(string="Nombre del Extra", required=True)
    descripcion = fields.Text(string="Descripción")
    precio = fields.Float(string="Precio", required=True)
    reserva_ids = fields.Many2many('casa_rural.reserva', string="Reservas")