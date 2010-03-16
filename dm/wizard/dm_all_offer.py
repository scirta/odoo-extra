# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

import wizard
import pooler

def product_offers(self, cr, uid, data, context):
    cr.execute("""select distinct offer_id from dm_offer_step 
                where id in (select distinct offer_step_id 
                  from dm_campaign_proposition_item 
                    where product_id =%s and offer_step_id is not null)""",
                    (str(data['id']),) )
    value = {
    'domain': [('id', 'in', cr.fetchall() )],
    'name': 'Offers',
    'view_type': 'form',
    'view_mode': 'tree,form',
    'res_model': 'dm.offer',
    'context': { },
    'type': 'ir.actions.act_window'
        }
    return value

class wizard_product_offers(wizard.interface):
    states = {
        'init': {
            'actions': [],
            'result': {
                'type': 'action',
                'action': product_offers,
                'state': 'end'
            }
        },
    }
wizard_product_offers("wizard_product_offers")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: