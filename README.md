# Workspace Permissions
Manage the availability of workspaces within Frappe/ ERPNext (sidebar) based on user-roles.

## Features
Configure foreach workspace, which roles can access / can not access a workspace

-   As a whitelist (means, we manage roles, that get access) -> “Visible To Roles”
-   As a blacklist (means, we manage roles, that can NOT get access) -> “Hidden to Roles”
-   Special handling for the "Administrator"-User, as we don't want to restrict anything for that user.
	- That user won't get affected by the configuration, even if he has one of the black-listed roles assigned
-   Hide section-names, if there are no more workspaces available for the same

**ATTENTION**
*This app will only work with a **modification** to the Frappe-Core,  `frappe/frappe/boot.py`. Right now there is no other option to get this functionality integrated*.

We have included a script that will "Monkey Patch" the relevant file/method. There is no need to manually modify any file. Therefore it is also no big deal to update Frappe later on - after updating (what would remove the modification), you just need to make sure to execute the given "seeds" once again.

## Dependency
-   Frappe/ ERPNext v13

## Install on Self-Hosted
> Remeber to replace  `MY_SITE`  with your site name.

    cd frappe-bench
    bench get-app https://github.com/pstuhlmueller/workspaceperms.git
    bench --site MY_SITE install-app workspaceperms
    # This will do the modification within frappe/frappe/boot.py
    bench execute workspaceperms.seeds.execute
    # You need to run `bench restart` once, as otherwise the modification to boot.py won't take effect
    bench restart


## Configuration
1. Go (via awesomebar) into `"Workspace Perms List"` 
2. Add a new `Workspace Perms` document
3. Select the relevant workspace
4. Set the permissions ("Visible To Roles" and/or "Hidden to Roles") as relevant for your scenario

*Hint: Instead of manually adding each Workspace Perm manually, you could also think about preparing a xlsx-file and go with the "Data Import"..*

# License
GPLv3
