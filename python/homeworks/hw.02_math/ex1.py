time = int(input('Сколько секунд?: '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 60
print(f'В указанном количестве секунд: {time}\n'
      f'{hours} часов.\n'
      f'{minutes} минут.\n'
      f'{seconds} секунд.')


input('\n\nНажмите "ENTER" для завершения.')


# Мо варианты ввода

# В указанном количестве секунд: 40000
# 11 часов.
# 6 минут.
# 40 секунд.


# В указанном количестве секунд: 6590
# 1 часов.
# 49 минут.
# 50 секунд.