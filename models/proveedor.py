from odoo import models, fields

class Proveedor(models.Model):
    _name = 'casa_rural.proveedor'
    _description = 'Proveedores de la Casa Rural'

    nombre = fields.Char(string="Nombre", required=True)
    contacto = fields.Char(string="Contacto")
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Email")
    direccion = fields.Text(string="Dirección")
    servicio_ids = fields.Many2many('casa_rural.servicio', string="Servicios")