from tabulate import tabulate
import requests

def category_data():
    url = "http://127.0.0.1:8000/"

    response = requests.get(url)
    return response.json()

def category_create(name, parent=None):
    url = "http://127.0.0.1:8000/"

    payload = {"name": name}
    if parent:
        payload = {"name": name, "parent":parent}
    headers = {"content-type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def category_update(pk, name, parent=None):
    url = f"http://127.0.0.1:8000/{pk}/"

    payload = {"name": name}
    if parent:
        payload = {"name": name,
                   "parent": parent}
    headers = {"content-type": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    return response.json()

def category_delete(pk):
    url = f"http://127.0.0.1:8000/{pk}/"
    response = requests.delete(url)
    try:
        return response.json()
    except ValueError:
        return {"status": response.status_code, "message": "Deleted(no content)"}
# ----------------------------------------------------------------------------------------------------------
# new_cartoon = category_create("Zootopia 3", 2)
# print(new_cartoon)
# ----------------------------------------------------------------------------------------------------------
# all_info = category_data()
# datas = []
# headers = ["ID", "Name", "Parent"]
# for category in all_info:
#     datas.append([category.get("id"),category.get("name"), category.get("parent")])
#
# print(tabulate(tabular_data=datas, headers=headers, tablefmt='grid'))
# ----------------------------------------------------------------------------------------------------------
# new_category = category_update(6, "Uzbek movies", 1)
# print(new_category)

# ----------------------------------------------------------------------------------------------------------
# delete_one = category_delete(15)
# print(delete_one)
# ----------------------------------------------------------------------------------------------------------
















