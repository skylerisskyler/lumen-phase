# Phase Lighting
### Home Assistant Advanced Lighting Control Integration

#### Config Example
```yaml
phase_lighting:
  lights:
    - entity_id: light.living_room
      layers:
          context: doorbell
          style:
            color: red
```