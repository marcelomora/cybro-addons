# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#    Copyright (C) 2017-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Niyas Raphy(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Hide Product Cost Price',
    'summary': """Product Cost Price Will be Visible Only for Specified Users in the Group""",
    'version': '10.0.1.0.0',
    'description': """Product cost price will be visible only users in group""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'http://www.cybrosys.com',
    'category': 'Sales',
    'depends': ['base', 'purchase'],
    'license': 'AGPL-3',
    'data': [
        'security/view_cost_price.xml',
        'views/hide_product_cost.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'demo': [],
    'installable': True,
    'auto_install': False,

}