import frappe
from workspaceperms.workspaceperms.doctype.workspace_perms.workspace_perms import get_workspace_perm_from_cache
from frappe.model.base_document import get_controller

@frappe.whitelist()
def get_desk_sidebar_items_v2():
	final_result = []
	from frappe.desk.desktop import get_desk_sidebar_items
	workspaces =  get_desk_sidebar_items()

	user_roles = set(frappe.get_roles())
	workspace_perm = get_workspace_perm_from_cache()

	for workspace in workspaces:
		if workspace["name"] in workspace_perm and frappe.session.user != "Administrator":
			if len(workspace_perm[workspace.name].get("visible_to_roles", set([]))) and not (user_roles & workspace_perm[workspace.name].get("visible_to_roles", set([]))):
				continue
			if len(user_roles & workspace_perm[workspace.name].get("hidden_to_roles", set([]))):
				continue
			
		final_result.append(workspace)

	return final_result

def load_desktop_data_v2(bootinfo):
	bootinfo.allowed_workspaces = get_desk_sidebar_items_v2()
	bootinfo.module_page_map = get_controller("Workspace").get_module_page_map()
	bootinfo.dashboards = frappe.get_all("Dashboard")