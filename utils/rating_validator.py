from rest_framework import serializers

def rating_validator(val: int) -> int:
    if isinstance(val, int):
        if (val > 5) or (val < 1):
            raise serializers.ValidationError({'rating':'Value must be between 1 and 5'})
        else:
            return int(val)
    else:
        raise serializers.ValidationError({'rating':'Value must be an integer'})
