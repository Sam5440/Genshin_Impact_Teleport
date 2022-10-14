def remove_start_space(s):
    if s.startswith(" "):
        return remove_start_space(s[1:])
    else:
        return s
print(remove_start_space("  123     111 "))

    