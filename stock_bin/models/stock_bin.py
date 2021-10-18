# -*- encoding: utf-8 -*-
# Copyright 2021 Accioma (https://accioma.com).
# @author marcelomora <java.diablo@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

class StockBin(models.Model):
    _name = 'stock.bin'
    _description = 'Stock Bin'

    name = fields.Char('Name', required=True )

    warehouse_id = fields.Many2one(
        'stock.warehouse',
        'Warehouse', required=True )

    prod_tmpl_id = fields.Many2one(
        'product.template',
        'Product Template')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bin_ids = fields.One2many(
        'stock.bin',
        'prod_tmpl_id',
        'Bins')




