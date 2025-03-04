from odoo import models, fields

class FacturacionProveedore(models.Model):
    _name = 'casa_rural.facturacion_proveedores'
    _description = 'Facturación Proveedores: Registra la facturación asociada a los pedidos de proveedores'

    monto_total = fields.Float(string='Monto Total')
    fecha_emision = fields.Date(string='Fecha de Emisión')
    estado_pago = fields.Char(string='Estado de Pago')
    pago_ids = fields.One2many('casa_rural.pagos_proveedores', 'factura_id', string='Pagos')
    pedido_ids = fields.Many2many(
        'casa_rural.pedido',
        'casa_rural_pedido_factura_rel',
        'factura_id', 'pedido_id',
        string='Pedidos'
    )