from osv import fields,osv


class product_product(osv.osv):
    _inherit = "product.product"
    
    _columns = {
        "is_maintenance" : fields.boolean('Is Maintenance?'),
    }
    
product_product()