class SpecialChar():
    @classmethod
    def add_special_char(cls, elements):
        return list(set(elements + cls.all_special_char()))
        
    @staticmethod
    def all_special_char():
        return [
            '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
            '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\',
            ';', ':', '\'', '"', '<', '>', ',', '.', '/', '?'
        ]