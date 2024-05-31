def is_context_manager(obj: object):
    return hasattr(obj, "__enter__") and hasattr(obj, "__exit__")


class ContextManager:
    def __enter__(self):
        return "beegeek"

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True


print(is_context_manager(ContextManager()))
