from odoo import fields, models, api

class ReviewHistoryProject(models.Model):
    _name = 'review.history.project'
    _description = 'Project Review History'
    user_id = fields.Many2one('res.users',"User", default=lambda self: self.env.user, required=True)
    date = fields.Date('Date', default=fields.Date.context_today, required=True)
    hours = fields.Float('Hours')
    task_id = fields.Many2one('project.task', string="Task", default= lambda self: self.env.context.get('active_id'), required=True)
    note = fields.Text("Note")
    project_id = fields.Many2one('project.project', string="Project", compute="get_name_project")
    type = fields.Selection([
                                ('code', 'Code'),
                                ('test_case', "Test Case"),
                                ('ut', "Unit Test")
                            ], 'Type', default='code', required=True)
    detail_ids = fields.One2many('review.detail.project','review_id', string="Issue Details")
    number_of_issue = fields.Integer(string="Number of issue", compute="compute_number_of_issue")

    @api.multi
    @api.depends('task_id')
    def get_name_project(self):
        for project in self:
            project.project_id = project.task_id.project_id.id

    @api.multi
    @api.depends('detail_ids')
    def compute_number_of_issue(self):
        number_issue = len(self.detail_ids)
        self.number_of_issue = number_issue
