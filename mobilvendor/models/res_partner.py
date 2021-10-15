# Copyright 2021 Akretion (https://www.akretion.com).
# @author marcelomora <java.diablo@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    mobilvendor_partner_number = fields.Char("MobilVendor Partner ID", size=25)
    

    

