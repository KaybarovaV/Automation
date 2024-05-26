from z_address import Address
from z_mailing import Mailing

to_address = Address(655017, "Abakan", "Торосова", "9", 222)
from_address = Address(655017, "Abakan", "Торосова", "9a", 222)

mail = Mailing(to_address, from_address, 354, "TR10045362U")
print(f"Отправление {mail.track} из {from_address.index}, {from_address.city}, {from_address.street}, {from_address.house} - {from_address.apartment} в {to_address.index}, {to_address.city}, {to_address.street}, {to_address.house} - {to_address.apartment}. Стоимость {mail.cost} рублей.")