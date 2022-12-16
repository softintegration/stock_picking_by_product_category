# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    transfer_by_product_categ = fields.Boolean(
        string='Transfer only products included in the same product category at once', default=False,
        help="If this case is checked,the system will display the field <Product categrory> in the transfer and only the products included in the selected category can be selected and transfered.")
