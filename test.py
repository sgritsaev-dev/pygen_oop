class Config:
    _instance=None
    program_name='GenerationPy'
    environment='release'
    loglevel='verbose'
    version='1.0.0'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:                       # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
            cls._instance.program_name='GenerationPy'
            cls._instance.environment='release'
            cls._instance.loglevel='verbose'
            cls._instance.version='1.0.0'
        return cls._instance
    
    def __init__(self, prog=program_name, env=environment, log=loglevel, ver=version) -> None:
        self.program_name=prog
        self.environment=env
        self.loglevel=log
        self.version=ver
    
    
config = Config(123, 45, 67)

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)