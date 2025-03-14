from odoo import models, fields

class FacturacionClientes(models.Model):
    _name = 'casa_rural.facturacion_clientes'
    _description = 'Facturación Clientes: Facturación generada por cada estancia'

    estancia_id = fields.Many2one('casa_rural.estancia', string='Estancia', required=True)
    monto = fields.Float(string='Monto')
    fecha_emision = fields.Date(string='Fecha de Emisión')
    estado_pago = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado')
    ], string="Estado de Pago", default='pendiente')
    metodo_pago = fields.Selection([
        ('tarjeta', 'Tarjeta'),
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia')
    ], string="Método de Pago")
    pago_ids = fields.One2many('casa_rural.pagos_clientes', 'factura_id', string='Pagos')