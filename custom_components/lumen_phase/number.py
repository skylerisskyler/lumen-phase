from homeassistant.components.number.NumberEntity import NumberEntity

class VariableNumber(NumberEntity):
    # Implement one of these methods.

    def __init__(self, hass, config):
        self.hass = hass
        self._value = 5.0 
        
    @property
    def name(self) -> str:
        """Return the name of the entity."""
        return 'entity_name'
    
    @property
    def value(self) -> float:
        """Return the current value."""
        return self._value
    
    @property
    def min_value(self) -> float:
        """Return the minimum value."""
        return 0.0
    
    @property
    def max_value(self) -> float:
        """Return the maximum value."""
        return 10.0
    
    @property
    def step(self) -> float:
        """Return the step size."""
        return 1.0
    
    @property
    def mode(self) -> str:
        return "auto"
    
    
    
    def set_value(self, value: float) -> None:
        """Update the current value."""
        self.value = value