from odoo import api, models, fields

class ReviewHistoryProjectWizard(models.TransientModel):
    _name = "review.history.project.wizard"
    _description = "Project Review History Wizard"
    hours = fields.Float('Hours')
    note = fields.Text("Note", required=True)
    type = fields.Selection([
                                ('code', 'Code'),
                                ('test_case', "Test Case"),
                                ('ut', "Unit Test")
                            ], 'Type', default='code', required=True)
    number_of_issue = fields.Integer(string="Number of issue", compute="compute_number_of_issue")
    detail_ids = fields.One2many('review.detail.wizard.project', 'review_id', string="Issue Details")
    task_id = fields.Many2one('project.task', string="Task", default=lambda self: self.env.context.get('active_id'), required=True)
    project_id = fields.Many2one('project.project', string="Project", compute="get_name_project")
    user_id = fields.Many2one('res.users', "User", default=lambda self: self.env.user, required=True)

    @api.multi
    @api.depends('detail_ids')
    def compute_number_of_issue(self):
        number_issue = len(self.detail_ids)
        self.number_of_issue = number_issue
    @api.multi
    @api.depends('task_id')
    def get_name_project(self):
        for project in self:
            project.project_id = project.task_id.project_id.id

    @api.multi
    def create_review_history_project(self):
        project_review_history = self
        name = project_review_history.note
        task_id = self.env.context.get('active_id')
        project_id = project_review_history.project_id.id
        current_date = fields.Date.from_string(fields.Date.context_today(self))
        current_employee = self.env.user.id
        unit_amount = project_review_history.hours
        account_id = project_review_history.user_id.id
        types = project_review_history.type
        number_of_issue = project_review_history.number_of_issue
        detail_ids = project_review_history.detail_ids

        self.env['account.analytic.line'].create({
            'name': name,
            'date': current_date,
            'employee_id' : current_employee,
            'amount': unit_amount,
            'task_id': task_id,
            'project_id': project_id,
            'account_id':account_id
        })

        return_review_id = self.env['review.history.project'].create({
            'note':name,
            'type': types,
            'hours':unit_amount,
            'project_id':project_id,
            'number_of_issue':number_of_issue,
            'date': current_date,
            'user_id': current_employee,
            'task_id':task_id
        })

        review_id = return_review_id.id
        if detail_ids:
            for project_review_detail in detail_ids:
                self.env['review.detail.project'].create({
                    'content': project_review_detail.content,
                    'status': project_review_detail.status,
                    'review_id': review_id,
                    'project_id': project_id
                })
        return True

