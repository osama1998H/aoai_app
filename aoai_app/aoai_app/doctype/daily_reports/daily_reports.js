// Copyright (c) 2022, Osama and contributors
// For license information, please see license.txt

// apply filter on task Department child table
frappe.ui.form.on('Daily Reports', {
	refresh: function (frm) {
		frm.set_query('task', 'today_achievements', function (doc, cdt, cdn) {
			var d = locals[cdt][cdn];
			return {
				filters: [
					['Daily Report Task', 'department', 'in', frm.doc.department]
				]
			};
		});
	}
});