from odoo import models, fields

class Pago(models.Model):
    _name = 'casa_rural.pago'
    _description = 'Pagos de la Casa Rural'

    factura_id = fields.Many2one('casa_rural.factura', string="Factura", required=True)
    monto = fields.Float(string="Monto", required=True)
    fecha_pago = fields.Date(string="Fecha de Pago", default=fields.Date.today)
    metodo_pago = fields.Selection([
        ('tarjeta', 'Tarjeta'),
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia')
    ], string="Método de Pago", required=True)
    estado_pago = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado')
    ], string="Estado de Pago", default='pendiente')