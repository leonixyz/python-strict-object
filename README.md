# strictobject

Lightweight validation for python objects.

Examples:

1. Simple validation
    ```python
    from strictobject import StrictObject

    class A(StrictObject):
        num: int
    
    A(num=0)  # ok
    A(num=42)  # ok
    A(num="not an int")  # will throw a TypeError
    ```
2. Custom validation
    ```python
    from strictobject import StrictObject

    class B(StrictObject):
        fortytwo: Union[int|str]
        # custom validators must by named by "validate_" followed by
        # the class attribute name, and they should return a bool
        def validate_fortytwo(self, val) -> bool:
            return int(val) == 42
    
    B(num=42)  # ok
    B(num="42")  # ok
    B(num=123)  # will throw a TypeError
    ```

Works with all built-in types, and with special types `List`, `Union`, `Optional` from package `typing`.