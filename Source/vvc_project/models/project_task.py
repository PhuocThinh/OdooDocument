from odoo import fields, models, api

class ProjectTask(models.Model):
    _inherit = 'project.task'
    review_ids = fields.One2many('review.history.project', 'task_id', string="Review")
    git_branch = fields.Char('Git branch')