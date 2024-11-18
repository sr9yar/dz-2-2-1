ids = {
    'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]
  }



def main(ids: dict[str, list[int]]) -> None:

  all_values = []

  for id_list in ids.values():
    all_values += id_list
  
  unique_values = set(all_values)

  print(f"Результат: {{{', '.join(map(str, unique_values))}}}")



main(ids)
