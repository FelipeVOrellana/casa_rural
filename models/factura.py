from odoo import models, fields

class Factura(models.Model):
    _name = 'casa_rural.factura'
    _description = 'Facturas de la Casa Rural'

    estancia_id = fields.Many2one('casa_rural.estancia', string="Estancia", required=True)
    monto = fields.Float(string="Monto", required=True)
    fecha_emision = fields.Date(string="Fecha de Emisión", default=fields.Date.today)
    estado_pago = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado')
    ], string="Estado de Pago", default='pendiente')
    metodo_pago = fields.Selection([
        ('tarjeta', 'Tarjeta'),
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia')
    ], string="Método de Pago")
    pago_ids = fields.One2many('casa_rural.pago', 'factura_id', string="Pagos")