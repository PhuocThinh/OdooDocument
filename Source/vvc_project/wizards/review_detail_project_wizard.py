from odoo import api, models, fields

class ReviewDetailProjectWizard(models.TransientModel):
    _name = 'review.detail.wizard.project'
    _description = 'Project Review Detail Wizard'
    content = fields.Html(string='Content')
    status = fields.Selection([('new', "New"),
                               ('done', "Done"),
                               ('cancel', "Cancel")
                               ], 'Status', default='new', required=True)
    review_id = fields.Many2one('review.history.project.wizard', string="Review")
