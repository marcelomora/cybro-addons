# -*- coding: utf-8 -*-
# Copyright 2019 Linksoft Mitra Informatika

from odoo import models, fields, api

# class default(models.Model):
#     _name = 'default.default'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100