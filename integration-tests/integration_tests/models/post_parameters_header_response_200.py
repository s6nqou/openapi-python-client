from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostParametersHeaderResponse200")


@_attrs_define
class PostParametersHeaderResponse200:
    """
    Attributes:
        boolean (bool): Echo of the 'Boolean-Header' input parameter from the header.
        string (str): Echo of the 'String-Header' input parameter from the header.
        number (float): Echo of the 'Number-Header' input parameter from the header.
        integer (int): Echo of the 'Integer-Header' input parameter from the header.
    """

    boolean: bool
    string: str
    number: float
    integer: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boolean = self.boolean

        string = self.string

        number = self.number

        integer = self.integer

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "boolean": boolean,
                "string": string,
                "number": number,
                "integer": integer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        boolean = d.pop("boolean")

        string = d.pop("string")

        number = d.pop("number")

        integer = d.pop("integer")

        post_parameters_header_response_200 = cls(
            boolean=boolean,
            string=string,
            number=number,
            integer=integer,
        )

        post_parameters_header_response_200.additional_properties = d
        return post_parameters_header_response_200

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
