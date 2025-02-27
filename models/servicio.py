from odoo import models, fields

class Servicio(models.Model):
    _name = 'casa_rural.servicio'
    _description = 'Servicios de la Casa Rural'

    nombre_servicio = fields.Char(string="Nombre del Servicio", required=True)
    descripcion = fields.Text(string="Descripción")
    precio = fields.Float(string="Precio", required=True)
    tipo_servicio = fields.Many2one('casa_rural.tipo_servicio', string="Tipo de Servicio", required=True)
    proveedor_ids = fields.Many2many('casa_rural.proveedor', string="Proveedores")