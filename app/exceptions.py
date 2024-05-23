from .types import GroupType


class InvlidGroupError(Exception):
    """Raised when invalid group type is passed."""

    def __init__(self, group_type: str | None = None):
        super().__init__(
            "Invalid group type{}. Allowed values are: {}".format(
                "" if group_type is None else f": '{group_type}'",
                GroupType.values(),
            )
        )
        self.group_type = group_type
