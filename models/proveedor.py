from odoo import models, fields

class Proveedor(models.Model):
    _name = 'casa_rural.proveedor'
    _description = 'Proveedores: Datos de proveedores externos'

    nombre = fields.Char(string='Nombre', required=True)
    contacto = fields.Char(string='Contacto')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    direccion = fields.Char(string='Dirección')
    contrato_ids = fields.One2many('casa_rural.contrato', 'proveedor_id', string='Contratos')
    pedido_ids = fields.One2many('casa_rural.pedido', 'proveedor_id', string='Pedidos')
    servicio_ids = fields.Many2many(
        'casa_rural.servicio',
        'casa_rural_proveedor_servicio_rel',
        'proveedor_id', 'servicio_id',
        string='Servicios'
    )