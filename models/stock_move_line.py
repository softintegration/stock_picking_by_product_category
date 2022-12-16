# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    transfer_by_product_categ = fields.Boolean(related='picking_type_id.transfer_by_product_categ')

    @api.onchange('transfer_by_product_categ')
    def _onchange_transfer_by_product_categ(self):
        if self.transfer_by_product_categ and self.picking_id.categ_id:
            return {'domain':{'product_id':[('categ_id','=',self.picking_id.categ_id.id)]}}
        elif self.transfer_by_product_categ and not self.picking_id.categ_id:
            return {'domain':{'product_id':[('id','=',-1)]}}

