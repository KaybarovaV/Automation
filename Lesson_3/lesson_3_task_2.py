from z_smartphone import Smartphone
catalog = [
    Smartphone("samsung", "galaxy", "+79199199191"),
    Smartphone("xiaomi", "13Ultra", "+79299199191"),
    Smartphone("google", "pixel", "+79399199191"),
    Smartphone("realme", "10", "+79499199191"),
    Smartphone("iphone", "13pro", "+79599199191")
    ]

for phone in catalog:
    print(f"{phone.ph_brand} - {phone.ph_model}. {phone.ph_number}")