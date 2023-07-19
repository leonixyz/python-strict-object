import pytest
from typing import List, Union, Optional

from strictobject import StrictObject


def test_strict_object_1() -> None:
    """
    Validate basic types attributes
    """
    class Test2(StrictObject):
        # booleans
        my_bool: bool
        # numeric types
        my_int: int
        my_float: float
        my_complex: complex
        # sequences
        my_tuple: tuple
        my_list: list
        my_range: range
        # strings
        my_str: str
        # binary
        my_bytes: bytes
        my_bytearray: bytearray
        # sets
        my_set: set
        my_frozenset: frozenset
        # dictionaries
        my_dict: dict

    Test2(
        my_bool=True,
        my_int=42,
        my_float=3.14159,
        my_complex=complex(1, 1),
        my_tuple=(1, 2, 3),
        my_list=[1,2,3],
        my_range=range(4),
        my_str="hello",
        my_bytes=b"hello",
        my_bytearray=bytearray(b'\xf0\xf1\xf2'),
        my_set=set([1,2,3]),
        my_frozenset=frozenset([1,2,3]),
        my_dict={"1":1, "2":2, "3":3},
    )

    with pytest.raises(TypeError):
        Test2(
            my_bool="maybe", # invalid
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int="42", # invalid
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float="3.14159", # invalid
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=1, # invalid
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=[1, 2, 3], # invalid
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=(1,2,3), # invalid
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=(1, 2, 3), # invalid
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str=b"hello", # invalid
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes="hello", # invalid
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=b'\xf0\xf1\xf2', # invalid
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=(1,2,3), # invalid
            my_frozenset=frozenset([1,2,3]),
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=(1,2,3), # invalid
            my_dict={"1":1, "2":2, "3":3},
        )
    with pytest.raises(TypeError):
        Test2(
            my_bool=True,
            my_int=42,
            my_float=3.14159,
            my_complex=complex(1, 1),
            my_tuple=(1, 2, 3),
            my_list=[1,2,3],
            my_range=range(4),
            my_str="hello",
            my_bytes=b"hello",
            my_bytearray=bytearray(b'\xf0\xf1\xf2'),
            my_set=set([1,2,3]),
            my_frozenset=frozenset([1,2,3]),
            my_dict=(1,2,3), # invalid
        )


def test_strict_object_2() -> None:
    """
    All non-Optional attributes must be declared during initialization
    """
    class Test0(StrictObject):
        num: int
        word: str

    with pytest.raises(TypeError):
        Test0(num=1)


def test_strict_object_3() -> None:
    """
    Validate `Union[int, str]` attributes
    """
    class Test3(StrictObject):
        str_or_int: Union[str, int]

    assert Test3(str_or_int="1")
    assert Test3(str_or_int=1)
    with pytest.raises(TypeError):
        Test3(str_or_int=None)


def test_strict_object_4() -> None:
    """
    Validate `Optional[Union[str, int]]` attributes
    """
    class Test4(StrictObject):
        optional_str_or_int: Optional[Union[str, int]]

    assert Test4(optional_str_or_int="1")
    assert Test4(optional_str_or_int=1)
    assert Test4(optional_str_or_int=None)
    with pytest.raises(TypeError):
        Test4(optional_str_or_int=[])


def test_strict_object_5() -> None:
    """
    Validate `List[int]` attributes
    """
    class Test5(StrictObject):
        list_of_int: List[int]

    assert Test5(list_of_int=[0,1,2,3])
    assert Test5(list_of_int=[0,-1,-2,-3])
    assert Test5(list_of_int=[])
    with pytest.raises(TypeError):
        Test5(list_of_int=["1","2","3"])


def test_strict_object_6() -> None:
    """
    Validate `List[Union[int,str]]` attributes
    """
    class Test6(StrictObject):
        list_of_union: List[Union[int,str]]

    assert Test6(list_of_union=[0,"a",2,"b"])
    assert Test6(list_of_union=["a",-1,"b",-3])
    assert Test6(list_of_union=[])
    with pytest.raises(TypeError):
        Test6(list_of_union=[None])


def test_strict_object_7() -> None:
    """
    Validate `Optional[List[Union[int,str]]]` attributes
    """
    class Test7(StrictObject):
        optional_list_of_union: Optional[List[Union[int,str]]]

    assert Test7(optional_list_of_union=[0,"a",2,"b"])
    assert Test7(optional_list_of_union=["a",-1,"b",-3])
    assert Test7(optional_list_of_union=[])
    assert Test7(optional_list_of_union=None)
    with pytest.raises(TypeError):
        Test7(optional_list_of_union=[None])


def test_strict_object_8() -> None:
    """
    Validate `Optional[List[Optional[Union[int,str]]]]` attributes
    """
    class Test8(StrictObject):
        optional_list_of_optional_union: Optional[List[Optional[Union[int,str]]]]

    assert Test8(optional_list_of_optional_union=[0,"a",2,"b"])
    assert Test8(optional_list_of_optional_union=["a",-1,"b",-3])
    assert Test8(optional_list_of_optional_union=[])
    assert Test8(optional_list_of_optional_union=None)
    assert Test8(optional_list_of_optional_union=[None])
    with pytest.raises(TypeError):
        Test8(optional_list_of_optional_union=[[]])


def test_strict_object_9() -> None:
    """
    Validate `List[List[int]]` attributes
    """
    class Test9(StrictObject):
        list_of_lists_of_int: List[List[int]]

    assert Test9(list_of_lists_of_int=[])
    assert Test9(list_of_lists_of_int=[[]])
    assert Test9(list_of_lists_of_int=[[],[]])
    assert Test9(list_of_lists_of_int=[[1],[2]])
    assert Test9(list_of_lists_of_int=[[1,2,3],[4,5,6]])
    with pytest.raises(TypeError):
        Test9(list_of_lists_of_int=[None,1,2,None])
    with pytest.raises(TypeError):
        Test9(list_of_lists_of_int=[1])
    with pytest.raises(TypeError):
        Test9(list_of_lists_of_int=[[""]])


def test_strict_object_10() -> None:
    """
    Validate custom type attributes
    """
    class MyObject:
        pass

    class Test10(StrictObject):
        obj: MyObject

    assert Test10(obj=MyObject())
    with pytest.raises(TypeError):
        Test10(obj=1)


def test_strict_object_11() -> None:
    """
    Refuse to validate unknown type attributes
    """
    class MyObject:
        __origin__ = "not Union and not List"

    class Test11(StrictObject):
        obj: MyObject

    with pytest.raises(RuntimeError):
        Test11(obj=MyObject())


def test_strict_object_12() -> None:
    """
    Validate attributes having custom validators
    """
    class Test11(StrictObject):
        pippo: str
        def validate_pippo(self, pippo) -> bool:
            return pippo.startswith("hello")

    assert Test11(pippo="hello world")
    assert Test11(pippo="hello pippo")
    with pytest.raises(TypeError):
        Test11(pippo="does not start with hello")


def test_strict_object_13() -> None:
    """
    Refuse validating attributes having custom validators but incorrect type declaration
    """
    class Test11(StrictObject):
        pippo: Union[str, int]
        def validate_pippo(self, pippo) -> bool:
            if isinstance(pippo, int):
                return pippo == 42
            elif isinstance(pippo, str):
                return pippo.startswith("hello")

    assert Test11(pippo=42)
    assert Test11(pippo="hello world")
    assert Test11(pippo="hello pippo")
    with pytest.raises(TypeError):
        Test11(pippo=13)
    with pytest.raises(TypeError):
        Test11(pippo="does not start with hello")
    with pytest.raises(TypeError):
        Test11(pippo="42")
