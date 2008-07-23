##############################################################################
#
# Copyright (c) 2004-2006 TINY SPRL. (http://tiny.be) All Rights Reserved.
#
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from osv import osv, fields
class library_price_category(osv.osv):
    _name = 'library.price.category'
    _description = 'Book Price Category'
    _columns = {
        'name': fields.char('Category', size=64, required=True),
        'price': fields.float('Price', required=True),
        'product_ids': fields.one2many('product.product', 'price_cat', 'Books' ,readonly=True)
    }

    _defaults = {
        'price': lambda *a : 0,
        }
library_price_category()

class library_rack(osv.osv):
    _name = 'library.rack'
    _description="Library Rack"
    _columns = {
        'name': fields.char('Name', size=64,required=True),
        'code' : fields.char('Code', size=16,),
        'active': fields.boolean('Active'),
        }

    _defaults= {
        'active': lambda *a: True
        }
library_rack()

class library_collection(osv.osv):
    _name = 'library.collection'
    _description="Library Collection"
    _columns = {
        'name': fields.char('Name', size=64,required=True),
        'code' : fields.char('Code', size=16,),
        }
library_collection()

class library_author(osv.osv):
    _name = 'library.author'
    _description="Author"
    _columns = {
        'name': fields.char('Name', size=64,required=True, select=True),
        'first_name':fields.char('First Name', size=64),
        'born_date': fields.date('Date of birth'),
        'death_date': fields.date('Date of death'),
        'biography': fields.text('Biography'),
        'note': fields.text('Notes'),
        'editor_ids': fields.many2many('res.partner','author_editor_rel','author_id','partner_id','Editors', select=1), 
    }
    def name_get(self, cr, uid, ids, context={}):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name','first_name'], context)
        return map(lambda x: (x['id'], x['name'] + (x['first_name'] and (', '+x['first_name']) or '')), reads)
library_author()
