from odoo import models, fields

class Mensaje(models.Model):
    _name = 'casa_rural.mensaje'
    _description = 'Mensajes de la Casa Rural'

    cliente_id = fields.Many2one('casa_rural.huesped', string="Cliente", required=True)
    fecha_envio = fields.Date(string="Fecha de Envío", default=fields.Date.today)
    asunto = fields.Char(string="Asunto", required=True)
    contenido = fields.Text(string="Contenido", required=True)
    estado = fields.Selection([
        ('leido', 'Leído'),
        ('no_leido', 'No Leído')
    ], string="Estado", default='no_leido')
    canal_comunicacion_id = fields.Many2one('casa_rural.canal_comunicacion', string="Canal de Comunicación")