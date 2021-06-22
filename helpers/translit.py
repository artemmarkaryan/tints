RU_CYR_TO_LAT_DICT = {
    u"А": u"A", u"а": u"a",
    u"Б": u"B", u"б": u"b",
    u"В": u"V", u"в": u"v",
    u"Г": u"G", u"г": u"g",
    u"Д": u"D", u"д": u"d",
    u"Е": u"E", u"е": u"e",
    u"Ё": u"YO", u"ё": u"yo",
    u"Ж": u"ZH", u"ж": u"zh",
    u"З": u"Z", u"з": u"z",
    u"И": u"I", u"и": u"i",
    u"Й": u"J", u"й": u"j",
    u"К": u"K", u"к": u"k",
    u"Л": u"L", u"л": u"l",
    u"М": u"M", u"м": u"m",
    u"Н": u"N", u"н": u"n",
    u"О": u"O", u"о": u"o",
    u"П": u"P", u"п": u"p",
    u"Р": u"R", u"р": u"r",
    u"С": u"S", u"с": u"s",
    u"Т": u"T", u"т": u"t",
    u"У": u"U", u"у": u"u",
    u"Ф": u"F", u"ф": u"f",
    u"Х": u"H", u"х": u"h",
    u"Ц": u"C", u"ц": u"c",
    u"Ч": u"CH", u"ч": u"ch",
    u"Ш": u"SH", u"ш": u"sh",
    u"Щ": u"SZ", u"щ": u"sz",
    u"Ъ": u"#", u"ъ": u"#",
    u"Ы": u"Y", u"ы": u"y",
    u"Ь": u"", u"ь": u"",
    u"Э": u"EH", u"э": u"eh",
    u"Ю": u"JU", u"ю": u"ju",
    u"Я": u"JA", u"я": u"ja",
}

def ru_to_en(s: str) -> str:
    s = s.strip()
    s = s.replace(" ", "-")
    new_s = []
    for c in s:
        new_c = RU_CYR_TO_LAT_DICT.get(c)
        c_to_append = new_c if new_c is not None else c
        new_s.append(c_to_append)
    return "".join(new_s).lower()