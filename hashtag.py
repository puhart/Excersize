"""
Функция для создания хештегов.
- Должно начинатся со знака #,
- Во всех словах первая буква должна быть заглавная,
- Если окончательный результат длинее 140 символов,
  должно возвращаться False
- Если ввод или результат представляем пустую строку,
  должн возвращаться False
"""

def hashtag():
    name = input('Пожалуйста введите хэштег: \n')
    tag = "".join(name.title().split())
    print("#" + tag)

hashtag()
