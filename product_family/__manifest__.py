
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    'name': 'Product Family',
    'version': '1.0',
    'category': "Generic Modules",
    'description': """ This module adds product family field""",
    'author': 'AvanzOSC',
    'website': 'http://www.openerp.com',
    'depends': ['base', 'stock'],
    'init_xml': [],
    'data': [
        'security/ir.model.access.csv',
        'views/product_family_view.xml',
        'views/product_template_view.xml'
                   ],
    'demo_xml': [],
    'installable': True,
    'auto_install': False,
}
