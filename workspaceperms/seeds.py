import frappe

BENCH_PATH = frappe.utils.get_bench_path()

def execute():
	add_boot_overrides()

def add_boot_overrides():
	file_path = "{}/{}".format(BENCH_PATH,
							   "apps/frappe/frappe/boot.py")
	with open(file_path) as f:
		if 'load_desktop_data = load_desktop_data_v2' in f.read():
			return
	with open(file_path, "a+") as f:
		f.write(
			"\nfrom workspaceperms.utils.overrides import load_desktop_data_v2")
		f.write(
			"\nload_desktop_data = load_desktop_data_v2")
		print("frappe/frappe/boot.py modified to activate workspaceperms.")