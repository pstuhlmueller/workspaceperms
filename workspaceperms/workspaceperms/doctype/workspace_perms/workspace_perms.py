# Copyright (c) 2021, Patrick Stuhlmüller and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class WorkspacePerms(Document):
	def validate(self):
		frappe.cache().set_value("workspace_perm", None)

def get_workspace_perm_from_db(cache = None):
	if not cache:
		cache = frappe.cache()

	sql_query = """SELECT
		perm.name,
		role_link.parentfield AS field,
		CONCAT(
			"[",
			GROUP_CONCAT('"', role_link.role_name, '"'),
			"]"
		) AS val
	FROM
		`tabWorkspace Perms` perm
	INNER JOIN `tabRole Link` role_link ON
		perm.name = role_link.parent
	GROUP BY
		perm.name,
		role_link.parentfield"""
	perm_rows = frappe.db.sql(sql_query, as_dict= True) 

	perm_dict = dict()
	for perm_row in perm_rows:
		if perm_row.name not in perm_dict:
			perm_dict[perm_row.name] = dict()
		perm_dict[perm_row.name][perm_row.field] = set(frappe.parse_json(perm_row.val))

	cache.set_value("workspace_perm", perm_dict)
	return perm_dict

def get_workspace_perm_from_cache(fetch=False):
	cache = frappe.cache()
	if fetch:
		return get_workspace_perm_from_db(cache)
	
	cached_value = cache.get_value("workspace_perm")
	if cached_value:
		return cached_value

	return get_workspace_perm_from_db(cache)