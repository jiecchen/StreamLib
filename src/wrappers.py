from functools import wraps

# class ObjectCalc:
#     """
#     Abstract class that can be decorated by @directCalc
#     """
#     def _calc(self, *args, **kwargs):
#         pass


# def directCalc(obj):
#     """
#     given an instance with method .calc()
#     return a function that directly call .calc()
#     """
#     # @wraps(obj)
        
#     if not hasattr(obj, '_calc'):
#         raise AttributeError
#     def _wappers(*args, **kwargs):
#         return obj._calc(*args, **kwargs)
#     return _wappers

