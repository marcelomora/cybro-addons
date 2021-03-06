# -*- encoding: utf-8 -*-
# Copyright 2021 Accioma (https://accioma.com).
# @author marcelomora <java.diablo@gmail.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api
import hashlib


class ResUsers(models.Model):
    _inherit = "res.users"

    password_hash = fields.Char('Name', size=128, required=False,)

    def __init__(self, pool, cr):
        """ Override of __init__ to add access rights on
        store fields. Access rights are disabled by
        default, but allowed on some specific fields defined in
        self.SELF_{READ/WRITE}ABLE_FIELDS.
        """
        init_res = super(ResUsers, self).__init__(pool, cr)
        # duplicate list to avoid modifying the original reference
        self.SELF_WRITEABLE_FIELDS = list(self.SELF_WRITEABLE_FIELDS)
        self.SELF_WRITEABLE_FIELDS.append('password_hash')
        # duplicate list to avoid modifying the original reference
        self.SELF_READABLE_FIELDS = list(self.SELF_READABLE_FIELDS)
        self.SELF_READABLE_FIELDS.append('password_hash')
        return init_res

    def _set_password(self):
        """ Encrypts then stores the provided plaintext password for the user
        ``id``
        """
        for user in self:
            user.password_hash = hashlib.sha1(user.password.encode()).hexdigest()
        return super(ResUsers, self)._set_password()
