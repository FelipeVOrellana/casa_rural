from odoo import models, fields

class Producto(models.Model):
    _name = 'casa_rural.producto'
    _description = 'Productos: Productos que se pueden pedir'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    precio_unitario = fields.Float(string='Precio Unitario')
    stock_disponible = fields.Integer(string='Stock Disponible')
    pedido_ids = fields.Many2many(
        'casa_rural.pedido',
        'producto_pedido_rel',
        'producto_id', 'pedido_id',
        string='Pedidos'
    )