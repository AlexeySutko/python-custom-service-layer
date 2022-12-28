from abc import abstractmethod


class BaseService:

    def __new__(cls, *args, **kwargs):
        fields = [key.split("_")[0] for key in cls.__dict__.keys() if str(key).endswith("_field")]
        new_instance = super().__new__(cls)
        new_instance.fields = fields
        return new_instance


class ServiceClass(BaseService):

    def __init__(self):
        self.result = None
        self.prepared_data = {}

    @classmethod
    def process(cls, **kwargs):
        instance = cls()
        instance._prepare_data(**kwargs)
        return instance.output()

    @abstractmethod
    def output(self):
        pass

    def _prepare_data(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.fields:
                self.prepared_data[key] = value