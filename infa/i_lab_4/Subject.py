from Address import Address
from Format import Format
from Type import Type

class Subject:
    def __init__(self, name: str, type_: Type, time: str, format_: Format, teacher: str, room: str = "", address: Address = Address.NAN, other = {}):
        self.name = name
        self.type = type_
        self.time = time
        self.format = format_
        self.teacher = teacher
        self.room = room
        self.address = address
        self.other =other

    @classmethod
    def from_hcl_block(cls, block: str) -> 'Subject':
        fields = {}
        i = 0
        n = len(block)
        

        while i < n:
            # Пропускаем пробелы и запятые
            while i < n and (block[i].isspace() or block[i] == ','):
                i += 1
            if i >= n:
                break

            # Читаем ключ (до =)
            if block[i].isalpha():
                key_start = i
                while i < n and (block[i].isalnum() or block[i] == '_'):
                    i += 1
                key = block[key_start:i].strip()

                # Пропускаем =
                while i < n and (block[i] == '=' or block[i].isspace()):
                    i += 1

                # Читаем значение (в кавычках)
                if i < n and block[i] == '"':
                    i += 1
                    val_start = i
                    while i < n:
                        if block[i] == '"' and (i == 0 or block[i - 1] != '\\'):
                            break
                        i += 1
                    value = block[val_start:i]
                    i += 1  # пропустить закрывающую "
                else:
                    # Значение не в кавычках — до конца строки или запятой
                    val_start = i
                    while i < n and block[i] not in ',\n}':
                        i += 1
                    value = block[val_start:i]

                fields[key] = value
            else:
                i += 1

        # Преобразуем строки в Enum
        type_enum = Type(fields.pop("type", "lecture"))
        format_enum = Format(fields.pop("format", "Очный"))
        addr_str = fields.pop("address", "")
        address_enum = Address.NAN if not addr_str or addr_str == "Не указано" else Address(addr_str)
        
        return cls(
            name=fields.get("subject", ""),
            type_=type_enum,
            time=fields.get("time", ""),
            format_=format_enum,
            teacher=fields.get("teacher", ""),
            room=fields.get("room", "").strip(),
            address=address_enum,
            other=fields
        )
    
    def to_yaml_block(self) -> str:
        block = f'  -{self.name}:\n    type: "{self.type.value}"\n    time: "{self.time}"\n    format: "{self.format.value}"\n    teacher: "{self.teacher}"\n    room: "{self.room}"\n    address: "{self.address.value}"\n'
        return block
    
    def to_xml_block(self) -> str:
        lines = []
        lines.append('      <Class>')
        lines.append(f'        <Subject>{self._escape(self.name)}</Subject>')
        lines.append(f'        <Type>{self._escape(self.type.value)}</Type>')
        lines.append(f'        <Time>{self._escape(self.time)}</Time>')
        lines.append(f'        <Format>{self._escape(self.format.value)}</Format>')
        lines.append(f'        <Room>{self._escape(self.room)}</Room>')
        lines.append(f'        <Address>{self._escape(self.address.value)}</Address>')
        lines.append(f'        <Teacher>{self._escape(self.teacher)}</Teacher>')
        lines.append('      </Class>\n')
        return '\n'.join(lines)
    
    def _escape(self, text: str) -> str:
        return (text
                .replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&apos;"))