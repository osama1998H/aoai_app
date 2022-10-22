from . import __version__ as app_version

app_name = "aoai_app"
app_title = "Aoai App"
app_publisher = "Osama"
app_description = "customize for website aoai.io "
app_email = "osamamoh890@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/aoai_app/css/aoai_app.css"
# app_include_js = "/assets/aoai_app/js/aoai_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/aoai_app/css/aoai_app.css"
web_include_css = [
    # "/assets/aoai_app/css/vendor/bootstrap.min.css",
    # "/assets/aoai_app/css/plugins/animation.css",
    # "/assets/aoai_app/css/plugins/feature.css",
    # "/assets/aoai_app/css/plugins/magnify.min.css",
    # "/assets/aoai_app/css/plugins/slick.css",
    # "/assets/aoai_app/css/plugins/slick-theme.css",
    # "/assets/aoai_app/css/plugins/lightbox.css",
    "/assets/aoai_app/css/custom.css",
]
# web_include_js = "/assets/aoai_app/js/aoai_app.js"
web_include_js = [
    # "/assets/aoai_app/js/vendor/modernizr.min.js",
    # "/assets/aoai_app/js/vendor/jquery.min.js",
    # "/assets/aoai_app/js/vendor/bootstrap.min.js",
    # "/assets/aoai_app/js/vendor/popper.min.js",
    # "/assets/aoai_app/js/vendor/waypoint.min.js",
    # "/assets/aoai_app/js/vendor/wow.min.js",
    # "/assets/aoai_app/js/vendor/counterup.min.js",
    # "/assets/aoai_app/js/vendor/feather.min.js",
    # "/assets/aoai_app/js/vendor/sal.min.js",
    # "/assets/aoai_app/js/vendor/masonry.js",
    # "/assets/aoai_app/js/vendor/imageloaded.js",
    # "/assets/aoai_app/js/vendor/magnify.min.js",
    # "/assets/aoai_app/js/vendor/lightbox.js",
    # "/assets/aoai_app/js/vendor/slick.min.js",
    # "/assets/aoai_app/js/vendor/easypie.js",
    # "/assets/aoai_app/js/vendor/text-type.js",
    # "/assets/aoai_app/js/vendor/jquery.style.swicher.js",
    # "/assets/aoai_app/js/vendor/js.cookie.js",
    # "/assets/aoai_app/js/main.js",
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "aoai_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "aoai_app.utils.jinja_methods",
#	"filters": "aoai_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "aoai_app.install.before_install"
# after_install = "aoai_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "aoai_app.uninstall.before_uninstall"
# after_uninstall = "aoai_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "aoai_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"aoai_app.tasks.all"
#	],
#	"daily": [
#		"aoai_app.tasks.daily"
#	],
#	"hourly": [
#		"aoai_app.tasks.hourly"
#	],
#	"weekly": [
#		"aoai_app.tasks.weekly"
#	],
#	"monthly": [
#		"aoai_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "aoai_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "aoai_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "aoai_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"aoai_app.auth.validate"
# ]
