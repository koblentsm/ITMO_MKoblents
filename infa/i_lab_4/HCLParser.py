from Subject import Subject
from ScheduleDay import ScheduleDay

class HCLParser:
    def parse_file(self, filename: str) -> ScheduleDay:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        return self.parse(text)

    def parse(self, text: str) -> ScheduleDay:
        text = self._remove_comments(text)
        day_name = self._extract_day_name(text)
        content = self._extract_top_level_block(text)
        # lessons_list_content = self._extract_lessons_list_content(content)
        # lesson_blocks = self._split_lesson_blocks(lessons_list_content)
        schedule = ScheduleDay(day_name)
        key_value_pairs = self._extract_all_key_value_pairs(content)
        for key, value in key_value_pairs.items():
            if key == "classes":
                # Обрабатываем список занятий
                lesson_blocks = self._split_lesson_blocks(value)
                for block in lesson_blocks:
                    subject = Subject.from_hcl_block(block)
                    schedule.add_subject(subject)
            else:
                schedule.other[key]=value
               
        # for block in lesson_blocks:
        #     subject = Subject.from_hcl_block(block)
        #     schedule.add_subject(subject)

        return schedule
    
    def _remove_comments(self, text: str) -> str:
        result = []
        i = 0
        n = len(text)
        in_string = False
        while i < n:
            char = text[i]
            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                in_string = not in_string
                result.append(char)
                i += 1
                continue

            if in_string:
                result.append(char)
                i += 1
                continue

            if i + 1 < n and char == '/' and text[i + 1] == '*':
                i += 2  
                while i + 1 < n:
                    if text[i] == '*' and text[i + 1] == '/':
                        break
                    i += 1
                continue
            if i + 1 < n and char == '/' and text[i + 1] == '/':
                while i < n and text[i] != '\n':
                    i += 1
                if i < n:
                    result.append('\n')
                continue
            result.append(char)
            i += 1

        return ''.join(result)


    def _extract_day_name(self, text: str) -> str:
        i = 0
        n = len(text)
        while i < n and text[i].isspace():
            i += 1
        start = i
        while i < n and (text[i].isalnum() or text[i] == '_'):
            i += 1
        return text[start:i]

    def _extract_top_level_block(self, text: str) -> str:
        i = 0
        n = len(text)
        while i < n:
            if i + 3 <= n and text[i] == '=' and text[i+1].isspace() and text[i+2] == '{':
                i += 3
                break
            i += 1
        if i >= n:
            raise ValueError("Не найдено '= {'")

        brace_level = 1
        in_string = False
        start = i

        while i < n and brace_level > 0:
            char = text[i]
            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                in_string = not in_string
            elif not in_string:
                if char == '{':
                    brace_level += 1
                elif char == '}':
                    brace_level -= 1
            i += 1

        if brace_level != 0:
            raise ValueError("Незакрытый блок")
        return text[start:i-1].strip()

    def _extract_lessons_list_content(self, text: str) -> str:
        i = 0
        n = len(text)
        in_string = False
        bracket_level = 0

        while i < n:
            char = text[i]
            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                in_string = not in_string

            if not in_string:
                if char == '[':
                    bracket_level += 1
                    if bracket_level == 1:
                        list_start = i + 1
                        i += 1
                        while i < n and bracket_level > 0:
                            char = text[i]
                            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                                in_string = not in_string
                            elif not in_string:
                                if char == '[':
                                    bracket_level += 1
                                elif char == ']':
                                    bracket_level -= 1
                            i += 1
                        if bracket_level == 0:
                            return text[list_start:i-1].strip()
                        else:
                            raise ValueError("Незакрытый список")
                elif char == ']':
                    bracket_level -= 1
            i += 1
        return ""

    def _split_lesson_blocks(self, text: str) -> list:
        blocks = []
        i = 0
        n = len(text)
        in_string = False
        brace_level = 0
        block_start = -1

        while i < n:
            char = text[i]
            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                in_string = not in_string

            if not in_string:
                if char == '{' and brace_level == 0:
                    block_start = i + 1
                    brace_level = 1
                elif char == '{':
                    brace_level += 1
                elif char == '}':
                    brace_level -= 1
                    if brace_level == 0 and block_start != -1:
                        blocks.append(text[block_start:i].strip())
            i += 1

        return blocks
    
    def _extract_all_key_value_pairs(self, text: str) -> dict:
        pairs = {}
        i = 0
        n = len(text)
        in_string = False
        brace_level = 0

        while i < n:
            while i < n and text[i].isspace():
                i += 1
            if i >= n:
                break

            if not in_string and text[i].isalpha():
                key_start = i
                while i < n and (text[i].isalnum() or text[i] == '_'):
                    i += 1
                key = text[key_start:i].strip()

                while i < n and (text[i] == '=' or text[i].isspace()):
                    i += 1

                if i < n:
                    if text[i] == '"':
                        i += 1
                        val_start = i
                        while i < n:
                            if text[i] == '"' and (i == 0 or text[i - 1] != '\\'):
                                break
                            i += 1
                        value = text[val_start:i]
                        i += 1 
                    elif text[i] == '{':
                        brace_level = 1
                        val_start = i
                        i += 1
                        while i < n and brace_level > 0:
                            char = text[i]
                            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                                in_string = not in_string
                            elif not in_string:
                                if char == '{':
                                    brace_level += 1
                                elif char == '}':
                                    brace_level -= 1
                            i += 1
                        value = text[val_start:i-1] 
                    elif text[i] == '[':
                        brace_level = 1
                        val_start = i
                        i += 1
                        while i < n and brace_level > 0:
                            char = text[i]
                            if char == '"' and (i == 0 or text[i - 1] != '\\'):
                                in_string = not in_string
                            elif not in_string:
                                if char == '[':
                                    brace_level += 1
                                elif char == ']':
                                    brace_level -= 1
                            i += 1
                        value = text[val_start:i-1]  
                    else:
                        val_start = i
                        while i < n and text[i] not in ',\n}':
                            i += 1
                        value = text[val_start:i].strip()
                else:
                    value = ""

                pairs[key] = value

            i += 1

        return pairs


