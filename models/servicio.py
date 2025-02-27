from odoo import models, fields

class Servicio(models.Model):
    _name = 'casa_rural.servicio'
    _description = 'Servicios: Servicios ofrecidos por o para la casa rural'

    nombre_servicio = fields.Char(string='Nombre del Servicio', required=True)
    descripcion = fields.Text(string='Descripción')
    precio = fields.Float(string='Precio')
    tipo_servicio_id = fields.Many2one('casa_rural.tipo_servicio', string='Tipo de Servicio')
    incidencia_ids = fields.One2many('casa_rural.incidencia', 'servicio_id', string='Incidencias')