def optimal_pickup(pairs, slots):
    chosen_items_with_strategy = []

    for pair in pairs:
        item1, item2 = pair
        # Проверяем, нужны ли эти предметы
        need_item1 = item1 in slots and (slots[item1] is False or (isinstance(slots[item1], int) and slots[item1] > 0))
        need_item2 = item2 in slots and (slots[item2] is False or (isinstance(slots[item2], int) and slots[item2] > 0))

        # Выбираем предмет с учетом стратегии
        if need_item1 and need_item2:
            # Если нужны оба предмета, выбираем тот, который встречается реже в последующих парах
            future_count_item1 = sum(item1 in future_pair for future_pair in pairs[pairs.index(pair) + 1:])
            future_count_item2 = sum(item2 in future_pair for future_pair in pairs[pairs.index(pair) + 1:])
            if future_count_item1 <= future_count_item2:
                chosen_item = item1
            else:
                chosen_item = item2
        elif need_item1:
            chosen_item = item1
        elif need_item2:
            chosen_item = item2
        else:
            chosen_item = "Пропуск"

        # Обновляем слоты и добавляем выбранный предмет в список
        if chosen_item != "Пропуск":
            if isinstance(slots[chosen_item], int):
                slots[chosen_item] -= 1
            else:
                slots[chosen_item] = True
        chosen_items_with_strategy.append(chosen_item)

    return chosen_items_with_strategy


HELMET = "шлем"
SHOULDER = "наплечники"
CAPE = "плащ"
ARMOR = "броня"
MITTENS = "рукавицы"
BELT = "пояс"
PANTS = "штаны"
BOOTS = "ботинки"
TWO_HANDED_WEAPON = "двуручное оружие"
ONE_HANDED_WEAPON = "одноручное оружие"
SPECIAL_WEAPON = "специальное оружие"
LEFT_HANDED_WEAPON = "оружие для левой руки"
RING = "кольцо"
CUFFS = "наручи"
SHIRT = "рубаха"
AMULET = "амулет"
EARRING = "серьга"

# Пары вариантов выбора вещей в розыгрыше
# (заполнить своими вариантами используя переменные выше и структуру данных items_pairs)
items_pairs = [
    (SHIRT, RING),
    (PANTS, SHIRT),
    (RING, BELT),
    (CAPE, HELMET),
    (CUFFS, ONE_HANDED_WEAPON),
    (RING, EARRING),
    (SHOULDER, BOOTS),
    (CAPE, EARRING),
    (AMULET, SPECIAL_WEAPON),
    (CAPE, SPECIAL_WEAPON),
    (PANTS, RING),
    (ARMOR, BOOTS),
    (BOOTS, SPECIAL_WEAPON),
    (MITTENS, ARMOR),
    (SHOULDER, LEFT_HANDED_WEAPON),
    (SHOULDER, SHIRT),
    (SHOULDER, ONE_HANDED_WEAPON),
    (EARRING, LEFT_HANDED_WEAPON),
    (AMULET, TWO_HANDED_WEAPON),
]

# Необходимый набор вещей для заполнения
required_slots = {
    HELMET: False,
    SHOULDER: False,
    CAPE: False,
    ARMOR: False,
    MITTENS: False,
    BELT: False,
    PANTS: False,
    BOOTS: False,
    TWO_HANDED_WEAPON: False,
    # ONE_HANDED_WEAPON: False, # Опциональный вариант (раскомментировать если нужно)
    SPECIAL_WEAPON: False,
    # LEFT_HANDED_WEAPON: False, # Опциональный вариант (раскомментировать если нужно)
    RING: 2,  # Два слота под кольца
    CUFFS: False,
    SHIRT: False,
    AMULET: False,
    EARRING: 2,  # Два слота под серьги
}

chosen_items = optimal_pickup(items_pairs, required_slots)
# результаты оптимального выбора возвращаются в том же порядке, в котором были определенны розыгрыши бг items_pairs
print(chosen_items)
