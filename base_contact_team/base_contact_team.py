from osv import osv, fields

class quality_team(osv.osv):
    _name = 'base.contact.team'

    _columns = {
        'name' : fields.char('Name', size=64, required=True, select=True),
        'description' : fields.text('Description'),
    }

quality_team()

class res_partner_job(osv.osv):
    _inherit = 'res.partner.job'

    _columns = {
        'quality_team_id' : fields.many2one('base.contact.team', 'Team'),
    }

res_partner_job()
