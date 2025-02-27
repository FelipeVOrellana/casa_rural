class PagosClientes(models.Model):
    _name = 'casa_rural.pagos_clientes'
    _description = 'Pagos Clientes: Pagos efectuados para cada factura de cliente'

    factura_id = fields.Many2one('casa_rural.facturacion_clientes', string='Factura', required=True)
    monto = fields.Float(string='Monto')
    fecha_pago = fields.Date(string='Fecha de Pago')
    metodo_pago = fields.Char(string='Método de Pago')
    estado_pago = fields.Char(string='Estado de Pago')