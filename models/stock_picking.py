# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class Picking(models.Model):
    _inherit = "stock.picking"

    transfer_by_product_categ = fields.Boolean(related='picking_type_id.transfer_by_product_categ')
    categ_id = fields.Many2one('product.category', 'Product Category',)


    @api.onchange('categ_id')
    def on_change_categ_id(self):
        self.move_lines = False

    @api.constrains('transfer_by_product_categ','categ_id','move_lines','move_ids_without_package','move_line_ids','move_line_ids_without_package')
    def _check_moves_categ_unicity(self):
        """ Check that all the selected products have the same category"""
        if self.transfer_by_product_categ and self.categ_id and self.move_lines:
            move_lines_categ_id = self._get_moves_categ('move_lines')
            if len(move_lines_categ_id) > 1:
                raise UserError(_("All the products must belongs to the same category!"))
            if move_lines_categ_id[0].id != self.categ_id.id:
                raise UserError(_("All the products must belongs to the picking category %s!")%self.categ_id.name)
        elif self.transfer_by_product_categ and self.categ_id and self.move_ids_without_package:
            move_lines_categ_id = self._get_moves_categ('move_ids_without_package')
            if len(move_lines_categ_id) > 1:
                raise UserError(_("All the products must belongs to the same category!"))
            if move_lines_categ_id[0].id != self.categ_id.id:
                raise UserError(_("All the products must belongs to the picking category %s!")%self.categ_id.name)
        elif self.transfer_by_product_categ and self.categ_id and self.move_line_ids:
            move_line_ids_categ_id = self._get_moves_categ('move_line_ids')
            if len(move_line_ids_categ_id) > 1:
                raise UserError(_("All the products must belongs to the same category!"))
            if move_line_ids_categ_id[0].id != self.categ_id.id:
                raise UserError(_("All the products must belongs to the picking category %s!")%self.categ_id.name)
        elif self.transfer_by_product_categ and self.categ_id and self.move_line_ids_without_package:
            move_line_ids_without_package_categ_id = self._get_moves_categ('move_line_ids_without_package')
            if len(move_line_ids_without_package_categ_id) > 1:
                raise UserError(_("All the products must belongs to the same category!"))
            if move_line_ids_without_package_categ_id[0].id != self.categ_id.id:
                raise UserError(_("All the products must belongs to the picking category %s!")%self.categ_id.name)

    def _get_moves_categ(self,move_field):
        return getattr(self,move_field).mapped("product_id").mapped("categ_id")




