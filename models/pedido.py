class Pedido(models.Model):
    _name = 'casa_rural.pedido'
    _description = 'Pedidos: Registra los pedidos realizados a proveedores'

    proveedor_id = fields.Many2one('casa_rural.proveedor', string='Proveedor', required=True)
    fecha_pedido = fields.Date(string='Fecha de Pedido')
    estado = fields.Char(string='Estado')
    fecha_entrega = fields.Date(string='Fecha de Entrega')
    detalle_ids = fields.One2many('casa_rural.detalle_pedido', 'pedido_id', string='Detalle del Pedido')
    # Relación muchos a muchos con Facturación_Proveedores (tabla intermedia "casa_rural_pedido_factura_rel")
    factura_ids = fields.Many2many(
        'casa_rural.facturacion_proveedores',
        'casa_rural_pedido_factura_rel',
        'pedido_id', 'factura_id',
        string='Facturación'
    )