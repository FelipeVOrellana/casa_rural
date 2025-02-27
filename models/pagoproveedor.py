class PagosProveedor(models.Model):
    _name = 'casa_rural.pagos_proveedores'
    _description = 'Pagos Proveedores: Registra los pagos realizados a proveedores'

    factura_id = fields.Many2one('casa_rural.facturacion_proveedores', string='Factura', required=True)
    monto = fields.Float(string='Monto')
    fecha_pago = fields.Date(string='Fecha de Pago')
    metodo_pago = fields.Char(string='Método de Pago')