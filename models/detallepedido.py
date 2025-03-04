from odoo import models, fields, api

class DetallePedido(models.Model):
    _name = 'casa_rural.detalle_pedido'
    _description = 'Detalle del Pedido: Especifica los productos y cantidades en cada pedido'

    pedido_id = fields.Many2one('casa_rural.pedido', string='Pedido', required=True)
    producto_id = fields.Many2one('casa_rural.producto', string='Producto', required=True)
    cantidad = fields.Integer(string='Cantidad')
    precio_unitario = fields.Float(string='Precio Unitario')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_unitario