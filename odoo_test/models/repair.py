from odoo import api, fields, models, _


class Repair(models.Model):
    _inherit = 'repair.order'

    serial_number_id = fields.Many2one('serial.number', 'Serial Number')

    
class RepairLine(models.Model):
    _inherit = 'repair.line'

    man_hour = fields.Float(
        'Man hour',
        default=0.0, digits=(16, 2), required=True)

    man_hour_rate = fields.Float(
        'Man hour rate',
        default=0.0, digits=(16, 2), required=True)
    

    @api.depends('price_unit', 'repair_id', 'product_uom_qty', 'product_id', 
                 'repair_id.invoice_method', 'man_hour', 'man_hour_rate')
    def _compute_price_subtotal(self):
        """
        Override root function to calculate man hour price 
        to subtotal sparepart.
        """
        for line in self:
            taxes = line.tax_id.compute_all(
                line.price_unit, 
                line.repair_id.pricelist_id.currency_id, 
                line.product_uom_qty, 
                line.product_id, 
                line.repair_id.partner_id
            )
            man_hour_cost = line.man_hour * line.man_hour_rate
            line.price_subtotal = taxes['total_excluded'] + man_hour_cost



class SerialNumber(models.Model):
    _name = 'serial.number'

    name = fields.Char('Serial Number')

    