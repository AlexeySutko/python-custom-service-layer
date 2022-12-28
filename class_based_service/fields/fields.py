

class PlaceholderFieldClass:

    @classmethod
    def primitive_field(cls, data_type=None, data=None):
        if not data:
            return None
        if type(data) == data_type:
            return data
        return data_type(data)

    @classmethod
    def string_primitive_field(cls, data=None):

        return str(data)

    @classmethod
    def int_primitive_field(cls, data=None):

        return int(data)

    @classmethod
    def float_primitive_field(cls, data=None):

        return float(data)

    @classmethod
    def bool_primitive_field(cls, data=None):

        return bool(data)

    @classmethod
    def list_field(cls, data=None):

        return list(data)

    @classmethod
    def dict_field(cls, data=None):

        return dict(data)

    @classmethod
    def tuple_field(cls, data=None):

        return tuple(data)

    @classmethod
    def set_field(cls, data=None):

        return set(data)

    @classmethod
    def file_field(cls, data=None):
        pass
