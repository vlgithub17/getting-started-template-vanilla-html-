import re

def update_js_file(new_service_id, new_owner_id):
    with open('getting-started-template-vanilla-html-/init.js', 'r') as file:
        content = file.read()

    pattern = r"Skapi\('([^']*)', '([^']*)'\)"

    new_content = re.sub(pattern, f"Skapi('{new_service_id}', '{new_owner_id}')", content)

    with open('getting-started-template-vanilla-html-/init.js', 'w') as file:
        file.write(new_content)

    # print(f"Updated 'init.js' with service_id: {new_service_id} and owner_id: {new_owner_id}")

update_js_file('new_service_id', 'new_owner_id')
