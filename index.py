from telethon.sync import TelegramClient

api_id = 'XXXXXXXXXXXXXXXXX'
api_hash = 'XXXXXXXXXXXXXXXXX'
proxy = ''
file_session = 'XXXXXXXXXXXXXXXXX'
client = TelegramClient(file_session, api_id, api_hash)

phone_number = 'XXXXXXXXXXXXXXXXX'

client.start(phone_number)
dialogs = client.get_dialogs()
groups = [dialog for dialog in dialogs if dialog.is_group]
user = [dialog for dialog in dialogs if dialog.is_user]
group_info = []
for group in groups:
    # print(group.entity.to_json())
    group_info.append(group.entity.to_dict())
    # group_info.append({
    #     'title': group.title,
    #     'id': group.id
    # })

for info in group_info:
    print("=======================================")
    print(f"Group info: {info}")
    print("=======================================")
    print()
client.disconnect()
