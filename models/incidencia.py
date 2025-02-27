from odoo import models, fields

class Incidencia(models.Model):
    _name = 'casa_rural.incidencia'
    _description = 'Incidencias de la Casa Rural'

    servicio_id = fields.Many2one('casa_rural.servicio', string="Servicio", required=True)
    fecha_incidencia = fields.Date(string="Fecha de Incidencia", default=fields.Date.today)
    descripcion = fields.Text(string="Descripción", required=True)
    estado_incidencia = fields.Selection([
        ('abierta', 'Abierta'),
        ('en_progreso', 'En Progreso'),
        ('cerrada', 'Cerrada')
    ], string="Estado de la Incidencia", default='abierta')