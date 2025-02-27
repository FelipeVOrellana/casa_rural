from odoo import models, fields

class TipoServicio(models.Model):
    _name = 'casa_rural.tipo_servicio'
    _description = 'Tipos de Servicio de la Casa Rural'

    nombre_tipo_servicio = fields.Char(string="Nombre del Tipo de Servicio", required=True)
    descripcion = fields.Text(string="Descripción")
    servicio_ids = fields.One2many('casa_rural.servicio', 'tipo_servicio', string="Servicios")