def update_file(import_file, remove_list):

  with open(import_file, "r") as file:
    ip_addresses = file.read()

  ip_addresses = ip_addresses.split()

  for element in remove_list:    
    if element in ip_addresses:
      ip_addresses.remove(element)

  ip_addresses = " ".join(ip_addresses)

  with open(import_file, "w") as file:
    file.write(ip_addresses)

update_file("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

with open("allow_list.txt", "r") as file:
  text = file.read()

print(text)
