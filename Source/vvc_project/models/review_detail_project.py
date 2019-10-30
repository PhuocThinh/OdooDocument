from odoo import fields, models, api


class ReviewDetailProject(models.Model):
    _name = 'review.detail.project'
    _description = 'Review Detail Project'
    review_id = fields.Many2one('review.history.project', string="Review")
    content = fields.Html(string="Content")
    status = fields.Selection([('new', "New"),
                                ('done', "Done"),
                                ('cancel', "Cancel")], 'Status', required=True)
